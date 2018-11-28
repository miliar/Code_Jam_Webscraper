#include <stdio.h>

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n;
		char s[1001];
		scanf("%d%s", &n, s);
		int r = 0, x = 0;
		for (int i = 0; i <= n; ++i) {
			if (x < i) {
				r += i -x;
				x = i;
			}
			x += s[i] - '0';
		}
		printf("Case #%d: %d\n", tt, r);
	}
}
