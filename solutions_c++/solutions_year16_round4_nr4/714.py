#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<time.h>
using namespace std;

string s[100];
int p[100];
int n;

bool check()
{
	sort(p, p + n);
	do
	{
		vector<int> can;
		can.push_back(0);

		for (int ii = 0; ii < n; ii++)
		{
			int i = p[ii];
			vector<int> can2;

			for (int mask : can)
			{
				bool found = false;
				for (int j = 0; j < n; j++)
					if (s[i][j] == '1' && (mask & (1 << j)) == 0)
					{
						found = true;
						can2.push_back(mask | (1 << j));
					}

				if (!found)
					return false;
			}

			can.swap(can2);
		}

	} while (next_permutation(p, p + n));

	return true;
}

int brute(int i, int j, int cost)
{
	if (j == n)
	{
		i++;
		j = 0;
	}
	if (i == n)
	{
		if (check())
			return cost;
		return 100;
	}

	if (s[i][j] == '1')
		return brute(i, j + 1, cost);

	int res = brute(i, j + 1, cost);

	s[i][j] = '1';
	res = min(res, brute(i, j + 1, cost + 1));
	s[i][j] = '0';
	return res;
}

void solve()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> s[i];

	for (int i = 0; i < n; i++)
		p[i] = i;

	cout << brute(0, 0, 0);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}