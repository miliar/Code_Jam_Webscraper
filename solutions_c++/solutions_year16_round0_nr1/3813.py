#include <bits/stdc++.h>

#include <emmintrin.h>

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

using namespace std;

typedef long long ll;

const int maxn = 201000;

void solve() {
	ll n;
	cin >> n;
	if (n == 0) cout << "INSOMNIA\n";
	else {
		ll cur = n;
		set<int> digs;
		while (true) {
			for (ll x = cur; x; x /= 10) {
				digs.insert(x % 10);
			}
			if (digs.size() == 10) {
				break;
			}
			cur += n;
		}
		cout << cur << endl;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
}
