#include <bits/stdc++.h>

using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)

double C, F, X;

double getTime(int farm) {
	double t = 0;
	for(int f = 0; f < farm; ++ f) {
		double rate = 2.0 + F * f;
		t += C / rate;
	}
	t += X / (2.0 + F * farm);
	return t;
}

double go() {
	cin >> C >> F >> X;

	int l = 0, r = (X+1);
	int ans = 0;

	// f(x) >= f(x+1), f(x+1) < f(x+2)
	while(l <= r) {
		int mid = (l + r) / 2;
		if(getTime(mid) >= getTime(mid + 1)) {
			// still good.
			l = mid + 1;
			ans = mid + 1;
		}
		else r = mid - 1;
	}

//	return getTime(ans);
	double ret = 1e100;
	for(int i = max(0, ans - 3); i <= ans + 3; ++ i) {
		ret = min(ret, getTime(i));
	}
	return ret;
}

int main() {
#if 0
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
#endif

	int T;
	cin >> T;
	for(int t = 1; t <= T; ++ t) {
		printf("Case #%d: %.7lf\n", t, go());
	}
	return 0;
}
