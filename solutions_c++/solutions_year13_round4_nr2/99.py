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


ll get_best(ll x, ll n)
{
	if (x == 0)
		return 0;
	if (x == n - 1)
		return n - 1;
	return get_best((x + 1) / 2, n / 2);
}

ll get_worst(ll x, ll n)
{
	if (x == 0)
		return 0;
	if (x == n - 1)
		return n - 1;
	return n/2 + get_worst((x - 1) / 2, n / 2);
}


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n; ll p;
	scanf("%d%lld", &n, &p);
	ll l = 0, r = (1LL << n) - 1;
	while(l < r)
	{
		ll m = (l + r + 1) / 2;
		if (get_best(m, (1LL << n)) < p)
			l = m;
		else
			r = m - 1;
	}
	ll best = l;
	l = 0, r = (1LL << n) - 1;
	while(l < r)
	{
		ll m = (l + r + 1) / 2;
		if (get_worst(m, (1LL << n)) < p)
			l = m;
		else
			r = m - 1;
	}
	ll worst = l;
	printf("%lld %lld\n", worst, best);

}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
