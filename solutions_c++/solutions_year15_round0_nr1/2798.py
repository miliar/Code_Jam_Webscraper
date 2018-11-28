#include <stdio.h>

int a[9999];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int k = 1; k <= t; k++) {
		int x;
		char b[9999];
		scanf("%d %s", &x, b);

		for (int i = 0; i <= x; i++) {
			a[i] = b[i] - '0';
		}

		int sum = a[0], add = 0;
		for (int i = 1; i <= x; i++) {
			if (i > sum) {
				int tt = i - sum;
				add += tt;
				sum += tt;
			}
			sum += a[i];
		}

		printf("Case #%d: %d\n", k, add);
	}

	return 0;
}