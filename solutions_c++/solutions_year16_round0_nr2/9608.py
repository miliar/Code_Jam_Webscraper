#include <iostream>
using namespace std;

int main()
{
	int inputs = 0;
	double flips = 0;
	string pancakes = "";

	cin >> inputs;

	for(int i = 0; i < inputs; i++)
	{
		cin >> pancakes;

		flips = 0;

		for(int j = pancakes.size() - 1; j >= 0; j--)
		{
			// Could keep track of odd or even number of flips
			// to reduce string changes, or.... brute force it! :D
			if(pancakes[j] == '-')
			{
				flips++;
				for(int k = j; k >= 0; k--)
				{
					if(pancakes[k] == '-')
					{
						pancakes[k] = '+';
					}
					else
					{
						pancakes[k] = '-';
					}
				}
			}
		}

		cout << "Case #" << i+1 << ": " << flips << endl;
	}

	return 0;
}