#include <cstdio>

typedef long long llint;
const llint LIMIT = 1000000, P = (1 << 10) - 1;

void check(llint &num, llint n) {
	while (n) {
		int x = n % 10;
		num |= 1 << x;
		n /= 10;
	}
}

int T;
llint n;

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		scanf("%lld", &n);
		llint num = 0;
		for (llint i = 1; i <= LIMIT; ++i) {
			check(num, i * n);
			if (num == P) {
				printf("%lld\n", i * n);
				break;
			}
		}
		if (num != P) printf("INSOMNIA\n");
	}
	return 0;
}
