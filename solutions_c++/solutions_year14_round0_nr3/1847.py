#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <queue>

using namespace std;

int n, m;
bool a[10][10];
int col[10][10];
bool ge[10][10];
int sx = 0, sy = 0;

void check(int x, int y)
{

	ge[x][y] = 1;
	int cn = 0;
	for (int z = -1; z <= 1; z++)
	{
		for (int t = -1; t <= 1; t++)
		{
			if (x + z >= 0 && x + z < n && y + t >= 0 && y + t < m && a[x + z][y + t])
				cn++;
		}
	}
	if (cn > 0)
		return;
	for (int z = -1; z <= 1; z++)
	{
		for (int t = -1; t <= 1; t++)
		{
			if (abs(z + t) > 0 && x + z >= 0 && x + z < n && y + t >= 0 && y + t < m && !ge[x + z][y + t] && !a[x + z][y + t])
				check(x + z, y + t);
		}
	}
}

bool getAns()
{
	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (!a[i][j])
			{
				cnt++;
				int cn = 0;
				for (int z = -1; z <= 1; z++)
				{
					for (int t = -1; t <= 1; t++)
					{
						if (abs(z + t) > 0 && i + z >= 0 && i + z < n && j + t >= 0 && j + t < m && a[i + z][j + t])
							cn++;
					}
				}
				sx = i, sy = j;
				if (cn > 0)
					continue;
				memset(ge, 0, sizeof(ge));
				check(i, j);
				bool fo = 0;
				for (int z = 0; z < n; z++) {
					for (int t = 0; t < m; t++) {
						if (!a[z][t] && !ge[z][t])
							fo = 1;
					}
				}
				if (!fo)
				{
					sx = i, sy = j;
					return 1;
				}
				else
					return 0;
			}
		}
	}
	return cnt <= 1;
}

bool rec(int cnt, int last)
{
	if (last == 0)
	{
		return getAns();
	}
	if (n * m - cnt > last)
	{
		a[cnt / m][cnt % m] = 0;
		if (rec(cnt + 1, last))
			return 1;
	}
	a[cnt / m][cnt % m] = 1;
	if (rec(cnt + 1, last - 1))
		return 1;
	a[cnt / m][cnt % m] = 0;
	return 0;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		int cn;
		scanf("%d%d%d", &n, &m, &cn);

		memset(a, 0, sizeof(a));
		if (rec(0, cn))
		{	
			printf("Case #%d:\n", tt + 1);
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (sx == i && sy == j)
						printf("c");
					else if (a[i][j])
						printf("*");
					else
						printf(".");
				}
				printf("\n");
			}
		}
		else
		{
			printf("Case #%d:\nImpossible\n", tt + 1);
		}
	}
	

	return 0;
}