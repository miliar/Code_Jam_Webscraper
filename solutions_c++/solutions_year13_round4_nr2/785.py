#include <cstdio>

#define SMALL
//#define LARGE

using namespace std;

long long two[55];

void init() {
	two[0] = 1;
	for (int i = 1; i <= 50; ++i)
		two[i] = two[i - 1] << 1;
}

int main()
{
#ifdef SMALL
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	init();
	int T, n;
	long long p;
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++Case) {
		int ans[55];
		scanf("%d %lld", &n, &p);
		long long nn = two[n];
		for (int i = 0; i < n; ++i) {
			if (two[n - i - 1] >= p)
				ans[i] = 1;
			else
				ans[i] = 0, p -= two[n - i - 1];
		}
/*		for (int i = 0; i < n; ++i)
			printf("%d", ans[i]);
		printf("\n");*/
		int tot = 0;
		int i;
		for (i = 0; i < n; ++i) {
			if (ans[i] == 0)
				break;
			tot++;
		}
		while (i < n) {
			if (ans[i] == 1) {
				tot++;
				break;
			}
			++i;
		}
		int ans2 = nn- two[tot];
		for (i = 0; i < n; ++i)
			if (ans[i] == 1)
				break;
		int ans1 = two[i + 1] - 2;
		if (ans1 >= nn)
			ans1 = two[n] - 1;
		printf("Case #%d: %d %d\n", Case, ans1, ans2);
	}
	return 0;
}
