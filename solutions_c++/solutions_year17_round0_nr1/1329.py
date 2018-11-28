#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc() {

}

void solve() {
	string s;
	int k;

	cin >> s >> k;

	int ans = 0;
	for (int i = 0; i + k <= s.size(); ++i) {
		if (s[i] == '-') {
			for (int j = i; j < i + k; ++j) {
				s[j] = (s[j] == '-' ? '+' : '-');
			}
			++ans;
		}
	}

	if (count(s.begin(), s.end(), '-') > 0) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << ans << endl;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
		cerr << test << endl;
		solve();
	}
	return 0;
}
