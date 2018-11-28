#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int people[1010];

int main()
{
	int i, k, e, t, smax, fr, stand, inv;

	char c;

	cin >> t;

	for (e = 1; e <= t; ++e)
	{
		cin >> smax;

		for (i = 0; i <= smax; ++i)
		{
			cin >> c;
			people[i] = c - '0';
		}

		fr = 0;
		stand = people[0];
		
		i = 1;
		while (1)
		{
			while ((stand >= i || people[i] == 0) && i <= smax)
			{
				stand += people[i];
				++i;
			}

			if (i == smax + 1)
			{
				break;
			}

			fr += i - stand;
			stand += i - stand;

		}
		
		cout << "Case #" << e << ": " << fr << endl;
	}



	return 0;
}