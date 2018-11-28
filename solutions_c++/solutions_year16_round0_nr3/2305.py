#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

inline ll eval(ll n, ll base) {
	ll val = 0;
	ll mult = 1;
	while(n) {
		val += (n & 1) * mult;
		mult *= base;
		n >>= 1LL;
	}
	return val;
}

ll mult(ll a, ll b, ll mod) {
	a %= mod;
	if(b > 0) {
		if(b & 1) {
			return (a + mult(a, b - 1, mod)) % mod;
		}
		else {
			return mult(a * 2, b / 2, mod) % mod;
		}
	}
	return 0;
}

ll f_exp(ll n, ll exp, ll mod) {
	n %= mod;
	if(exp > 1) {
		if(exp & 1) {
			return mult(n, f_exp(n, exp - 1, mod), mod) % mod;
		}
		else {
			return f_exp(mult(n, n, mod), exp >> 1, mod) % mod;
		}
	}
	return !exp ? 1 : n;
}

// miller-rabin's primality check 
bool is_prime(ll n) {
	if(n == 1) {
		return false;
	}
	if(!(n & 1)) {
		return n == 2;
	}
	ll d = n - 1;
	ll s = 0;
	while(!(d & 1)) {
		d >>= 1;
		s++;
	}
	for(ll i = 3; i <= min(20LL, n - 2); i++) {
		bool prime = false;
		if(f_exp(i, d, n) == 1) {
			prime = true;
		}
		else {
			for(ll k = 0; k <= s - 1; k++) {
				if(f_exp(i, (1LL << k) * d, n) == n - 1) {
					prime = true;
					break;
				}
			}
		}

		if(!prime) {
			return false;
		}
	}
	return true;
}

string to_bin(ll x) {
	string bin = "";
	while(x) {
		bin += (x & 1) + '0';
		x >>= 1;
	}
	reverse(bin.begin(), bin.end());
	return bin;
}

int main() {
	ios_base::sync_with_stdio(false);
	
	int kase = 1;
	vector<ll> coins;
	for(ll i = (1LL << 15) + 1; i < (1LL << 16) && coins.size() < 50; i += 2) {
		bool deu_bom = true;	
		fori(j, 2, 11) {
			if(is_prime(eval(i, j))) {
				deu_bom = false;
				break;
			}
		}
		if(deu_bom) {
			coins.push_back(i);
		}
	}

	cout << "Case #" << kase++ << ":" << '\n';
	for(auto &each : coins) {
		string s = to_bin(each);
		cout << s;
		fori(i, 2, 11) {
			ll val = eval(each, i);
			for(ll j = 2; j * j <= val; j++) {
				if(val % j == 0) {
					cout << " " << j;
					break;
				}
			}
		}
		cout << '\n';
	}

	return 0;
}
