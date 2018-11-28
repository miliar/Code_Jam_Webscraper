#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm> 
#include <iostream> 
#include <string.h> 
#include <stdlib.h>
#include <limits.h>
#include <numeric>
#include <sstream> 
#include <fstream>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define INF 0x3F3F3F3F 
#define eps 1e-9
using namespace std;
typedef pair<int, int> pii;

#define N 109

char s[N][N];

int solve()
{
	int n, m, i, j;
	scanf("%d %d", &n, &m);
	for (i = 0; i < n; i++)
		scanf("%s", s[i]);
	int cnt = 0;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			if (s[i][j] != '.')
			{
				int dx = s[i][j] == '^' ? -1 : s[i][j] == 'v' ? 1 : 0;
				int dy = s[i][j] == '>' ? 1 : s[i][j] == '<' ? -1 : 0;
				int x = i + dx, y = j + dy;
				for (; x >= 0 && y >= 0 && x < n && y < m && s[x][y] == '.'; x += dx, y += dy)
				{
				}
				if (x < 0 || y < 0 || x >= n || y >= m)
					cnt++;
				bool possible = false;
				for (x = i + 1; x < n; x++)
					possible |= s[x][j] != '.';
				for (x = 0; x < i; x++)
					possible |= s[x][j] != '.';
				for (y = j + 1; y < m; y++)
					possible |= s[i][y] != '.';
				for (y = 0; y < j; y++)
					possible |= s[i][y] != '.';
				if (!possible)
					return -1;
			}
		}
	}
	//for (int mask = 0; mask < (1 << (n*m)); mask++)
	//{
	//	for (i = 0; i < n; i++)
	//	{
	//		for (j = 0; j < m; j++)
	//		{
	//			if (s[i][j] != '.')
	//			{
	//			}
	//		}
	//	}
	//}
	return cnt;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		int ans = solve();
		printf("Case #%d: ", test);
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
}

/*
1 
4 4 
.>>. 
^..v 
^..v 
.<<. 
*/