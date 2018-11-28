#include <cstdio>

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int m;
		char c;
		scanf("%d ", &m);
		int all = 0;
		int ans = 0;
		for (int h = 0; h < m + 1; h++) {
			scanf("%c", &c);
			if (h > all) {
				ans += h - all;
				all = h;
			}
			all += c - '0';
		}
		printf("Case #%d: %d\n", i + 1, ans);
		scanf("\n");
	}
	return 0;
}