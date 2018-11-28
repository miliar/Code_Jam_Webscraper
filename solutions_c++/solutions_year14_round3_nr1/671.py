#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all_of(v) v.begin(), v.end()
#define fi first
#define se second
#define pb push_back

ll gcd(ll a, ll b) {
	if (b == 0) {
		return a;
	} else if (a < b) {
		return gcd(b, a);
	} else {
		return gcd(b, a % b);
	}
}

bool is_pot(ll x) {
	while (x % 2 == 0) {
		x /= 2;
	}

	return x == 1;
}

int solve(ll p, ll q) {

	//cout << "solve(" << p << ", " << q << ")" << endl;

	ll g = gcd(p, q);

	p /= g;
	q /= g;

	if (p == 0) {
		return INT_MAX;
	}

	if (p == q - 1) {
		return 1;
	}
	
	/*
	if ((p - 1) % 4 == 0) {
		return solve(p + 1, q) + 1;
	} else {
		return solve(p - 1, q) + 1;
	}
	*/

	return min(solve(p + 1, q), solve(p - 1, q)) + 1;
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		cout << "Case #" << test << ": ";

		ll p, q;
		cin >> p;

		cin.get();

		cin >> q;

		ll g = gcd(p, q);

		p /= g;
		q /= g;

		if (!is_pot(q)) {
			cout << "impossible" << endl;
			continue;
		}

		int ans = 1;
		while (p < q / 2) {
			p *= 2;
			ans++;
		}

		cout << ans << endl;
	}
}