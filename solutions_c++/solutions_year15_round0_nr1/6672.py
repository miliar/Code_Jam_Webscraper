#include <iostream>

using namespace std;

int main()
{
	int T;

	// Read number of test cases
	cin >> T;


	for (int i = 0; i < T; i++)
	{
		// Read max level of shyness
		int Smax;
		cin >> Smax;

		int people[1001];
		char ch;

		// Read number of people of each level from 0 to Smax
		for (int j = 0; j < Smax + 1; j++)
		{
			cin >> ch;
			people[j] = ch - 48;
		}

		int standing = 0;
		int extra = 0;

		for (int j = 0; j < Smax + 1; j++)
		{
			if (people[j] != 0)
			{
				if (j - standing > 0)
				{
					extra += j - standing;
					standing += extra + people[j];
				}
				else
					standing += people[j];
			}
		}

		cout << "Case #" << i + 1 << ": " << extra << endl;
	}

	return 0;
}