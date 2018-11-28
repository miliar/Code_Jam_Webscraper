#include <cstdio>

typedef long long lint;

lint pior(lint x, int n) {
	if (x == 0) return 0;
	else return (1LL<<(n-1)) + pior( (x - 1) / 2, n - 1);
}

lint melhor(lint x, int n) {
	if (x == (1LL<<n) - 1) {
		return x;
	} else {
		lint piores = (1LL<<n) - x - 1;
		lint y = (1LL<<(n-1)) - (piores - 1) / 2 - 1;
		return melhor(y, n - 1);
	}
}

int main() {
	int n, ntests;
	lint p;
	
	scanf("%d", &ntests);
	for (int test = 1; test <= ntests; test++) {
		scanf("%d %I64d", &n, &p);
		
		lint garante = 0;
		
		lint bot = 0, top = (1LL<<n)-1;
		
		while (bot <= top) {
			lint mid = (bot + top) / 2;
			if (pior(mid, n) < p) {
				garante = mid;
				bot = mid + 1;
			} else {
				top = mid - 1;
			}
		}
		
		lint podeser = 0;
		
		bot = 0, top = (1LL<<n)-1;
		while (bot <= top) {
			lint mid = (bot + top) / 2;
			if (melhor(mid, n) < p) {
				podeser = mid;
				bot = mid + 1;
			} else {
				top = mid - 1;
			}
		}
		
		printf("Case #%d: ", test);
		printf("%I64d %I64d\n", garante, podeser);
	}
	
	return 0;
}