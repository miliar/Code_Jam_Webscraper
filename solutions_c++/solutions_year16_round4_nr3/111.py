#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <string>

#include <valarray>
#include <complex>
#include <functional>

using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif
#define pair akek

const int N = 100;
int R, C;
int pair[N];

void read()
{
	scanf("%d%d", &R, &C);
	for (int i = 0; i < (R + C); i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		a--, b--;
		pair[a] = b;
		pair[b] = a;
	}
}

vector <int> g[N];

int cellId[N][N][4];
int mv = 0;

int getLeft(int x, int y)
{
	return cellId[x][y][0];
}

int getRight(int x, int y)
{
	return cellId[x][y][2];
}

int getUp(int x, int y)
{
	return cellId[x][y][1];
}

int getDown(int x, int y)
{
	return cellId[x][y][3];
}

char table[N][N];

void addEdge(int a, int b)
{
	g[a].push_back(b);
	g[b].push_back(a);
}

int border(int v)
{
	if (v < C)
		return getUp(0, v);
	if (v < R + C)
		return getRight(v - C, C - 1);
	if (v < R + 2 * C)
		return getDown(R - 1, C - (v - R - C) - 1);
	return getLeft(R - (v - R - C - C) - 1, 0);
}

void cell(int x, int y, int t)
{
	if (t == 0)
	{
		table[x][y] = '\\';
		addEdge(getLeft(x, y), getDown(x, y));	
		addEdge(getRight(x, y), getUp(x, y));	
	}
	else
	{
		table[x][y] = '/';
		addEdge(getLeft(x, y), getUp(x, y));
		addEdge(getRight(x, y), getDown(x, y));
	}
}

int color[N];
int cc;

void dfs(int v, int c)
{
	color[v] = c;
	for (int to : g[v])
	{
		if (color[to] == 0)
			dfs(to, c);
	}
}

void solve()
{
	mv = 0;
	for (int i = 0; i < R; i++)
		for (int s = 0; s < C; s++)
		{
			for (int t = 0; t < 4; t++)
				cellId[i][s][t] = mv++;
		}

	for (int i = 0; i < (1 << (R * C)); i++)
	{
		for (int v = 0; v < mv; v++)
			g[v].clear();

		for (int a = 0; a < R; a++)
		{
			for (int b = 0; b < C; b++)
			{
				int pos = (a * C + b);
				cell(a, b, (i >> (pos) & 1));
			}
		}
		for (int a = 0; a < R; a++)
		{
			for (int b = 0; b < C; b++)
			{
				if (a < R - 1)
					addEdge(getDown(a, b), getUp(a + 1, b));
				if (b < C - 1)
					addEdge(getRight(a, b), getLeft(a, b + 1));
			}
		}
		cc = 1;
		fill(color, color + mv, 0);
		for (int v = 0; v < mv; v++)
		{
			if (color[v] == 0)
				dfs(v, cc++);
		}
		bool ok = true;
		for (int a = 0; a < 2 * (R + C); a++)
		{
			if (pair[a] < a)
				continue;
			int b = pair[a];
			if (color[border(a)] != color[border(b)])
				ok = false;
		}
		if (ok)
		{
			for (int a = 0; a < R; a++)
			{
				for (int b = 0; b < C; b++)
				{
					putchar(table[a][b]);
				}
				puts("");
			}
			return;
		}
	}
	puts("IMPOSSIBLE");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d:\n", i + 1);
		read();
		solve();
	}
	return 0;
}
