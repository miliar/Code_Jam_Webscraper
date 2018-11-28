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

int a[100][100];
bool opened[100][100];
int cnt;
int n, m, bombs, zeros;

bool inside(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool isBomb(int x, int y)
{
	return inside(x, y) && a[x][y] == -1;
}

void dfs(int x, int y)
{
	opened[x][y] = 1;
	cnt++;

	if (a[x][y] != 0)
		return;
	for (int p = -1; p <= 1; p++)
		for (int q = -1; q <= 1; q++)
		{
			int xx = x + p, yy = y + q;
			if (inside(xx, yy) && !opened[xx][yy])
				dfs(xx, yy);
		}
}

bool check()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (a[i][j] != -1)
			{
				for (int p = -1; p <= 1; p++)
					for (int q = -1; q <= 1; q++)
						a[i][j] += isBomb(i + p, j + q);
			}

	for (int ii = 0; ii < n; ii++)
		for (int jj = 0; jj < m; jj++)
		{
			if (a[ii][jj] == -1)
				continue;

			cnt = 0;
			for (int i = 0; i < n; i++)
				for (int j = 0; j < m; j++)
					opened[i][j] = 0;

			dfs(ii, jj);
			if (cnt == zeros)
			{
				a[ii][jj] = 100;
				return 1;
			}
		}

	return 0;
}

bool good(int mask)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			if ((mask & 1))
				a[i][j] = -1;
			else
				a[i][j] = 0;
			mask >>= 1;
		}

	return check();
}

void Solution()
{

	cin >> n >> m >> bombs;
	zeros = n * m - bombs;

	int all = (1 << (n * m)) - 1;
	for (int mask = 0; mask <= all; mask++)
	{
		int x = mask, y = 0;
		while (x > 0)
		{
			y += (x & 1);
			x >>= 1;
		}
		if (y != bombs)
			continue;

		if (good(mask))
		{
			//return;
			for (int ii = 0; ii < n; ii++)
			{
				for (int jj = 0; jj < m; jj++)
					if (a[ii][jj] == 100)
						cout << "c";
					else if (a[ii][jj] == -1)
						cout << "*";
					else
						cout << ".";
					cout << endl;
			}
			return;
		}
	}

	cout << "Impossible\n";
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	double t0 = clock();

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		Solution();
		//printf("%d %d %d\n\n", n, m, bombs);
	}

	double t1 = clock();
	//printf("remain: %.2lf", (t1 - t0) / CLOCKS_PER_SEC);
}