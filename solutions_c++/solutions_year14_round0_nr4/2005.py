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

double a[1000];
double b[1000];

void solve(int test_case)
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		scanf("%lf", &a[i]);
	for(int i = 0; i < n; i++)
		scanf("%lf", &b[i]);
	std::sort(a, a+n);
	std::sort(b, b+n);
	int cnt1 = n;
	for(int i = 0, j = 0; i < n; i++)
	{
		while(j < n && b[j] < a[i])
			j++;
		if (j < n)
		{
			cnt1 --;
			j++;
		}
	}
	int cnt2 = 0;
	for(int i = 0, j = 0; i < n; i++)
	{
		while(j < n && a[j] < b[i])
			j++;
		if (j < n)
		{
			cnt2 ++;
			j++;
		}
	}

	printf("Case #%d: %d %d\n", test_case, cnt2, cnt1);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		solve(i + 1);


	return 0;
}
