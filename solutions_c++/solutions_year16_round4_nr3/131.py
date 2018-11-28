#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;

const int N = 20;
const int DX[] = {-1, 0, 1, 0};
const int DY[] = {0, 1, 0, -1};
int n, m;
int a[N][N];
int p[N * 10];

void read()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n + m; i++)
	{
		int x, y;
		scanf("%d%d", &x, &y);
		x--;y--;
		p[x] = y;
		p[y] = x;
	}
	return;
}

void fillTable(int mask)
{
	int k = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			a[i][j] = (mask >> k) & 1;
			k++;
		}
	return;
}

int getCoords(int id, int &x, int &y)
{
	if (id < m)
	{
		x = -1;
		y = id;
	}
	else if (id < m + n)
	{
		x = id - m;
		y = m;
	}
	else if (id < m + n + m)
	{
		x = n;
		y = 2 * m + n - 1 - id;
	}
	else if (id < m + n + m + n)
	{
		x = 2 * (m + n) - 1 - id;
		y = -1;
	}
	else throw;
}

bool checkCell(int x, int y)
{
	return x >= 0 && x < n && y >= 0 && y < m;
}

int changeDir(int dir, int t)
{
	if ((dir & 1) ^ t)
		dir--;
	else
		dir++;
	return (dir + 4) % 4;
}

void go(int x, int y, int dir, int &xx, int &yy)
{
	x += DX[dir];
	y += DY[dir];
	if (!checkCell(x, y))
	{
		xx = x;
		yy = y;
		return;
	}
	dir = changeDir(dir, a[x][y]);
	go(x, y, dir, xx, yy);
	return;
}

bool solve2()
{
	for (int i = 0; i < 2 * (n + m); i++)
	{
		int x, y;
		getCoords(i, x, y);
		int xx, yy;
		getCoords(p[i], xx, yy);
		int xxx, yyy;
		int dir = -1;
		if (i < m)
			dir = 2;
		else if (i < m + n)
			dir = 3;
		else if (i < m + n + m)
			dir = 0;
		else if (i < m + n + m + n)
			dir = 1;
		if (dir == -1) throw;
		go(x, y, dir, xxx, yyy);
		if (xx != xxx || yy != yyy) return false;
	}
	return true;
}

void printAns()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (a[i][j])
				printf("\\");
			else
				printf("/");
		}
		printf("\n");
	}
	return;
}

void solve()
{
	for (int mask = 0; mask < (1 << (n * m)); mask++)
	{
		fillTable(mask);
		if (solve2())
		{
			printAns();
			return;
		}
	}
	printf("IMPOSSIBLE\n");
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d:\n", i);
		read();
		solve();
	}

	return 0;
}