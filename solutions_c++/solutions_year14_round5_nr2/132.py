#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

ll h[104];
ll g[104];

ll dp[103][100500];
ll balance[104];

const ll infty = 1LL << 60;


void solve(int test_case)
{
	int p, q, n;
	scanf("%d%d%d", &p, &q, &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%lld%lld", &h[i], &g[i]);
		for(int m = 1; ; m++)
		{
			ll ts = (h[i] - p*(m-1)-1) / q;
			//dbg("%d %d -> %d %lld\n", i, m, ts, ts * q + p - h[i]);
			if (ts * q + p*m >= h[i])
			{
				if(ts < 0)
					throw 42;
				balance[i] = m - ts;
				//dbg("%d %lld \n", i, balance[i]);
				break;
			}
		}
	}
	for(int i = 0; i <= n; i++)
		for(int j = 0; j < 100500; j++)
			dp[i][j] = -infty;
	dp[0][1] = 0;
	int max = 1;
	for(int i = 0; i < n; i++)
		for(int j = max; j >= 0; j--)
		{
			if (j >= balance[i])
			{
				dp[i+1][j-balance[i]] = std::max(dp[i+1][j-balance[i]], dp[i][j] + g[i]);
				max = std::max(max, j - (int) balance[i]);
			}
			ll ttc = (h[i]-1) / q + 1;
			dp[i+1][j+ttc] = std::max(dp[i+1][j+ttc], dp[i][j]);
			max = std::max(max, j + (int) ttc);
			if (max > 100500)
				throw 42;
		}
	ll ans = 0;
	for(int j = 0; j <= max; j++)
		ans = std::max(ans, dp[n][j]);
	printf("Case #%d: ", test_case);
	printf("%lld\n", ans);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
