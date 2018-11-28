#include <cstdio>
#include <cassert>

#define SMALL
//#define LARGE

int t, n, j;
long long ans, LIMIT;

void out(const long long& x) {
	if (x == 0)
		return;
	out(x / 2);
	printf("%lld", x & 1);
}

long long change(const long long& x, const int& d) {
	long long temp = x, ret = 0, now = 1;
	while (temp) {
		ret += now * (temp % 2);
		temp /= 2, now *= d;
	}
	return ret;
}

bool check(const long long& x) {
	for (int i = 2; i <= 10; ++i) {
		long long temp = change(x, i);
		if (temp % (i + 1) != 0)
			return false;
	}
	return true;
}

int main()
{
#ifdef SMALL
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif

	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		scanf("%d %d", &n, &j);
		printf("Case #%d:\n", Case);
		ans = 1;
		for (int i = 1; i < n; ++i)
			ans *= 2;
		LIMIT = ans * 2;
		ans += 3 - ans % 3;
		while (j--) {
			if (!check(ans)) {
				ans += 6;
				++j;
				continue;
			}
			out(ans);
			for (int i = 2; i <= 10; ++i)
				printf(" %d", i + 1);
			printf("\n");
			assert(ans < LIMIT);
			ans += 6;
		}
	}
	return 0;
}
