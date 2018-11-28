#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int 	testcases;
	int 	topshyness;
	int 	people;
	int 	cumulative;
	int 	result;
	int 	mod;

	cin >> testcases;

	for (int t = 0; t < testcases; t++)
	{
		cumulative = 0;
		result = 0;

		cin >> topshyness;

		cin >> people;

		mod = pow(10.0, topshyness);

		for (int i = 0; i <= topshyness; i++)
		{
			int value = people / mod;

			if (cumulative >= i)
			{
				if (cumulative == i && value == 0)
				{
					cumulative++;
					result++;
				}
				else
					cumulative += value;
			}
			else
			{
				result++;
				cumulative++;
			}

			people -= value * mod;
			mod /= 10;
		}

		cout << "Case #" << t+1 << ": " << result << endl;
	}

	return 0;
}