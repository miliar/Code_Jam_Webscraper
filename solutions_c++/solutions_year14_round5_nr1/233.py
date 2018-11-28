#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

typedef long long ll;

ll n, p, q, r, s;
ll tsum[1000000];

ll ntr(ll i) {
	return ((i * p + q) % r) + s;
}

void solve() {
	cin >> n >> p >> q >> r >> s;
	tsum[0] = ntr(0);
	for (ll i=1; i<n; i++) {
		tsum[i] = tsum[i-1] + ntr(i);
	}
	ll best = 0;
	for (ll i=0; i<n; i++) {
		best = max(best, min(tsum[i], tsum[n-1] - tsum[i]));
		ll lo(i), hi(n-1);
		while (lo < hi) {
			ll c = (lo + hi) / 2;
			ll low = tsum[i] - ntr(i);
			ll mid = tsum[c] - tsum[i] + ntr(i);
			ll high = tsum[n-1] - tsum[c];
			best = max(best, tsum[n-1] - max(low, max(mid, high)));
			if (high >= mid) {
				lo = c+1;
			} else {
				hi = c;
			}
		}
	}
	cout << ((long double)best / tsum[n-1]);
}

int main() {
	cout << setprecision(10) << fixed;
	int t;
	cin >> t;
	for (int casenum=1; casenum<=t; casenum++) {
		cout << "Case #" << casenum << ": ";
		solve();
		cout << "\n";
	}
}
