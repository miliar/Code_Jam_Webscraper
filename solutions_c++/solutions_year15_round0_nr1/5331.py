#include <stdio.h>

int t, n, data[1010];

int main() {
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		int sol = 0, total = 0;
		scanf("%d", &n);
		for (int i = 0; i <= n; i++) scanf("%1d", &data[i]);
		for (int i = 0; i <= n; i++) {
			if (i > total) {
				sol += i - total;
				total += i - total;
			}
			total += data[i];
		}
		printf("Case #%d: %d\n", T, sol);
	}
}