#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <gmpxx.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {
}

typedef long long ll;

vector<ll> solve_smart(int k, int c, int s) {
	if (s*c < k) {
		return {};
	} else {
		vector<ll> kpow(c+1);
		kpow[0] = 1ll;
		forn(i, c) {
			kpow[i+1] = kpow[i] * (ll) k;
		}
		vector<ll> ans;
		ll u = 0;
		bool stop = false;
		forn(i, s) {
			ll pos = 0ll;
			for (int d = 0; d < c; ++d) {
				pos += u * kpow[c - d - 1];
				assert (pos < kpow[c]);
				if (stop == false) {
					++u;
				}
				if (u >= k) {
					u = 0;
					stop = true;
				}
			}
			ans.push_back(pos + 1ll);
			if (stop) {
				return ans;
			}
		}
		return ans;
	}
}

vector<ll> solve(int k, int c, int s) {
	return solve_smart(k, c, s);
	if (s < k) {
		return {};
	} else {
		vector<ll> ans(k);
		forn(i, k) {
			ans[i] = i+1;
		}
		return ans;
	}
}

int main(void) {
	int t; cin >> t;
	forn(nc, t) {
		int k, c, s; cin >> k >> c >> s;
		vector<ll> ans = solve(k, c, s);
		if (ans.empty()) {
			cout << "Case #" << (nc+1) << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << (nc+1) << ":";
			for (auto x : ans) {
				cout << " " << x;
			}
			cout << endl;
		}
	}
	return 0;
}
