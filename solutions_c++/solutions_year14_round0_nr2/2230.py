#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#define clr(a) memset(a, 0, sizeof(a))

typedef std::pair<int, int> pii;
typedef long long ll;

void dbg(const char * fmt, ...)
{
	#if 1
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
		fflush(stdout);
	#endif
}

const double eps = 1e-13;

void solve(int test_case)
{
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double ans = x / 2;
	double farms = 0;
	double farm_time = 0;
	while(true)
	{
		farm_time += c / (2 + farms * f);
		farms++;
		if (farm_time + x / (2 + farms * f) - ans < -eps)
			ans = farm_time + x / (2 + farms * f);
		else
			break;
	}
	printf("Case #%d: %.10lf\n", test_case, ans);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		solve(i + 1);


	return 0;
}
