#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define in_str(b) scanf("%s",(b))
#define in_int1(a) scanf("%d",&(a))
#define in_int2(a,b) scanf("%d%d",&(a),&(b))
#define in_int3(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
#define in_int4(a,b,c,d) scanf("%d%d%d%d",&(a),&(b),&(c),&(d))
#define so(a) sort((a).begin(), (a).end())
#define rso(a) sort((a).rbegin(), (a).rend())
#define mp(a,b) make_pair(a,b)
#define mset(a,n) memset(a,n,sizeof(a))
#define readints(mas,n) for (int _i=0;_i<(n);_i++) in_int1((mas)[_i])
#define readdoubles(mas,n) for (int _i=0;_i<(n);_i++) scanf("%lf", &(mas)[_i])
#define unq(src) src.erase(unique((src).begin(), (src).end()), (src).end())
#define MOD 1000000007
typedef pair<int, int> pii;
typedef long long ll;
typedef pair<ll, ll> pll;

int mas[24][24];
int love[256];
int r, c;

int dfs(int y, int x, int d)
{
	if (y == 0 || x == 0 || y == r+1 || x == c+1) return mas[y][x];
	
	// from up
	if (d == 0)
	{
		if (mas[y][x] == 0) return dfs(y, x + 1, 3);
		else return dfs(y, x - 1, 1);
	}

	// from right
	if (d == 1)
	{
		if (mas[y][x] == 0) return dfs(y-1, x, 2);
		else return dfs(y+1, x, 0);
	}

	// from bottom
	if (d == 2)
	{
		if (mas[y][x] == 0) return dfs(y, x-1, 1);
		else return dfs(y, x+1, 3);
	}

	// from left
	if (mas[y][x] == 0) return dfs(y+1, x, 0);
	return dfs(y-1, x, 2);
}

int testMaze()
{
	int i;
	ll used = 0;

	// top
	for (i = 1; i <= c; i++)
	{
		if (!(used&(1ll<<mas[0][i])))
		{
			used |= 1ll << mas[0][i];
			int ret = dfs(1, i, 0);
			if (ret != love[mas[0][i]]) return 0;
		}
	}

	// bottom
	for (i = 1; i <= c; i++)
	{
		if (!(used&(1ll << mas[r+1][i])))
		{
			used |= 1ll << mas[r + 1][i];
			int ret = dfs(r, i, 2);
			if (ret != love[mas[r + 1][i]]) return 0;
		}
	}

	// right
	for (i = 1; i <= r; i++)
	{
		if (!(used&(1ll << mas[i][c+1])))
		{
			used |= 1ll << mas[i][c+1];
			int ret = dfs(i, c, 1);
			if (ret != love[mas[i][c+1]]) return 0;
		}
	}

	// left
	for (i = 1; i <= r; i++)
	{
		if (!(used&(1ll << mas[i][0])))
		{
			used |= 1ll << mas[i][0];
			int ret = dfs(i, 1, 3);
			if (ret != love[mas[i][0]]) return 0;
		}
	}

	return 1;
}

void printMaze()
{
	int i, j;
	for (i = 1; i <= r; i++)
	{
		for (j = 1; j <= c; j++) printf("%c", mas[i][j] ? '/' : '\\');
		printf("\n");
	}
}

void Solve()
{
	int i, j, k, m;

	int tests;
	in_int1(tests);
	for (int test = 1; test <= tests; test++)
	{
		in_int2(r, c);
		int n = 1;
		for (i = 1; i <= c; i++)mas[0][i] = n++;
		for (i = 1; i <= r; i++)mas[i][c + 1] = n++;
		for (i = c; i > 0; i--) mas[r + 1][i] = n++;
		for (i = r; i > 0; i--) mas[i][0] = n++;
		mset(love, 0);
		for (i = 0; i < n-1; i+=2)
		{
			int a, b;
			in_int2(a, b);
			love[a] = b;
			love[b] = a;
		}

		printf("Case #%d:\n", test);
		int h = r*c;
		// generate maze
		for (i = 0; i < 1 << h; i++)
		{
			k = 0;
			for (j = 1; j <= r; j++)
			{
				for (int o = 1; o <= c; o++)
				{
					if (i&(1 << k)) mas[j][o] = 0;
					else mas[j][o] = 1;
					k++;
				}
			}

			if (testMaze())
			{
				printMaze();
				break;
			}
		}
		if (i >= (1 << h)) printf("IMPOSSIBLE\n");
	}
}

int main()
{
#ifdef __LOCAL_RUN__
	FILE *res_output = freopen("output.txt", "wt", stdout);
	FILE *res_input = freopen("input.txt", "rt", stdin);
	Solve();
#else
	Solve();
#endif
	return 0;
}