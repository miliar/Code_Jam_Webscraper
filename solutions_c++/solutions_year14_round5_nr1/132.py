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


const int size = 1000500;
ll ar[size];

ll bs(int n)
{
	int l = 0, r = n;
	while(l < r-1)
	{
		int m = (l + r) / 2;
		if (2*ar[m] >= ar[n])
			r = m;
		else
			l = m;
	}
	return std::min(std::max(ar[r], ar[n] - ar[r]), std::max(ar[l], ar[n] - ar[l]));
}

void solve(int test_case)
{
	int n;
	ll p, q, r, s;
	scanf("%d%lld%lld%lld%lld", &n, &p, &q, &r, &s);
	for(int i = 0; i < n; i++)
		ar[i] = (i * p + q) % r + s;
	for(int i = 1; i < n; i++)
		ar[i] += ar[i-1];
	ll ans = ar[n-1];
	for(int i = 0; i < n; i++)
		ans = std::min(ans, std::max(ar[n-1] - ar[i], bs(i)));

	printf("Case #%d: %.10lf\n", test_case, 1 - (double)ans / (double)ar[n-1]);

}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
