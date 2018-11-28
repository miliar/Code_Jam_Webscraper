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

const int size = 100500;
int ar[size];

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n, x;
	scanf("%d%d", &n, &x);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &ar[i]);
	}
	std::sort(ar, ar+n);
	int ans = 0;
	int l = 0, r = n - 1;
	while (l <= r)
	{
		if (l == r)
		{
			ans++;
			break;
		}
		if (ar[l] + ar[r] <= x)
		{
			l++; r--;
			ans++;			
		}
		else
		{
			ans++;
			r--;
		}
	}
	printf("%d\n", ans);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
