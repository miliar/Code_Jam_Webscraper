#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(ll i = ll(ini); i < ll(lim); i++)
#define ford(i, ini, lim) for(ll i = ll(ini); i >= ll(lim); i--)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> ii;

void get_digits(ll x, set<ll> &s) {
	while(x) {
		s.insert(x % 10);
		x /= 10;
	}
}

ll last(ll x) {
	set<ll> s;
	ll ini_x = x;
	while(1) {
		get_digits(x, s);
		if(s.size() == 10) {
			break;
		}
		x += ini_x;
	}
	return x;
}

int main() {
	ios_base::sync_with_stdio(false);

	ll kase = 1;
	ll t;
	cin >> t;
	while(t--) {	
		ll n;
		cin >> n;
		cout << "Case #" << kase++ << ": ";
		if(n == 0) {
			cout << "INSOMNIA";
		}
		else {
			cout << last(n);
		}
		cout << '\n';
	}
	return 0;	
}
