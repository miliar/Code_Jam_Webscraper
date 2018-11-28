#include <stdio.h>
#include <string.h>
int c[10];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int runs = 1;
	int T; for (scanf("%d", &T); T--; ) {
		long long x;
		scanf("%lld", &x);
		memset(c, 0, sizeof(c));
		int cnt = 0;
		long long res = -1;
		for (int k = 1; k <= 1e6; k++) {
			long long y = x*k;
			while (y) {
				if (c[y % 10] == 0) cnt++;
				c[y % 10] = 1;
				y /= 10;
			}
			if (cnt == 10) {
				res = x*k;
				break;
			}
		}
		printf("Case #%d: ", runs++);
		if (res < 0) puts("INSOMNIA");
		else printf("%lld\n", res);

	}
	fcloseall();
	return 0;
}