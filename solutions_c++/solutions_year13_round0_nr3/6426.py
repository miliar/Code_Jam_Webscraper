#include <iostream>
#include <vector>
#include <cstdlib>
#include <cmath>

using namespace std;

bool isPalindrome(unsigned long long k);

int main()
{
	unsigned long long start, stop;
	unsigned long long rstart, rstop;
	unsigned int cases;
	
	cin >> cases;
	
	// For each case,
	for (unsigned int Case = 1; Case <= cases; ++Case)
	{
		// Reset the counter
		unsigned long long count = 0;
		
		// Read the start and stop region of searching
		cin >> rstart >> rstop;
		
		start = (unsigned long long) sqrt(rstart);
		stop = (unsigned long long) sqrt(rstop) + 1;
		
		// Find the fair and square palindrome
		for (unsigned long long i=start; i<=stop; i++)
		{
			if (isPalindrome(i))
			{
				unsigned long long square = i * i;
				
				// Re-bounding
				if (square < rstart)
					continue;
				if (square > rstop)
					continue;
				
				// Square Palindrome
				if (isPalindrome(square))
				{
					count++;
					#ifdef DEBUG
					cout << i << " -> " << square << "\n";
					#endif
				}
			}
		}
		
		// Display the result;
		cout << "Case #" << Case << ": " << count << "\n";
	}
	
	exit(EXIT_SUCCESS);
}

bool isPalindrome(unsigned long long k)
{
	unsigned long long reversed = 0, n = k;
	
	while (n > 0)
	{
		reversed = reversed * 10 + n % 10;
		n /= 10;
	}

	return k == reversed;
}
