/*
	C++ Competitive Programming Template
	Author: Kendrick Timothy B. Mercado (mightymercado / Proficient)
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
#define forr(i, j, n) 	for (int i = j; i < n; i++)
#define ford(i, j, n)	for (int i = n - 1; i >= j; i--)
#define forn(i, n)		forr(i,0,n)
#define fornd(i, n)		ford(i,0,n)
#define fill(a,v)		memset(a, v, sizeof(a))
#define zero(a) 		fill(a, 0)
#define initdp(a)		fill(a, -1)
#define all(x)			(x).begin(), (x).end()
#define mp 				make_pair
#define pb 				pb
const int MOD = 1e9+7;
const double PI = acos(-1);
ll negmod(ll n, ll m = MOD) {
	ll r = n % m;
	return r < 0 ? r + m : r;
}
ll modpow(ll n, ll p, ll m = MOD) {
	ll r = 1;
	n %= m;
	while (p) {
		if (p & 1) r = r * n % m;
		n = n * n % m;
		p >>= 1;
	}
	return r;
}

int main() {
	int t;
	string s;
	cin >> t;
	forn(tc, t) {
		cin >> s;
		int flips = 0;
		char last = '?';
		forn(i, s.size()) {
			if (s[i] == '-') {
				
				if (last == '+') {
					while (s[i+1] == '-') {
						i++;
					}
					flips += 2;
					last = '+';
				} else if (i == s.size() - 1) {
					flips++;
				} else {
					last = '-';
				}
			} else if (s[i] == '+') {
				if (last == '-') {
					flips++;
					last = '+';
				} else {
					last = '+';
				}
			}
		}
		printf("Case #%d: %d\n", tc+1, flips);
	}
}