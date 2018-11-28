#include <cstdio>

//#define SMALL
#define LARGE

int t, n;

int main()
{
#ifdef SMALL
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		scanf("%d", &n);
		printf("Case #%d: ", Case);
		if (n == 0)
			printf("INSOMNIA\n");
		else {
			int show = 0, ans;
			for (int i = 1; show != ((1 << 10) - 1); ++i) {
				ans = i * n;
				for (int temp = ans; temp; temp /= 10)
					show |= (1 << (temp % 10));
			}
			printf("%d\n", ans);
		}
	}
	return 0;
}
