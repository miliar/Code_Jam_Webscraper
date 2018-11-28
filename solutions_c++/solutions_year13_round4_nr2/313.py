#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long LL;

int T, n;
LL p, e[100];

bool ok_should(LL x) {
	int cnt = n - 1;
	LL before = 0;
	while (x) {
		x = (x - 1) / 2;
		before += e[cnt];
		cnt--;
	}
	return before + 1 <= p;
}

bool ok_could(LL x) {
	int cnt = n;
	LL after = 0;
	while (x + 1 < e[cnt]) {
		after += e[cnt - 1];
		cnt--;
		x = (x + 1) / 2;
	}
	return e[n] - after <= p;
}

int main() {
	scanf("%d", &T);
	e[0] = 1;
	for (int i = 1; i < 60; i++) e[i] = e[i - 1] * 2;

	for (int Test = 1; Test <= T; Test++) {
		printf("Case #%d: ", Test);
		scanf("%d%lld", &n, &p);

		LL m = e[n], l = 0, r = m - 1;
		while (l < r) {
			LL mid = (l + r + 1) / 2;
			if (ok_should(mid)) l = mid; else r = mid - 1;
		}

		printf("%lld ", l);

		l = 0; r = m - 1;
		while (l < r) {
			LL mid = (l + r + 1) / 2;
			if (ok_could(mid)) l = mid; else r = mid - 1;
		}
		printf("%lld\n", l);
	}
}
