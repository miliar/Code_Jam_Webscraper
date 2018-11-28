#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


char g[101][101];
int a[101][101][4];

void solve(int n, int m, int test)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			a[i][j][0] = 0;
			a[i][j][1] = 0;
			a[i][j][2] = 0;
			a[i][j][3] = 0;
		}
	}
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (g[i][j] != '.')
			{
				a[i][j][3]++;
				break;
			}
		}

		for (int j = m - 1; j >= 0; j--)
		{
			if (g[i][j] != '.')
			{
				a[i][j][1]++;
				break;
			}
		}

	}


	for (int j = 0; j < m; j++)
	{
		for (int i = 0; i < n; i++)
		{
			if (g[i][j] != '.')
			{
				a[i][j][0]++;
				break;
			}
		}

		for (int i = n - 1; i >= 0; i--)
		{
			if (g[i][j] != '.')
			{
				a[i][j][2]++;
				break;
			}
		}
	}

	bool possible = true;
	int count = 0;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			int sum = a[i][j][0] + a[i][j][1] + a[i][j][2] + a[i][j][3];

			if (sum == 4)
			{
				possible = false;
			}

			int x = 0;

			if (a[i][j][0] == 1 && g[i][j] == '^')
			{
				x = 1;
			}

			if (a[i][j][1] == 1 && g[i][j] == '>')
			{
				x = 1;
			}

			if (a[i][j][2] == 1 && g[i][j] == 'v')
			{
				x = 1;
			}

			if (a[i][j][3] == 1 && g[i][j] == '<')
			{
				x = 1;
			}
			
			count += x;
		}
	}

	if (possible)
	{
		printf("Case #%d: %d\n", test, count);
	}
	else
	{
		printf("Case #%d: IMPOSSIBLE\n", test);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int TC;
	cin >> TC;

	for (int test = 1; test <= TC; test++)
	{
		int n, m;

		scanf("%d %d\n", &n, &m);

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%c", &g[i][j]);
			}
			scanf("\n");
		}

		solve(n, m, test);
	}

	return 0;
}