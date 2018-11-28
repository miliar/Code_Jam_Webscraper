#include <iostream>
#include <string>

using namespace std;

int RR, PP, SS; 

string can(int n, int& r, int& p, int& s, char w, bool first = 1) {
	if (first)
		r = p = s = 0;

	if (n == 0) {
		if (w == 'R') ++r;
		if (w == 'S') ++s;
		if (w == 'P') ++p;
		if (r <= RR && p <= PP && s <= SS) return string(1, w);
		else return "";
	} else {
		if (w == 'R') {
			string L = can(n - 1, r, p, s, 'R', false);
			string R = can(n - 1, r, p, s, 'S', false);
			if (L.length() > 0 && R.length() > 0)
				return min(L, R) + max(L, R);
			else
				return "";
		}
		if (w == 'S') {
			string L = can(n - 1, r, p, s, 'P', false);
			string R = can(n - 1, r, p, s, 'S', false);
			if (L.length() > 0 && R.length() > 0)
				return min(L, R) + max(L, R);
			else
				return "";
		}
		if (w == 'P') {
			string L = can(n - 1, r, p, s, 'R', false);
			string R = can(n - 1, r, p, s, 'P', false);
			if (L.length() > 0 && R.length() > 0)
				return min(L, R) + max(L, R);
			else
				return "";
		}
	}
}

void solve() {
	string ans = "IMPOSSIBLE";

	int N; cin >> N;
	cin >> RR >> PP >> SS;
	int R, P, S;
	R = P = S = 0;

	if (can(N, R, P, S, 'R').length()) ans = can(N, R, P, S, 'R');
	if (can(N, R, P, S, 'S').length()) ans = can(N, R, P, S, 'S');
	if (can(N, R, P, S, 'P').length()) ans = can(N, R, P, S, 'P');

	static int test_id;
	cout << "Case #" << ++test_id << ": " << ans << endl; 
}

int main() {
	int t; cin >> t;
	while (t --> 0)
		solve();
	return 0;
}
