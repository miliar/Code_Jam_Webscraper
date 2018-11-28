#include <cstdio>

using namespace std;

int main() {
	int tt;
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++) {
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", t);
		if ((c == 1 && s < k) || (c > 1 && s < k-1)) {
			printf(" IMPOSSIBLE\n");
		} else {
			if (k == 1) {
				printf(" 1");
			} else if (c == 1) {
				for (int i = 1; i <= k; i++) {
					printf(" %d", i);
				}
			} else {
				for (int i = 2; i <= k; i++) {
					printf(" %d", i);
				}
			}
			printf("\n");
		}
	}
}