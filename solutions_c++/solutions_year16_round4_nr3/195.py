#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <queue>
#include <deque>
#include <cctype>
#include <bitset>
#include <algorithm>

using namespace std;

int n, m;
int grid[10][10];
int vis[10][10][10];
int finaln, finalm;

void dfs(int i, int j, int k, int c)
{
	if (i == 0 || i == n + 1)
	{
		finaln = i;
		finalm = j;
		return;
	}
	if (j == 0 || j == m + 1)
	{
		finaln = i;
		finalm = j;
		return;
	}
	if (grid[i][j] == 0)
	{
		if (k == 0)
			dfs(i, j - 1, 1, c);
		else if (k == 1)
			dfs(i + 1, j, 0, c);
		else if (k == 2)
			dfs(i, j + 1, 3, c);
		else
			dfs(i - 1, j, 2, c);
	} else {
		if (k == 0)
			dfs(i, j + 1, 3, c);
		else if (k == 1)
			dfs(i - 1, j, 2, c);
		else if (k == 2)
			dfs(i, j - 1, 1, c);
		else
			dfs(i + 1, j, 0, c);
	}
}

int a[100];
int pos[100][2];
int sp[100][3];

int main()
{
	int Cases;
	cin >> Cases;
	for (int Case = 1; Case <= Cases; Case++)
	{
		memset(pos, 0, sizeof pos);
		memset(sp, 0, sizeof sp);
		memset(a, 0, sizeof a);
		cin >> n >> m;
		for (int i = 0; i < 2 * (n + m); i++)
			cin >> a[i];
		for (int i = 1; i <= m; i++)
		{
			pos[i][0] = 0; sp[i][0] = 1;
			pos[i][1] = i; sp[i][1] = i;
			sp[i][2] = 0;
		}
		for (int i = 1; i <= n; i++)
		{
			pos[i + m][0] = i; sp[i + m][0] = i;
			pos[i + m][1] = m + 1; sp[i + m][1] = m;
			sp[i + m][2] = 1;
		}
		for (int i = 1; i <= m; i++)
		{
			pos[i + m + n][0] = n + 1; sp[i + m + n][0] = n;
			pos[i + m + n][1] = m + 1 - i; sp[i + m + n][1] = m + 1 - i;
			sp[i + m + n][2] = 2;
		}
		for (int i = 1; i <= n; i++)
		{
			pos[i + m + m + n][0] = n + 1 - i; sp[i + m + m + n][0] = n + 1 - i;
			pos[i + m + m + n][1] = 0; sp[i + m + m + n][1] = 1;
			sp[i + m + m + n][2] = 3;
		}
		bool xxx = false;
		cout << "Case #" << Case << ": " << endl;
		for (int i = 0; i < (1 << (n * m)); i++)
		{
			memset(grid, 0, sizeof grid);
			memset(vis, 0, sizeof vis);
			int j = i;
			for (int x = 1; x <= n; x++)
				for (int y = 1; y <= m; y++)
				{
					grid[x][y] = j % 2;
					j /= 2;
				}
			bool succ = true;
			for (int j = 0; j <= 2 * (n + m); j += 2)
			{
				dfs(sp[a[j]][0], sp[a[j]][1], sp[a[j]][2], j);
				if (pos[a[j + 1]][0] != finaln || pos[a[j + 1]][1] != finalm)
					succ = false;
			}
			if (succ) {
				xxx = true;
				for (int x = 1; x <= n; x++)
				{
					for (int y = 1; y <= m; y++)
					{
						if (grid[x][y] == 0)
							cout << '/';
						else
							cout << '\\';
					}
					cout << endl;
				}
				break;
			}
		}
		if (!xxx)
			cout << "IMPOSSIBLE" << endl;
	}
}