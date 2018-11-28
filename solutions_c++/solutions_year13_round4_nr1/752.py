#include <iostream>
#include <vector>
#include <map>
#include <cassert>
using namespace std;

const long long MOD = 1000002013ll;
long long n;

inline long long calc(long long dta, long long v) {
	return ((n + n - dta + 1) * dta / 2 % MOD) * v % MOD;
}

inline void add(long long & a, long long b) {
	a = (a + b) % MOD;
}

int main() {
	int T, m;
	cin >> T;
	for (int ca = 1; ca <= T; ca++) {
		cin >> n >> m;
		map<long long, long long> mp;
		vector<pair<long long, long long>> stk;
		long long orig = 0, l, r, v, ans = 0;
		for (int i = 0; i < m; i++) {
			cin >> l >> r >> v;
			add(orig, calc(r - l, v));
			mp[l] += v;
			mp[r] -= v;
			if (mp[l] == 0)
				mp.erase(l);
			if (mp[r] == 0)
				mp.erase(r);
		}
		for (auto & iter : mp) {
			if (iter.second >= 0)
				stk.push_back(make_pair(iter.first, iter.second));
			else {
				long long cost = -iter.second;
				while (stk.size() > 0 && stk.back().second <= cost) {
					cost -= stk.back().second;
					add(ans, calc(iter.first - stk.back().first, stk.back().second));
					stk.pop_back();
				}
				stk.back().second -= cost;
				add(ans, calc(iter.first - stk.back().first, cost));
			}
		}
		assert(orig - ans + MOD >= 0);
		cout << "Case #" << ca << ": " << (orig - ans + MOD) % MOD << "\n";
	}
	return 0;
}
