#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;



bool checkCircle(vector<int> circ, vector<int> friends) {
	auto next = [&circ](int x) -> int {
		if (x == circ.size() - 1) {
			return 0;
		} else {
			return x + 1;
		}
	};
	auto prev = [&circ](int x) -> int {
		if (x == 0) {
			return circ.size() - 1;
		} else {
			return x - 1;
		}
	};

	REP(x, circ.size()) {
		int v = circ[x];
		int f = friends[v];
		// cout << v << " " << f << " " << circ[next(x)] << " " << circ[prev(x)] << endl;
		if (f != circ[next(x)] && f != circ[prev(x)]) {
			// cout << "ERROR!\n";
			// for (auto it : circ) {
	  //   		cout << it + 1 << " ";
	  //   	}
	  //   	cout << endl;
	    	return false;
		}
	}
    return true;
}

int checkCombination(vector<int> comb, vector<int> friends) {
    sort(comb.begin(), comb.end());
    do {
        if (checkCircle(comb, friends)) {
            // for (auto it : comb) {
            //     cout << it + 1 << " ";
            // }
            // cout << endl;
            return comb.size();
        }
    } while (next_permutation(comb.begin(), comb.end()));
    return 0;
}

int solve(vector<int> friends) {
    int res = 0;
    int n = (1 << friends.size());
    for (int i = 0; i < n; ++i) {
        vector<int> comb;
        REP(x, friends.size()) {
            if (i & (1 << x)) {
                comb.push_back(x);
            }
        }
        res = max(res, checkCombination(comb, friends));
    }
    return res;
}

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin >> t;
	REP(o, t) {
		int n;
		cin >> n;
		vector<int> friends(n);
        REP(x, n) {
            cin >> friends[x];
            --friends[x];
        }
        cout << "Case #" << o + 1 << ": " << solve(friends) << endl;
	}
	return 0;
}
#endif