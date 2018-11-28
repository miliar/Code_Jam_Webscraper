#include <cstdio>

int main() {
	int tests; scanf("%d", &tests);
	for (int t = 1; t <= tests; t++) {
		int smax; scanf("%d", &smax);

		int qtt[1005];

		for (int i = 0; i <= smax; i++) {
			char c; scanf(" %c", &c);
			qtt[i] = (int) (c - '0');
		}

		int curr = 0;
		int ans = 0;
		for (int s = 0; s <= smax; s++) {
			if (qtt[s] == 0)
				continue;

			int need = s - curr;
			if (need > 0) {
				ans += need;
				curr += need;
			}

			curr += qtt[s];
		}

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}