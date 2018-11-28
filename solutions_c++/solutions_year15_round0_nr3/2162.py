#include <iostream>

#define NOPE cout << "Case #" << e << ": NO" << endl
#define YEP  cout << "Case #" << e << ": YES" << endl

using std::cin;
using std::cout;
using std::endl;

char str[10010];

char mult[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 1, 2, 3, 4 },
	{ 0, 2, 1, 4, 3 },
	{ 0, 3, 4, 1, 2 },
	{ 0, 4, 3, 2, 1 } };

bool change[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 0, 0 },
	{ 0, 0, 1, 0, 1 },
	{ 0, 0, 1, 1, 0 },
	{ 0, 0, 0, 1, 1 } };


int main()
{
	int t, e, len, j, jjj;

	long long i, iii, times;
	bool minus, first;

	int res;

	cin >> t;

	for (e = 1; e <= t; ++e)
	{
		cin >> len >> times;

		cin >> str;

		for (j = 0; j < len; ++j)
		{
			str[j] -= 'i' - 2;
		}

		minus = false;
		res = 1;

		// SEARCH I

		for (i = 0; i < times; ++i)
		{
			for (j = 0; j < len; ++j)
			{
				if (change[res][str[j]])
				{
					minus = !minus;
				}
				
				res = mult[res][str[j]];

				if (res == 2)
				{
					iii = i;
					jjj = j;
					
					i = times; // break
					j = len; // break
				}

			}
		}

		if (res != 2) // != i
		{
			NOPE;
			continue;
		}

		// search J

		res = 1;
		first = true;

		for (i = iii; i < times; ++i)
		{
			if (!first)
			{
				jjj = -1;
			}
			else
			{
				first = false;
			}

			for (j = jjj + 1; j < len; ++j)
			{
				if (change[res][str[j]])
				{
					minus = !minus;
				}

				res = mult[res][str[j]];

				if (res == 3)
				{
					iii = i;
					jjj = j;

					i = times; // break
					j = len; // break
				}
			}
		}

		if (res != 3)
		{
			NOPE;
			continue;
		}

		// search K

		first = true;
		res = 1;

		for (i = iii; i < times; ++i)
		{
			if (!first)
			{
				jjj = -1;
			}
			else
			{
				first = false;
			}

			for (j = jjj + 1; j < len; ++j)
			{
				if (change[res][str[j]])
				{
					minus = !minus;
				}

				res = mult[res][str[j]];
			}
		}

		if (res != 4 || minus == true)
		{
			NOPE;
			continue;
		}

		YEP;

	}

	return 0;
}