#include <cstdio>
#include <algorithm>
int a[10000];
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		int n, c; scanf("%d%d", &n, &c);
		for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		std::sort(a, a + n);
		int i = 0, j = n-1, ans = 0;
		while (i < j) {
			if (a[i] + a[j] <= c) i++, j--;
			else j--;
			ans++;
		}
		if (i == j) ans++;
		printf("%d\n", ans);
	}
	return 0;
}
