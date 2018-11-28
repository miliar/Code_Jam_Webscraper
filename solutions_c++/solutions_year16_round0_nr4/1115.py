#include <cstdio>

int main() {
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int ca = 0;
	while (T--) {
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d:", ++ca);
		for (int i = 1; i <= k; ++i) {
			printf(" %d", i);
		}
		puts("");
	}
	return 0;
}
