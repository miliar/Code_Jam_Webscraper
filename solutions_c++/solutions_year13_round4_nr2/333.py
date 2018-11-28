#include <cstdio>

typedef long long ll;

int n;
ll p;

ll calc(ll v) {
	ll ret = 0;
	for (int i = 0; i < n && v; ++ i) {
		v = (v - 1) / 2;
		ret += 1LL << (n - i - 1);
	}
	return ret;
}

ll solve_0() {
	ll low = 0, upp = 1LL << n;
	while (upp - low > 1) {
		ll mid = (low + upp) / 2;
		if (calc(mid) < p) {
			low = mid;
		} else {
			upp = mid;
		}
	}
	return low;
}

ll solve_1() {
	ll low = 0, upp = 1LL << n;
	while (upp - low > 1) {
		ll mid = (low + upp) / 2;
		if ((1LL << n) - 1 - calc((1LL << n) - 1 - mid) < p) {
			low = mid;
		} else {
			upp = mid;
		}
	}
	return low;
}

int main() {
	int tn;
	scanf("%d", &tn);
	for (int t = 1; t <= tn; ++ t) {
		scanf("%d%lld", &n, &p);
		printf("Case #%d: %lld %lld\n", t, solve_0(), solve_1());
	}
	return 0;
}
