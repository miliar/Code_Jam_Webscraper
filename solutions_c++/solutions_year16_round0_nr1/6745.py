#include <stdio.h>
int main() {
	int i;
	int t;
	int n;
	int ans = 0;
	int k = 0;
	int tmp;
	bool chk[11];
	int sw;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		sw = ans = 0;
		for (i = 0; i < 10; i++) chk[i] = false;

		scanf("%d", &n);

		printf("Case #%d: ", ++k);
		if (n == 0) printf("INSOMNIA\n");
		else {
			while (1) {
				ans += n;
				tmp = ans;
				while (tmp > 0) {
					if (!chk[tmp % 10]) {
						chk[tmp % 10] = true;
						sw++;
					}
					tmp /= 10;
				}
				if (sw == 10) break;
			}
			printf("%d\n", ans);
		}
	}
	return 0;
}