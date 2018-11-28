#include <iostream>
#include <vector>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

enum {
	LOWER_BOUND = 1,
	UPPER_BOUND = 100000000000000
};

// Check if it's a palindrome
bool checkFair(int64_t num)
{
	const int numDigits = num > 0 ? log10(num) + 1 : 1;
	char numAsStr[1024];
	sprintf(numAsStr, "%lld", num);

	bool fair = true;
	for(int i = 0; i < numDigits/2; ++i)
	{
		if (numAsStr[i] != numAsStr[numDigits-i - 1])
		{
			fair = false;
		}
	}

	if (fair)
	{
		// std::cout << "digits: " << numDigits << ", num: " << std::string(numAsStr) << std::endl;
	}

	return fair; 
}

void processLine(int lineNum, std::vector<int64_t>& fairSquares)
{
	int64_t lowerBound = 0;
	int64_t upperBound = 0;

	std::cin >> lowerBound;
	std::cin >> upperBound;

	assert(lowerBound > 0);
	assert(upperBound > 0);

	// std::cout << "lower: " << lowerBound << ", upper: " << upperBound << std::endl;

	// How many elements of fairSquares are <= lowerBound and <= upperBound?
	int fairs = 0;
	for(int i = 0; i < fairSquares.size(); ++i)
	{
		if ( (fairSquares[i] >= lowerBound) && (fairSquares[i] <= upperBound))
		{
			fairs += 1;
		}
	}

	std::cout << "Case #" << lineNum+1 << ": " << fairs << std::endl;
}

int main()
{
	int numLines = 0;
	std::cin >> numLines;

	// Pre-compute a cache used for each line
	std::vector<int64_t> fairSquares;
	
	// Find all numbers that are squares from LOWER_BOUND to UPPER_BOUND
	int64_t i = 0;
	while(++i)
	{
		int64_t square = i*i;

		// We're done with the search!
		if (square > UPPER_BOUND)
		{
			break;
		}

		if ((square >= LOWER_BOUND) && (square <= UPPER_BOUND))
		{
			if(checkFair(i))
			{
				if (checkFair(square))
				{
					fairSquares.push_back(square);

					// std::cout << "Cached square: " << square << std::endl;
				}
			}
		}
	} 
	

	for(int i = 0; i < numLines; ++i) {
		processLine(i, fairSquares);	
	}

	return 0;
}
