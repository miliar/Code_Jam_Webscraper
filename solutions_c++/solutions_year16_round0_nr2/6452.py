#include <stdio.h>
#include <string.h>

int n, x, a[105];
char t[105];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%s", t + 1);
		x = strlen(t + 1);
		for (int j = 1; j <= x; j++) {
			a[j] = t[j] == '+' ? 1 : 0;
		}

		int count = 0;
		for (;;) {
			int last = 0;
			for (int j = x; j >= 1; j--) {
				if (a[j] == 0) {
					last = j;
					break;
				}
			}
			if (last == 0) {
				break;
			}
			count++;
			for (int j = 1; j <= last; j++) {
				a[j] = 1 - a[j];
			}
		}
		printf("Case #%d: %d\n", i, count);
	}

	return 0;
}