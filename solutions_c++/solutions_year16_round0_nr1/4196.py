#include <stdio.h>

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	scanf("%d", &t);

	int tc = 0;

	while (t--) {

		int n;
		scanf("%d", &n);

		bool used[10] = { 0 };

		printf("Case #%d: ", ++tc);

		if (n == 0)printf("INSOMNIA\n");
		else {
			int c = 0;
			for (int i = 1;; i++) {
				int k = n * i;
				while (k) {
					if (!used[k % 10]) {
						used[k % 10] = true;
						c++;
					}
					k /= 10;
				}
				if (c == 10) {
					printf("%d\n", n*i);
					break;
				}
			}
		}

	}

}