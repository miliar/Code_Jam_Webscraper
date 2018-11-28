#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

#define ll long long

ll gcd(ll a, ll b) {
	if (b > a) {
		ll t = b;
		b = a;
		a = t;
	}

	if (b == 0) {
		return a;
	}

	return gcd(b, a % b);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	scanf("%d", &tests);

	for (int t = 1; t <= tests; t++) {
		ll p, q;

		scanf("%I64d/%I64d", &p, &q);

		ll g = gcd(p, q);

		p /= g;
		q /= g;

		ll base = 2;
		bool ok = false;
		for (int i = 1; i <= 50; i++) {
			if (q == base) {
				ok = true;
				break;
			}
			base *= 2;
		}

		if (!ok) {
			printf("Case #%d: impossible\n", t);
			continue;
		}

		int count = 1;
		while (p < q / 2) {
			p *= 2;
			count++;
		}

		printf("Case #%d: %d\n", t, count);
	}
	
	return 0;
}
/*
8
1/2
3/4
6/8
1/4
3/22
1/256
123/31488
2/562949953421312
*/