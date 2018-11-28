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
#include <gmpxx.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {
}

typedef long long ll;

ll getOneDivisor(ll n) {
	if (n == 0ll || n == 1ll) return n;
	else if (n == 2ll || n == 3ll || n == 5ll || n == 7ll) return -1;
	else if (n % 2ll == 0ll) return n / 2ll;
	else if (n % 3ll == 0ll) return n / 3ll;
	else {
		for (ll i = 5ll; i * i <= n; i += 6ll) {
			if (n % i == 0ll) { return i; }
			if (n % (i + 2ll) == 0ll) { return i + 2ll; }
		}
		return -1;
	}
}

ll makeBase(ll seq, ll base) {
	ll res = 0;
	ll mult = 1ll;
	while (seq) {
		res += (seq & 1ll) * mult;
		seq >>= 1;
		mult *= base;
	}
	return res;
}

string toString(ll seq) {
	string s;
	while (seq) {
		if (seq & 1ll) {
			s.push_back('1');
		} else {
			s.push_back('0');
		}
		seq >>= 1;
	}
	std::reverse(s.begin(), s.end());
	return s;
}

void solve_small(int n, int j) {
	int cnt = 0;
	for (ll i = 1; i < (1ll << (n - 1)); i += 2ll) {
		ll x = (1ll << (n - 1)) + i;
		vector<ll> tokens;
		for (ll base = 2; base <= 10; ++base) {
			ll y = makeBase(x, base);
			ll d = getOneDivisor(y);
			if (d < 0) { break; }
			tokens.push_back(d);
		}
		if ((int) tokens.size() == 9) {
			++cnt;
			cout << toString(x);
			for (auto d : tokens) {
				cout << " " << d;
			}
			cout << endl;
			if (cnt == j) { break; }
		}
	}
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		int n, j; cin >> n >> j;
		cout << "Case #" << (k+1) << ": " << "" << endl;
		solve_small(n, j);
	}
	return 0;
}
