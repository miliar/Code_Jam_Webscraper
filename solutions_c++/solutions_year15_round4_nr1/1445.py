#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <stack>

using namespace std;

int a[200][200];
bool used[200][200];

pair <int, int> c[5] = { { 0, 0 }, { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int pp = 1; pp <= t; pp++)
	{
		int n, m;
		cin >> n >> m;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				char c;
				cin >> c;
				if (c == '.')
				{
					a[i][j] = 0;
				}
				if (c == '^')
				{
					a[i][j] = 1;
				}
				
				if (c == '>')
				{
					a[i][j] = 2;
				}

				if (c == 'v')
				{
					a[i][j] = 3;
				}
				if (c == '<')
				{
					a[i][j] = 4;
				}
			}
		}
		bool f = true;
		int ans = 0;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] == 0)
				{
					continue;
				}
				int cnt = 0;
				int dir = a[i][j];
				int curx = i;
				int cury = j;
				while (curx >= 0 && curx <= n && cury >= 0 && cury <= m)
				{
					if (a[curx][cury])
					cnt++;
					curx += c[dir].first;
					cury += c[dir].second;
				}
				if (cnt > 1)
				{
					continue;
				}
				cnt = -2;
				for (int ti = 1; ti <= n; ti++)
				{
					if (a[ti][j])
					{
						cnt++;
					}
				}
				for (int tj = 1; tj <= m; tj++)
				{
					if (a[i][tj])
					{
						cnt++;
					}
				}
				if (cnt == 0)
				{
					f = false;
					break;
				}
				else
				{
					ans++;
				}
			}
			if (!f)
			{
				break;
			}
		}
		cout << "Case #" << pp << ": ";
		if (f)
		{
			cout << ans << "\n";
		}
		else
		{
			cout << "IMPOSSIBLE" << "\n";
		}
	}



	return 0;
}