#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int k, c, s;

ll pow(ll a, ll b) {
	if (b == 0) return 1;
	ll tmp = pow(a, b / 2);
	if (b % 2 == 0) return tmp * tmp;
	return tmp * tmp * a;
}

ll f(ll i, ll c) {
	if (c == 1) return i;
	if (i == 1) return 1;
	if (i == k) return pow(k, c);

	// f(i, C) = [f(i, C - 1) - 1] * K + i
	return (f(i, c - 1) - 1) * k + i;
}

ll f1(ll i0, ll i, ll c1) {
	if (c1 == c) return i;

	return f1(i0, (i - 1) * k + i0, c1 + 1);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ctest = 1; ctest <= t; ctest++) {
		scanf("%d %d %d", &k, &c, &s);

		printf("Case #%d:", ctest);
		for (int i = 1; i <= k; i++) {
			printf(" %lld", f1(i, i, 1));
		}
		printf("\n");
	}
	return 0;
}
