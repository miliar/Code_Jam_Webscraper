#pragma comment(linker, "/STACK:255000000")
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <stack>
#include <memory.h>
#include <algorithm>
#include <math.h>
#include <valarray>
#include <complex>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef complex<double> comp;

long double eps = 1e-7;
const int BASE = (int) 1e9;
const long double PI = 3.1415926535897932384626433832795;
const int MOD = (int) 1e9 + 7;
const int HMOD = (1 << 18) - 1;
const int N = 4000000;
const int INF = 1 << 30;
const LL LLINF = 1ll << 60;

int t, n, m, c;
int a[6][6];
bool used[6][6];

bool Bound(int y, int x)
{
	return y >= 0 && x >= 0 && y < n && x < m;
}

void Dfs(int y, int x)
{
	used[y][x] = true;
	for (int i = -1; i <= 1; i++)
		for (int j = -1; j <= 1; j++)
			if (i != 0 || j != 0)
			{
				int xto = x + j;
				int yto = y + i;
				if (Bound(yto, xto) && a[yto][xto])
					return;
			}
	for (int i = -1; i <= 1; i++)
		for (int j = -1; j <= 1; j++)
			if (i != 0 || j != 0)
			{
				int xto = x + j;
				int yto = y + i;
				if (Bound(yto, xto) && !used[yto][xto] && !a[yto][xto])
					Dfs(yto, xto);
			}
}

bool Check()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (!used[i][j] && !a[i][j])
				return false;
	return true;
}

bool flag = false;

void F(int i, int j, int curm)
{
	if (flag)
		return;
	if (curm < 0)
		return ;
	if (j == m)
	{
		F(i + 1, 0, curm);
		return;
	}
	if (i == n)
	{
		if (curm > 0)
			return ;
		for (int q = 0; q < n; q++)
			for (int w = 0; w < m; w++)
			{
				if (a[q][w])
					continue;
				memset(used, 0, sizeof(used));
				Dfs(q, w);
				if (Check())
				{
					flag = true;
					for (int i1 = 0; i1 < n; i1++)
					{
						for (int j1 = 0; j1 < m; j1++)
						{
							if (i1 == q && j1 == w)
								printf("c");
							else
								if (a[i1][j1])
									printf("*");
								else
									printf(".");
						}
						printf("\n");
					}
					return ;
				}
			}
	}
	a[i][j] = 0;
	if (i == n)
		return;
	F(i, j + 1, curm);
	if (curm > 0)
	{
		a[i][j] = 1;
		F(i, j + 1, curm - 1);
	}
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 0; k < t; k++)
	{
		scanf("%d%d%d", &n, &m, &c);
		printf("Case #%d:\n", k + 1);
		flag = 0;
		F(0, 0, c);
		if (!flag)
			printf("Impossible\n");
	}
	return 0;
}