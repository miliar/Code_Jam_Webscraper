#include <iostream>
#include <bitset>
#include <vector>
#include <cmath>
#include "infint.h"

using namespace std;

typedef long long ll;

bitset<1001001> bs;
vector<ll> v;
int cc = 0;

int pt(InfInt n) {
	for (int i = 0; i < v.size() && InfInt(v[i]) <= n.intSqrt(); i++) {
		if (n % v[i] == 0) return v[i];
	}
	return 0;
}

InfInt gt(ll v, ll b) {
	InfInt a = 0ll;
	InfInt c = 1ll;
	while (v > 0ll) {
		a += InfInt((v & 1ll)) * c;
		c *= b;
		v >>= 1ll;
	}
	return a;
}

void print(ll a) {
	string s = "";
	while (a > 0ll) {
		if (a & 1ll) {
			s += '1';
		} else {
			s += '0';
		}
		a >>= 1ll;
	}
	reverse(s.begin(), s.end());
	cout << s;
}

void sieve() {
	bs.reset();
	bs[0] = bs[1] = 1;
	for (ll i = 2; i <= 100; i++) {
		if (!bs[i]) {
			for (ll j = i*i; j <= 100; j+=i) {
				bs[j] = 1;
			}
			v.push_back(i);
		}
	}
}

void test(ll a) {
	vector<ll> v; bool no = false;
	for (ll i = 2; i <= 10; i++) {
		ll ans = pt(gt(a, i));
		if (ans == 0) { no = true; break; }
		else v.push_back(ans);
	}
	if (!no) {
		print(a);
		for (ll i = 0; i < v.size(); i++) {
			cout << " " << v[i];
		}
		cout << '\n';
		cc++;
	}
}

int main() {
	sieve();
	int t;
	cin >> t;
	while (t--) {
		ll n, j; cin >> n >> j;
		ll a = 0;
		a |= (1ll << (n-1));
		a |= 1;
		ll b = 0;
		cout << "Case #" << t+1 << ":\n";
		while (b < (1ll << (n-2))) {
			ll c = a + (b << 1);
			test(c);
			if (cc == j) break;
			b++;
		}
	}
}