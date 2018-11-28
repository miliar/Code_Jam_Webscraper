#include <stdio.h>

long long n, a[15];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%lld", &n);

	long long v, w, c;
	for (int i = 1; i <= n; i++) {
		scanf("%lld", &v);
		for (int j = 0; j <= 9; j++) {
			a[j] = 0;
		}
		for (long long j = 1; j <= 1000000; j++) {
			w = v * j;
			for (;w > 0;) {
				a[w % 10] = 1;
				w /= 10;
			}
			c = 0;
			for (int k = 0; k <= 9; k++) {
				c += a[k];
			}
			if (c == 10) {
				w = v*j;
				break;
			}
		}

		printf("Case #%d: ", i);

		if (w == 0) {
			printf("INSOMNIA\n");
		}
		else {
			printf("%lld\n", w);
		}
	}
	return 0;
}