#include <cstdio>

int T;
int a[1005];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		int N, k;
		scanf("%d", &N);
		int mx = 0;
		for (int i = 0; i < N; ++i) {
			scanf("%d", &a[i]);
			if (a[i] > mx) mx = a[i];
		}
		int ans = mx;
		for (int i = 1; i <= mx; ++i) {
			int tmp = 0;
			for (int j = 0; j < N; ++j) {
				tmp += a[j] / i - 1;
				if (a[j] % i) ++tmp;
			}
			if (tmp + i < ans) ans = tmp + i;
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}