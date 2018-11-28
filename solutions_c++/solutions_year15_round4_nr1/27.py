#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

const int maxn = 105;
char f[maxn][maxn];

int tl[maxn][maxn], tr[maxn][maxn], tu[maxn][maxn], td[maxn][maxn];


void solve()
{
	int r, c;
	scanf("%d%d", &r, &c);
	for (int i = 0; i < r; i++)
	{
		scanf("%s", f[i] );
	}

	for (int i = 0; i < r; i++)
	{
		int x = 0;
		for (int j = 0; j < c; j++)
		{
			tl[i][j] = x;
			if (f[i][j] != '.')
			{
				x = 1;
			}
		}
		x = 0;
		for (int j = c - 1; j >= 0; j--)
		{
			tr[i][j] = x;
			if (f[i][j] != '.')
			{
				x = 1;
			}
		}
	}
	for (int j = 0; j < c; j++)
	{
		int x = 0;
		for (int i = 0; i < r; i++)
		{
			tu[i][j] = x;
			if (f[i][j] != '.')
			{
				x = 1;
			}
		}
		x = 0;
		for (int i = r - 1; i >= 0; i--)
		{
			td[i][j] = x;
			if (f[i][j] != '.')
			{
				x = 1;
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			if (f[i][j] == '.')
				continue;
			if (tl[i][j] + tr[i][j] + td[i][j] + tu[i][j] == 0)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
			if (f[i][j] == '<' && !tl[i][j] )
				ans++;
			else if (f[i][j] == '>' && !tr[i][j] )
				ans++;
			else if (f[i][j] == 'v' && !td[i][j] )
				ans++;
			else if (f[i][j] == '^' && !tu[i][j] )
				ans++;
		}
	printf("%d\n", ans);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


