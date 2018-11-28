#include <stdio.h>

int a[9999];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int k = 1; k <= t; k++) {
		int x, m = 0;
		scanf("%d", &x);
		for (int i = 1; i <= x; i++) {
			scanf("%d", &a[i]);
			if (m < a[i]) {
				m = a[i];
			}
		}

		int min = m;
		for (int w = 1; w <= m; w++) {
			int cnt = 0;
			for (int i = 1; i <= x; i++) {
				if (a[i] > w) {
					int q = a[i] / w - 1;
					if (a[i] % w) { q++; }
					cnt += q;
				}
			}
			if (cnt + w < min) {
				min = cnt + w;
			}
		}

		printf("Case #%d: %d\n", k, min);
	}

	return 0;
}