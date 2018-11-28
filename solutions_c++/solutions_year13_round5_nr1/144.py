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

ll ar[37];
ll b;


double profit(int i, ll m)
{
	ll sum = 0;
	for(int j = 0; j < i; j++)
	{
		sum += m - ar[j];
	}
	ll set = sum;
	for(int j = i; j < 37; j++)
		if (ar[j] <= m)
			sum += m - ar[j] + 1;
	if (sum > b)
		return -1000;
	return (double) set * (36.0 / i) - (double) sum;
}

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	clr(ar);
	 int n;
	scanf("%lld%d", &b, &n);
	for(int i = 0; i < n; i++)
		scanf("%lld", &ar[i]);
	std::sort(ar, ar+37);
	double ans = 0;
	for(int i = 1; i <= 36; i++)
	{
		ll l = ar[i-1];
		ll r = 10000000000000LL;
		while(l < r)
		{
			ll m = (l + r + 1) / 2;
			if (profit(i, m) > -100)
				l = m;
			else
				r = m - 1;
		}
		ans = std::max(ans, profit(i, l));
		ans = std::max(ans, profit(i, ar[i-1]));
		ans = std::max(ans, profit(i, ar[i]));
		//ll set = 0;
		//for(int j = 0; j < i; j++)
			//set += l - ar[j];
		//ll sum = set;
		//for(int j = i; j < 37; j++)
			//if (ar[j] <= l)
				//sum += l - ar[j] + 1;

		////dbg("%d %lld %lld %.10lf\n", i, l, set, (double) set * (36.0 / i) - (double) sum);
		//ans = std::max(ans, (double) set * (36.0 / i) - (double) sum);
	}
	printf("%.10lf\n", ans);
}

int main()
{
	int n;
	//freopen("sample.in", "r", stdin);
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
