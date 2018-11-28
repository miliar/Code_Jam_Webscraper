#include <iostream>
#include <string>
#include <algorithm>
#define ll long long
using namespace std;

void solve(string s) {
	int i, j, ans = 0, n = s.length();
	bool a[n];
	for (i = 0; i < n; ++i) {
		a[i] = (s[i] == '+');
	}
	while (1) {
		for (i = n - 1; i >= 0; --i) {
			if (!a[i]) {
				break;
			}
		}
		if (i < 0) {
			break;
		}
		for (j = i; j >= 0; --j) {
			a[j] = !a[j];
		}
		++ans;
	}
	cout << ans << '\n';
}

int main() {
	int tc, T;
	string s;
	cin >> T;
	for (tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";
		cin >> s;
		solve(s);
	}
	return 0;
}