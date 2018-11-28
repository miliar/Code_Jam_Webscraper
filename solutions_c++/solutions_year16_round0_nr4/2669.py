# include <stdio.h>
# include <stdlib.h>
# include <string.h>

using namespace std;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int kase = 0; kase < t; kase ++) {
		printf("Case #%d: ", kase + 1);

		int k, c, s;

		scanf("%d%d%d", &k, &c, &s);

		long long base = 1;
		c--;
		while (c--) {
			base *= (long long)k;
		}

		printf("1");
		for (int i = 1; i < k; i ++) {
			printf(" %lld", i * base + 1);
		}

		printf("\n");
	}
}