# include <stdio.h>
# include <stdlib.h>

using namespace std;

int hash;

void breakdown(long long x) {
	while (x != 0 && hash != 0) {
		int cur = x % 10;
		hash = hash & (~((1 << cur)));
		x /= 10;
	}
}

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int kase = 0; kase < t; kase ++) {
		printf("Case #%d: ", kase + 1);

		hash = 1023;

		long long n;

		scanf("%lld", &n);

		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}

		for (int i = 1; i <= 10000000; i ++) {
			breakdown(n * (long long)i);

			if (!hash) {
				printf("%lld\n", n * (long long)i);
				break;
			}
		}
	}
}