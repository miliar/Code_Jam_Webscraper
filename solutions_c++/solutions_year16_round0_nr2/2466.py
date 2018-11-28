#include <iostream>
#include <sstream>
#include <set>

using namespace std;

void solve() {
	string s;
	cin >> s;
	char m = '-';
	int ans = 0;
	for (int i = s.size() - 1; i >= 0; i--) {
		if (m == s[i]) {
			ans++;
			m = '+' + '-' - m;
		}
	}
	cout << " " << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ":";
		solve();
	}
}
