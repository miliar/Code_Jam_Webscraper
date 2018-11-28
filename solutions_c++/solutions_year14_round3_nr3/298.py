#include<iostream>
#include<cstring>
using namespace std;

int grid[20][20];
int n, m;

const int dx[4] = { -1, 1, 0, 0 };
const int dy[4] = { 0, 0, -1, 1 };

bool valid(int row, int col)
{
	return 0 <= row&&row < n && 0 <= col&&col < m;
}

void dfs(int row, int col)
{
	grid[row][col] = 2;
	for (int i = 0; i < 4; i++)
	{
		int nr = row + dx[i];
		int nc = col + dy[i];
		if (valid(nr, nc) && grid[nr][nc] != 1 && grid[nr][nc] != 2)
			dfs(nr, nc);
	}
}

int main()
{
	int t, kase = 0;
	cin >> t;
	while (t--)
	{
		int sum, k, best = 2147483647;
		cin >> n >> m >> k;
		sum = n * m;
		for (int i = 0; i < (1 << sum); i++)
		{
			memset(grid, 0, sizeof(grid));
			int stone = 0;
			for (int j = 0; j < sum;j++)
				if (i&(1 << j))
				{
					stone++;
					int r = j / m, c = j % m;
					grid[r][c] = 1;
				}
			for (int j = 0; j < n; j++)
			{
				if (grid[j][0] == 0)
					dfs(j, 0);
				if (grid[j][m - 1] == 0)
					dfs(j, m - 1);
			}
			for (int j = 0; j < m; j++)
			{
				if (grid[0][j] == 0)
					dfs(0, j);
				if (grid[n - 1][j] == 0)
					dfs(n - 1, j);
			}
			int cnt = 0;
			for (int j = 0; j < n; j++)
				for (int k = 0; k < m; k++)
					if (grid[j][k] == 2)
						cnt++;
			int rem = sum - cnt;
			if (rem >= k && stone < best)
				best = stone;
		}
		cout << "Case #" << ++kase << ": " << best << endl;
	}
	return 0;
}