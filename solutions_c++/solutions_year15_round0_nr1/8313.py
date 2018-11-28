#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
	ll T;
	cin >> T;
	for (ll t = 1; t <= T; t++) {
		{ ll smax; cin >> smax; }
		string s;
		cin >> s;
		ll sum = 0;
		ll add = 0;
		for (ssize_t i = 0; i < s.size(); i++) {
			ll n = s[i] - '0';
			ll x = max(0LL, i - sum);
			sum += x + n;
			add += x;
		}
		cout << "Case #" << t << ": " << add << endl;
	}
}
