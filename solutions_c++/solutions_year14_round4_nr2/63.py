#include <cstdio>
int a[1000];
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		int n; scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		if (n == 1) {
			puts("0");
			continue;
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int x = 0, y = 0;
			for (int j = 0; j < i; j++)
				if (a[i] < a[j]) x++;
			for (int j = i+1; j < n; j++)
				if (a[i] < a[j]) y++;
			ans += (x < y ? x : y);
		}
		printf("%d\n", ans);
	}
	return 0;
}
