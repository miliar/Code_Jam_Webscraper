#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iomanip>
#include <utility>

using namespace std;

int dp[10011][5];
string _s;

string dupe(const string& str, int times) {
	string ret;
	ret.reserve(str.length() * times);
	for (int i = 0; i < times; i++) ret.append(str);
	return ret;
}

// codes:
// 1 = 1, i = 2, j = 3, k = 4

int c_mult(int x, int y) {

	int mod = 1;
	if (x < 0) {
		mod = -1;
		x = -x;
	}
	if (x == 1) return y * mod;
	if (y == 1) return x * mod;
	if (x == y) return -1 * mod;
	if (x == 2 && y == 3) return 4 * mod;
	if (x == 3 && y == 2) return -4 * mod;
	if (x == 3 && y == 4) return 2 * mod;
	if (x == 4 && y == 3) return -2 * mod;
	if (x == 2 && y == 4) return -3 * mod;
	if (x == 4 && y == 2) return 3 * mod;
	return 0;
}

int trans(char ch) {
	return (ch - 'i') + 2;
}

// state = 0, 1, 2
int memo(int idx, int state) {
	int poss = 0;
	if (state == 3 && idx == _s.length()) return 1;
	if (state == 3) return 0;
	if (idx >= _s.length()) return 0;
	int& ret = dp[idx][state];
	if (ret != -1) return ret;
	//cout << "memo(" << idx << "," << state << ") for string: " << _s << "\n";
	int start = trans(_s[idx]);
	if (start == (state + 2)) {
		poss = max(poss, memo(idx + 1, state + 1));
	}
	for (int i = idx + 1; i + (2 - state) < _s.length(); i++) {
		// try to get the state
		//cout << "multiply " << start << " by " << trans(_s[i]) << " = " << c_mult(start, trans(_s[i])) << endl;
		start = c_mult(start, trans(_s[i]));
		//cout << "start = " << start << " iter = " << i << "\n";
		
		if (start == (state + 2)) {
			// memo
			poss = max(poss, memo(i + 1, state + 1));
		}
	}

	return ret = poss;
}

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int L, X; cin >> L >> X;
		std::string str; cin >> str;
		_s = dupe(str, X);
		memset(dp, -1, sizeof(dp));
		int z = memo(0, 0);
		cout << "Case #" << t << ": " << (z == 1 ? "YES" : "NO") << endl;
	}
	return 0;
}