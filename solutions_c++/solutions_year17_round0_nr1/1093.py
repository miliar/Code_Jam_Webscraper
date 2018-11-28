#include <iostream>
#include <string>

using namespace std;

void solve() {
	string s;
	int k = 0;
	cin >> s;
	cin >> k;
	int cnt = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-' && i + k < s.size() + 1) {
			cnt++;
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '-')
					s[i + j] = '+';
				else
					s[i + j] = '-';
			}
		}
	}
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << cnt << endl;
}

int main() {
	int test = 0;
	cin >> test;
	for (int i = 1; i <= test; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}