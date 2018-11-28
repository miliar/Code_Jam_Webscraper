#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve() {
	string s;
	cin >> s;

	int ans = s.length() / 2 * 5;

	vector<char> d;
	for (int i = 0; i < s.length(); ++i) {
		if (d.size() == 0 || d.back() != s[i]) {
			d.push_back(s[i]);
		} else {
			d.pop_back();
			ans += 5;
		}
	}

	static int test_id;
	cout << "Case #" << ++test_id << ": " << ans << endl; 
}

int main() {
	int t; cin >> t;
	while (t --> 0)
		solve();
	return 0;
}
