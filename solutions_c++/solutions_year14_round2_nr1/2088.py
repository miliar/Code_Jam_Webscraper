#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;

int main ()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t, n, sum[100], ans, num[100][100];
	string list[100], base;
	cin >> t;

	for (int a, b, c, x = 0;x < t;x++)
	{
		cin >> n;
		for (int a = 0;a < n;a++)
			cin >> list[a];

		//Reduce the first string.
		base = "";
		base += list[0][0];
		for (a = 1;a < list[0].length ();a++)
			if (list[0][a] != list[0][a - 1])
				base += list[0][a];

		//Loop through all the strings and find sum for each base char.
		memset (sum, 0, 100 * sizeof (int));
		memset (num, 0, 100 * 100 * sizeof (int));
		for (a = 0;a < n;a++)
		{
			for (b = 0, c = 0;b < list[a].length () && c < base.length ();)
			{
				if (list[a][b] == base[c])
				{
					for (;b < list[a].length () && c < base.length () && list[a][b] == base[c];b++)
					{
						sum[c]++;
						num[a][c]++;
					}

					c++;
				}
				else
					break;
			}

			if (b != list[a].length () || c != base.length ())
				break;
		}

		//No answer.
		if (a != n)
		{
			cout << "Case #" << x + 1 << ": Fegla Won\n";
			continue;
		}

		//Find nearest multiple of n to seach sum.
		for (a = 0;a < base.length ();a++)
		{
			sum[a] = (double)sum[a] / n + 0.5;
		}

		//Add diff.
		ans = 0;

		for (a = 0;a < n;a++)
			for (b = 0;b < base.length ();b++)
				ans += abs (sum[b] - num[a][b]);

		cout << "Case #" << x + 1 << ": " << ans << "\n";
	}

	return 0;
}