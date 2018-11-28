# include <iostream>

using namespace std;
typedef long long ll;

void solve() {
	string s;
	cin >> s;
	int n = s.size();
	int a[111];
	for(int i = 0; i < n; ++i) {
		a[i] = s[i] == '+';
	}
	int ans = 0;
	for(int i = n - 1; i >= 0; --i) {
		if(a[i] == 0) {
			ans++;
			for(int j = i; j >= 0; --j) {
				a[j] ^= 1;
			}
		}
	}
	cout << ans << '\n';
}

int main () {
	int t;
	cin >> t;
	for(int it = 1; it <= t; ++it) {
		cout << "Case #" << it << ": ";
		solve();
	}

	return 0;
}