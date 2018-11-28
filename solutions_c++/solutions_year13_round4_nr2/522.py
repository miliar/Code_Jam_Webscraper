#include <cstdio>
#include <algorithm>
#include <string>
#include <stdint.h>
#include <map>

using namespace std;

const int MOD = 1000002013;

inline int64_t ticket_price(int n, int o, int e, int p) {
	e -= o; o = 2 * n + 1 - e;
	return ((int64_t)e * o / 2) % MOD * p % MOD;
}

int64_t get_min(int n, int64_t p) {
	int64_t b = (1LL) << (n - 1);
	int64_t s = 2;
	while (b > 0 && p >= b) {
		s <<= 1;
		p -= b;
		b >>= 1;
	}
	if (b == 0)
		s = s / 2 + 1;
	return s - 2;
}

int64_t get_max(int n, int64_t p) {
	int64_t f = (1LL) << n;
	int64_t b = f - 1;
	int64_t s = 1;
	while (p < b) {
		s <<= 1;
		b >>= 1;
	}
	
	return f - s;
}

int main() {
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		int n;
		int64_t p;
		scanf("%d%ld\n", &n, &p);
		p -= 1;
		printf("Case #%d: %ld %ld\n", i + 1, 
		       get_min(n, p),
		       get_max(n, p));
	}
	return 0;
}
