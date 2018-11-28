#define HEADER_H
//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ull          = unsigned long long;
using ll           = long long;
using ld           = long double;
using vi           = vector<ll>;
using vvi          = vector<vi>;
using vb           = vector<bool>;
using ii           = pair<ll, ll>;
constexpr bool LOG = true;
void Log() {
	if(LOG) cerr << "\n";
}
template <class T, class... S>
void Log(T t, S... s) {
	if(LOG) cerr << t << "\t", Log(s...);
} /* ============== END OF HEADER ============== */

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";

		string s;
		int k;
		cin >> s >> k;
		vector<bool> b;
		b.reserve(s.size());
		for(auto c : s) b.push_back(c == '+');

		int ans = 0;
		for(int i = 0; i < b.size() - k + 1; ++i) {
			if(!b[i]) {
				// flip range
				++ans;
				for(int j = 0; j < k; ++j) b[i + j] = !b[i + j];
			}
		}
		// remainder must be +
		bool pos = true;
		for(int i         = b.size() - k + 1; i < b.size(); ++i)
			if(!b[i]) pos = false;
		if(pos)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
