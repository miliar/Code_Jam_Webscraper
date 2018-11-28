#include <stdio.h>
#include <string.h>
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int runs = 1;
	int T; for (scanf("%d", &T); T--; ) {
		printf("Case #%d:\n", runs++);
		int n, Q;
		scanf("%d%d", &n, &Q);
		for (int i = (1 << (n - 1)) + 1; Q && i < (1 << n); i += 2) {
			if (i == 35)
				i = i;
			long long x[11] = { 0, }, G[11] = { 0, }, r[11] = { 0, };
			for (int j = 2; j <= 10; j++) G[j] = 1;
			for (int j = 0; j < n; j++) {
				if ((1 << j)&i) {
					for (int k = 2; k <= 10; k++) x[k] += G[k];
				}
				for (int k = 2; k <= 10; k++) G[k] *= (long long)(k);
			}
			for (int k = 2; k <= 10; k++) {
				if (x[k] % 2 == 0) {
					r[k] = 2;
					continue;
				}
				for (int i = 3; (long long)(i)*(i) <= x[k]; i += 2) {
					if (x[k] % i == 0) {
						r[k] = i;
						break;
					}
				}
			}
			bool ok = 1;
			for (int k = 2; k <= 10; k++) {
				if (r[k] == 0) ok = 0;
			}
			if (ok) {
				Q--;
				for (int j = n - 1; j >= 0; j--) printf("%d", ((1 << j)&i) > 0);
				for (int j = 2; j <= 10; j++) printf(" %d", r[j]);
				puts("");
			}
		}
	}
	fcloseall();
	return 0;
}