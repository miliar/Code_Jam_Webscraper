#include <iostream>
#include <vector>
#include <algorithm>
#include <assert.h>

void processLine(int lineNum)
{
	const int SHYNESS_LIMIT = 1000;

	int maxShyness = 0;
	std::cin >> maxShyness;

	std::string shynessValuesStr;
	std::cin >> shynessValuesStr;
	const int numShynessValues = shynessValuesStr.size();

	assert(maxShyness >= 0);
	assert(maxShyness <= SHYNESS_LIMIT);


	std::vector<int> shynessValues(numShynessValues, 0);	// reserve and set to 0
	for(int i = 0; i < numShynessValues; ++i)
	{
		shynessValues[i] = shynessValuesStr[i] - '0';		// convert from string to int
	}

	/* Debug print
	std::cout << "Debug print of shynessValues" << std::endl;
	for(int i = 0; i < numShynessValues; ++i)
	{
		std::cout << shynessValues[i] << ' ';
	}
	std::cout << std::endl;
	Debug print */

	int totalRequired = 0;	// Friends required to attend and stand
	int totalStanding = 0;	// Running sum of audience members standing including totalRequired

	for(int i = 0; i < numShynessValues; ++i)
	{
		// Blocked because we need more people to stand
		if ((shynessValues[i] > 0) && (totalStanding < i))
		{
			const int requiredToPushThem = i - totalStanding;
			totalRequired += requiredToPushThem;
			totalStanding += requiredToPushThem;
		}

		// Now they'll stand
		totalStanding += shynessValues[i];
	}

	// output	
	std::cout << "Case #" << lineNum+1 << ": " << totalRequired;
	std::cout << std::endl;
}

int main()
{
	int numLines = 0;
	std::cin >> numLines;

	for(int i = 0; i < numLines; ++i) 
	{
		processLine(i);	
	}

	return 0;
}
