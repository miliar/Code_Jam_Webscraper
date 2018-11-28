#include <cstdio>
#include <algorithm>
#include <cassert>
#include <cstring>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int mult(int a, int b) {
	int qa = a / 4;
	int qb = b / 4;
	int ra = a % 4;
	int rb = b % 4;
	int v = 4 * (qa + qb);
	if (ra == 0) return (v + rb) % 8;
	if (rb == 0) return (v + ra) % 8;
	if (ra == rb) return (v + 4) % 8;
	if (ra == 1 && rb == 2) return (v + 3) % 8;
	if (ra == 1 && rb == 3) return (4 + v + 2) % 8;
	if (ra == 2 && rb == 1) return (4 + v + 3) % 8;
	if (ra == 2 && rb == 3) return (1 + v) % 8;
	if (ra == 3 && rb == 1) return (2 + v) % 8;
	if (ra == 3 && rb == 2) return (4 + 1 + v) % 8;
	assert(0);
}

int powmod(int a, long long b) {
	int res = 0;
	while (b) {
		if (b & 1) res = mult(a, res);
		a = mult(a, a);
		b >>= 1;
	}
	return res;
}

int c[26];
char str[1 << 20];

int solve(int test) {
	int L;
	long long X;
	scanf("%d%lld", &L, &X);
	scanf("%s", str);
	c['i' - 'a'] = 1;
	c['j' - 'a'] = 2;
	c['k' - 'a'] = 3;
	int v = mult(1, 2);
	v = mult(v, 3);
	int u = 0;
	for (int i = 0; i < L; i++) u = mult(u, c[str[i] - 'a']);
	u = powmod(u, X);
	if (u != v) {
		printf("Case #%d: NO\n", test);
	} else {
		long long mina = L * X + 1;
		int val = 0;
		for (long long i = 0; i < min(50LL * L, L * X); i++) {
			val = mult(val, c[str[i % L] - 'a']);
			if (val == 1) {
				mina = i + 1;
				break;
			}
		} 
		val = 0;
		long long maxb = -1;
		for (long long i = L * X - 1; i >= max(0LL, L * (X - 50)); i--) {
			val = mult(c[str[i % L] - 'a'], val);
			if (val == 3) {
				maxb = i;
				break;
			}
		}
		if (maxb - mina >= 1LL) {
			printf("Case #%d: YES\n", test);
		} else {
			printf("Case #%d: NO\n", test);
		}
	}
	return 1;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) solve(t);
}
