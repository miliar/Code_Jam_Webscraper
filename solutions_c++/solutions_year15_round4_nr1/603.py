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

string s[200];
int sumx[200], sumy[200];

void solve()
{
	int r, c;
	cin >> r >> c;
	for (int i = 0; i < r; i++)
		cin >> s[i];

	for (int i = 0; i < r; i++)
		sumx[i] = 0;
	for (int j = 0; j < c; j++)
		sumy[j] = 0;

	int ans = 0;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			if (s[i][j] == '.')
				continue;
			sumx[i]++; sumy[j]++;

			int di = 0, dj = 0;
			if (s[i][j] == '>')
				dj = 1;
			if (s[i][j] == '<')
				dj = -1;
			if (s[i][j] == 'v')
				di = 1;
			if (s[i][j] == '^')
				di = -1;

			int a = i + di, b = j + dj;
			while (0 <= a && a < r && 0 <= b && b < c && s[a][b] == '.')
			{
				a += di;
				b += dj;
			}

			if (0 > a || a >= r || 0 > b || b >= c)
				ans++;
		}

	bool bad = false;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (sumx[i] == 1 && sumy[j] == 1 && s[i][j] != '.')
				bad = true;

	if (bad)
	{
		cout << "IMPOSSIBLE";
		return;
	}

	cout << ans;
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