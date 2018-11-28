#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cassert>

using namespace std;

typedef long long ll;

int n;
ll p;

ll minlow(int level, ll pos) {
	assert(pos >= 0 && pos <= (1LL << level));
	if (level == 0) return 1;
	if (pos == (1LL << level)) return pos;
	return minlow(level - 1, pos / 2 + 1);
}

ll maxhigh(int level, ll pos) {
	assert(pos >= 0 && pos <= (1LL << level));
	if (level == 0) return 1;
	if (pos == 1) return 1;
	return (1LL << (level - 1)) + maxhigh(level - 1, pos / 2);
}

int solve(int id) {
	cout << "Case #" << id << ": ";
	cin >> n >> p;
	ll l = 0, r = (1LL << n) + 1;
	while (l < r - 1) {
		ll m = (l + r) / 2;
		//cerr << "min of " << m << " = " << minlow(n, m) << endl;
		if (minlow(n, m) > p)
			r = m;
		else
			l = m;
	}
	ll a1 = l;
	l = 0, r = (1LL << n) + 1;
	while (l < r - 1) {
		ll m = (l + r) / 2;
		if (maxhigh(n, m) > p)
			r = m;
		else
			l = m;
	}
	ll a2 = l;
	cout << a2 - 1 << " " << a1 - 1 << endl;
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
		solve(i + 1);
	return 0;
}
