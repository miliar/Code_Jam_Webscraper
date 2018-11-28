#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <memory>
#include <bitset>
#include <iomanip>
#include <deque>

using namespace std;
using ll = long long;
#define FOR(i,a,b) for(ll i=(a); i<(b); ++i)

static double compute(const vector<double> &picked) {
		map<ll,double> dp;
		dp[0] = 1;
		for(double p : picked) {
			map<ll,double> ndp;
			for(auto e : dp) {
				ndp[e.first-1] += e.second*p;
				ndp[e.first+1] += e.second*(1-p);
			}
			swap(dp,ndp);
		}
		return dp[0];
}

int main() {
	ll T; cin >> T;
	FOR(t,0,T) {
		cout << "Case #" << t+1 << ": ";
		ll k, n;
		cin >> n >> k;
		vector<double> ps;
		FOR(i,0,n) {
			double p;
			cin >> p;
			ps.push_back(p);
		}
		sort(begin(ps),end(ps));

		vector<double> picked{0};
		FOR(mask, 0, 1<<n) {
			if(__builtin_popcount(mask) != k) continue;
			vector<double> cand;
			FOR(i,0,n) {
				if((1<<i) & mask)
					cand.push_back(ps[i]);
			}
			if(compute(cand) >= compute(picked))
				swap(cand, picked);
		}

		cout << setprecision(10) << compute(picked);
		cout << endl;
	}
}
