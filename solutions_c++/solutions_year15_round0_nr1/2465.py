#include <bits/stdc++.h>

using namespace std;

#define _ ios_base::sync_with_stdio(false); cin.tie(NULL);

typedef long long ll;

int main() { _
	ll t;
	cin >> t;
	for (ll test = 1; test <= t; ++test) {
		cout << "Case #" << test << ": ";
		ll n, sum = 0, ans = 0;
		string s;
		cin >> n >> s;
		sum = s[0] - '0';
		for (ll i = 1; i < s.length(); ++i) {
			if (sum >= i)
				sum += s[i] - '0';
			else {
				ans += i - sum;
				sum = i;
				sum += s[i] - '0';
			}
		}
		cout << ans << endl;
	}
}
