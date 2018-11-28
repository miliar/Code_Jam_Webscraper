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

const int N = 26;
char f[N][N];
int g[N][N], ng[N][N];
int p[N];
bool dp[N][16];

void solve()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", f[i] );
		for (int j = 0; j < n; j++)
			g[i][j] = f[i][j] - '0';
	}
	int ans = n * n;
	for (int mask = 0; mask < (1 << (n * n) ); mask++)
	{
		int _mask = mask;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				ng[i][j] = _mask & 1;
				_mask >>= 1;
			}
		int cnt = 0;
		bool good = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (g[i][j] && !ng[i][j] )
					good = false;
				else if (!g[i][j] && ng[i][j] )
					cnt++;
		if (!good) continue;

		for (int i = 0; i < n; i++)
			p[i] = i;

		bool fail = false;
		do
		{
			memset(dp, 0, sizeof dp);
			dp[0][0] = true;
			for (int i = 0; i < n; i++)
			{
				int cur = p[i];
				for (int x = 0; x < (1 << n); x++)
				{
					if (!dp[i][x] ) continue;
					bool fnd = false;
					for (int j = 0; j < n; j++)
						if (ng[cur][j] && (x & (1 << j) ) == 0)
						{
							fnd = true;
							dp[i + 1][x | (1 << j) ] = true;
						}
					if (!fnd)
					{
						fail = true;
						break;
					}
				}
				if (fail)
					break;
			}
			if (fail)
				break;
		}
		while (next_permutation(p, p + n) );
		if (fail) continue;
	//	if (cnt == 0)
	//		eprintf("mask = %d\n", mask);
		ans = min(ans, cnt);
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


