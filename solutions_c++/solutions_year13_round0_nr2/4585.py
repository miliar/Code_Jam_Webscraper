#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

int g[105][105];
int f[105][105];
int a[105][105];
int n, m;

void tryUseRow (int ind)
{
	for (int i = 0; i < m; i++)
		if (f[ind][i] == 0)
			return ;

	for (int i = 0; i < m; i++)
		a[ind][i] = 1;
}

void tryUseCol (int ind)
{
	for (int i = 0; i < n; i++)
		if (f[i][ind] == 0)
			return ;

	for (int i = 0; i < n; i++)
		a[i][ind] = 1;
}

bool canDo (int h)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (g[i][j] > h)
				f[i][j] = 0;
			else
				f[i][j] = 1;
		}
	}
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			a[i][j] = 0;

	for (int i = 0; i < n; i++)
		tryUseRow(i);

	for (int i = 0; i < m; i++)
		tryUseCol(i);

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (f[i][j] == 1 && a[i][j] == 0)
				return false;
		}
	}

	return true;
}

void solve ()
{
	int hMin = 1000;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			hMin = min(hMin, g[i][j] );

	for (int i = 100; i >= hMin; i--)
	{
		if (!canDo(i) )
		{
			printf("NO");
			return ;
		}
	}

	printf("YES");
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0; t < test; t++)
	{
		if (t)
			printf("\n");

		printf("Case #%d: ", t + 1);

		// input

		scanf("%d%d\n", &n, &m);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%d", &g[i][j] );
			}
			scanf("\n");
		}

		// #input

		solve();
	}

	return 0;
}