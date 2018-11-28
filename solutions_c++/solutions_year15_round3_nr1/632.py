#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

int dp[200000];
bool good[200000];
const int INF = 1e9;
int r, c, w;

string toStr(int mask)
{
	string s = "";
	for (int i = 0; i < c; i++)
	{
		int b = mask % 3;
		mask /= 3;
		s = (char)(b + '0') + s;
	}
	return s;
}

int fromStr(string s)
{
	int mask = 0;
	for (int i = 0; i < c; i++)
	{
		int b = s[i] - '0';
		mask = mask * 3 + b;
	}
	return mask;
}

bool check(string s)
{
	for (int ship = 0; ship + w - 1 < c; ship++)
	{
		bool ok = true;
		for (int i = 0; i < c; i++)
		{
			if (i < ship || i > ship + w - 1)
			{
				if (s[i] == '2')
					ok = false;
			}
			else
			{
				if (s[i] == '1')
					ok = false;
			}
		}

		if (ok)
			return true;
	}
	return false;
}

bool foundShip(string s)
{
	int cnt = 0;
	for (int i = 0; i < c; i++)
		cnt += (s[i] == '2');
	return cnt == w;
}

void solve()
{
	cin >> r >> c >> w;

	int all = 1;
	for (int i = 0; i < c; i++)
		all *= 3;
	all--;

	for (int mask = all; mask >= 0; mask--)
	{
		dp[mask] = INF;
		string s = toStr(mask);
		good[mask] = check(s);
	}

	for (int mask = all; mask >= 0; mask--)
	{
		if (!good[mask])
			continue;
		string s = toStr(mask);
		if (foundShip(s))
		{
			dp[mask] = 0;
			continue;
		}

		int best = INF;
		for (int i = 0; i < c; i++)
		{
			if (s[i] != '0')
				continue;
			
			int cur = 0;
			s[i] = '1';
			if (good[fromStr(s)])
				cur = max(cur, dp[fromStr(s)]);
			s[i] = '2';
			if (good[fromStr(s)])
				cur = max(cur, dp[fromStr(s)]);
			best = min(best, cur);
			s[i] = '0';
		}

		dp[mask] = best + 1;
	}

	printf("%d", dp[0]);
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
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
}