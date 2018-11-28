#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 7)
using namespace std;

typedef long long ll;
ll p, q;

inline void read() {
	scanf("%lld/%lld", &p, &q);
}

inline void solve() {
	ll gcd = __gcd(p, q);
	p /= gcd;
	q /= gcd;

	ll pow2 = 1LL;
	while (pow2 < q) pow2 *= 2LL;
	if (pow2 > q) {
		puts("impossible");
		return;
	}

	ll c = q / 2LL, ans = 0LL;
	while (c) {
		ans ++;
		if (c <= p) break;
		c /= 2LL;
	}

	cout << ans << '\n';
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		read();
		solve();
	}
	return 0;
}