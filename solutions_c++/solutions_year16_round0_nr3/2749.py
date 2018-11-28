#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#define ll long long
using namespace std;

int n = 16, r = 50;

ll conv(ll a, ll base) {
	ll c = 1, ret = 0;
	while (a > 0) {
		ret += (a%2)*c;
		c *= base;
		a /= 2;
	}
	return ret;
}

ll check(ll a) {
	for (ll i = 2; i <= sqrt(a); i++) {
		if (a%i == 0) return i;
	}
	return -1;
}

int main() {
	printf("Case #1:\n");
	for (int i = (1<<(n-1))+1; i < (1<<n); i += 2) {
		bool ok = 1;
		ll div[11];
		for (int j = 2; j <= 10; j++) {
			ll a = check(conv(i, j));
			if (a == -1) {
				ok = 0;
				break;
			}
			else {
				div[j] = a;
			}
		}
		if (ok) {
			r--;
			ll t = i;
			int b[n], d = n;
			while (t > 0) {
				b[--d] = t%2;
				t /= 2;
			}
			for (int k = 0; k < n; k++) printf("%d", b[k]);
			printf(" ");
			for (int k = 2; k <= 10; k++) {
				printf("%lld ", div[k]);
			}
			printf("\n");
			if (r == 0) break;
		}
	}
	return 0;
}