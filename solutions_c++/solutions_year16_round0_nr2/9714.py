#include <iostream>
#include <string>
using namespace std;

void SwapUpToIndexInclusive(const int& index, string& pancakes)
{
	for (int i = 0; i <= index; i++)
	{
		if (pancakes[i] == '-')
			pancakes[i] = '+';
		else
			pancakes[i] = '-';
	}

}

int main()
{
	int T, timesFlipped = 0, minuses;
	string pancakes;
	bool areSorted = false;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> pancakes;
		int n = pancakes.length();

		timesFlipped = 0;
		areSorted = false;
		//First pass see if there's more pluses or minuses

		minuses = 0;
		for (int j = 0; j < n; j++)
		{
			if (pancakes[j] == '-')
			{
				minuses++;
			}
		}
		//If more minuses than pluses, flip all
		/*if (minuses > (n / 2))
		{
			SwapUpToIndexInclusive(n - 1, pancakes);
			timesFlipped++;
		}
		else if (minuses == n)
		{
			SwapUpToIndexInclusive(n - 1, pancakes);
			timesFlipped++;
			areSorted = true;
		}
		else if (minuses == 0)
		{
			areSorted = true;
		}*/
		//Now go through pancakes one by one
		while (!areSorted)
		{
			for (int k = 0; k < n; k++)
			{
				if (pancakes[k] == '-' &&  pancakes[k + 1] == '+')
				{
					//TODO swap all up to k (inclusive) -- turn minuses up until now to pluses
					SwapUpToIndexInclusive(k, pancakes);
					timesFlipped++;
					break;
				}
				else if (pancakes[k] == '+' && pancakes[k + 1] == '-')
				{
					//TODO swap all up to k (inclusive) -- turn pluses to minuses
					SwapUpToIndexInclusive(k, pancakes);
					timesFlipped++;
					break;
				}
			}
			minuses = 0;
			for (int j = 0; j < n; j++)
			{
				if (pancakes[j] == '-')
				{
					minuses++;
				}
			}
			if (minuses == n)
			{
				SwapUpToIndexInclusive(n - 1, pancakes);
				timesFlipped++;
			}
			//Each time check if sorted
			areSorted = true;
			for (int j = 0; j < n; j++)
			{
				if (pancakes[j] == '-')
				{
					areSorted = false;
					break;
				}
			}
			
		}
		cout << "Case #" << i + 1 << ": " << timesFlipped << endl;
	}
	// -- + -
	//++-+

	return 0;
}
