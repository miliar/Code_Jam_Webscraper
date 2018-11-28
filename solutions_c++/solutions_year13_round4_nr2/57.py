#include <iostream>
#include <cstdio>

using namespace std;

typedef long long lld;

int tests;
lld n, p, tot;

bool chk1(lld r) {
	lld tmp = 0;
	while ((((lld)1)<<tmp) <= r + 1) {
		tmp ++;
	}
	tmp --;
	//printf("%lld %lld %lld\n", r, tot - (((lld)1)<<(n - tmp)), p);
	if (tot - (((lld)1)<<(n - tmp)) >= p) return false;
	else return true;
}

lld binarysearch1() {
	lld le = 0, ri = tot;
	while (ri > le + 1) {
		lld mi = (le + ri) / 2;
		if (chk1(mi)) {
			le = mi;
		} else {
			ri = mi;
		}
	}
	return le;
}

bool chk2(lld r) {
	lld tmp = 0;
	while ((((lld)1)<<tmp) <= tot - r) {
		tmp ++;
	}
	tmp --;
	if ((((lld)1)<<(n - tmp)) > p) return false;
	else return true;
}

lld binarysearch2() {
	lld le = 0, ri = tot;
	while (ri > le + 1) {
		lld mi = (le + ri) / 2;
		if (chk2(mi)) {
			le = mi;
		} else {
			ri = mi;
		}
	}
	return le;
}

int main() {
	scanf("%d", &tests);
	for (int test = 0 ; test < tests ; test ++) {
		printf("Case #%d: ", test + 1);
		scanf("%lld %lld", &n, &p);
		tot = (((lld)1)<<n);
		printf("%lld ", binarysearch1());
		printf("%lld\n", binarysearch2());
	}
	return 0;
}