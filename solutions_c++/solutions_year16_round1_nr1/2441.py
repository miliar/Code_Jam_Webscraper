#include <bits/stdc++.h>
using namespace std;

string solve() {
	string s;
	cin >> s;

	string ans = s.substr(0, 1);

	for (int i = 1; i < s.size(); i++) {
		string t = s.substr(i, 1);
		if (ans + t >= t + ans) {
			ans = ans + t;
		} else {
			ans = t + ans;
		}
	}
	
	return ans;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
}