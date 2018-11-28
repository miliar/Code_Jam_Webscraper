#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin >> t;
	REP(o, t) {
		cout << "Case #" << o + 1 << ": ";
		string str;
		cin >> str;
		deque<char> winning;
		winning.push_back(str[0]);
		FOR(x, 1, str.size()) {
			if (str[x] >= winning.front()) {
				winning.push_front(str[x]);
			} else {
				winning.push_back(str[x]);
			}
		}
		for (auto it : winning) {
			cout << it;
		}
		cout << endl;
	}
	return 0;
}
#endif