#include <iostream>
#include <vector>
#include <string>
#include <cmath>

template <typename T>
void printCase(int caseNum, T result)
{
	std::cout << "Case #" << caseNum + 1 << ": " << result << std::endl;
}

int main()
{
	int testCases;
	std::cin >> testCases;

	std::vector<std::string> tests;
	for (int i = 0; i < testCases; i++)
	{
		std::string n;
		std::cin >> n;

		tests.push_back(n);
	}

	for (int i = 0; i < testCases; i++)
	{
		std::string test = tests[i];

		//

		int totalFlips = 0;
		while (true)
		{
			// Check if we need to continue flipping and find
			// the last sad pancake index
			int countNegative = 0;
			int lastNegativeIndex = 0;
			for (int i = 0; i < test.size(); i++)
			{
				if (test[i] == '-')
				{
					countNegative++;
					lastNegativeIndex =	i;
				}
			}

			// No more swaps to be done
			if (countNegative == 0)
				break;

			// We never want to saw when they differ, otherwise we'll
			// always end up with a - at the bottom of the stack
			while (test[lastNegativeIndex] != test[0])
				lastNegativeIndex--;

			for (int i = 0; i <= lastNegativeIndex / 2; i++)
			{
				// Swap
				char tmp = test[i];
				test[i] = test[lastNegativeIndex - i];
				test[lastNegativeIndex - i] = tmp;

				// Flip
				test[i] = test[i] == '+' ? '-' : '+';

				// We never ever want to flip the same element twice
				// to revert it back to its original value before this
				if (i != lastNegativeIndex - i)
					test[lastNegativeIndex - i] = test[lastNegativeIndex - i] == '+' ? '-' : '+';
			}

			totalFlips++;
		}

		//

		printCase(i, totalFlips);
	}
}