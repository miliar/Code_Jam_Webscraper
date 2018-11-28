# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <deque>
# include <algorithm>

using namespace std;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int kase = 1; kase <= t; kase ++) {
		printf("Case #%d: ", kase);

		int n;
		scanf("%d", &n);
		int a[30];
		int mn = 0;
		for (int i = 0; i < n; i ++) {
			scanf("%d", &a[i]);
			if (i) {
				mn = min(mn, a[i]);
			} else {
				mn = a[i];
			}
		}

		while (1) {
			int mx = a[0];
			int p = 0;
			for (int i = 1; i < n; i ++) {
				if (a[i] > mx) {
					mx = a[i];
					p = i;
				}
			}

			if (mx == mn) break;

			printf("%c ", p + 'A');
			a[p]--;
		}

		for (int i = 0; i < n - 2; i ++) {
			for (int j = 0; j < a[i]; j ++) printf("%c ", i + 'A');
		}

		for (int i = 0; i < a[n - 1]; i ++) {
			printf("%c%c ", n - 2 + 'A', n - 1 + 'A');
		}

		printf("\n");
	}
}