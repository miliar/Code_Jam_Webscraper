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


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n;
	scanf("%d", &n);
	std::vector<int> ar(n);
	for(int i = 0; i < n; i++)
		scanf("%d", &ar[i]);
	int ans = 0;
	for(int i = 0; i < n; i++)
	{
		int min = 0;
		for(int j = 0; j < (int) ar.size(); j++)
			if (ar[j] < ar[min])
				min = j;
		ans += std::min(min, (int) ar.size() - 1 - min);
		ar.erase(ar.begin() + min);
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
