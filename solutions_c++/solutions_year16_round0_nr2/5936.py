#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define ll long long
int t;

int baga(char c, string s) {
	s += '.';
	string currS = "";
	currS = s[0];
	int ans = 0;
	int bug = 0;
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] != s[i - 1]) {
			if (currS[0] != c) {
				ans += + 1 + bug;
			}
			bug = 1;
			currS = s[i];
		}
	}
	if (c == '-') {
		ans ++;
	}
	return ans;
}

int main() {
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	#endif

	cin >> t;
	cin.get();
	for (int i = 1; i <= t; ++i) {
		string s;
		cin >> s;
		int ans = min(baga('-', s), baga('+', s));
		cout << "Case #" << i << ": " << ans << "\n";
	}

	return 0;
}