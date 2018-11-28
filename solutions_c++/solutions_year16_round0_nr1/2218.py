/*
	C++ Competitive Programming Template
	Author: Kendrick Timothy B. Mercado (mightymercado / Proficient)
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
#define forr(i, j, n) 	for (ll i = j; i < n; i++)
#define ford(i, j, n)	for (ll i = n - 1; i >= j; i--)
#define forn(i, n)		forr(i,0,n)
#define fornd(i, n)		ford(i,0,n)
#define fill(a,v)		memset(a, v, sizeof(a))
#define zero(a) 		fill(a, 0)
#define initdp(a)		fill(a, -1)
#define all(x)			(x).begin(), (x).end()
#define mp 				make_pair
#define pb 				pb
const ll MOD = 1e9+7;
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
	ll t, n, num, temp;
	bool marked[15];
	cin >> t;
	forn(tc, t) {
		cin >> n;
		if (n==0) {
			printf("Case #%lld: INSOMNIA\n", tc+1);
		} else {
			zero(marked);
			ll c = 0;
			num = 0;
			ll count = 0;
			while (c != 10) {
				count++;
				num+=n;
				temp = num;
				do {
					if (marked[temp%10] == false) c++;
					marked[temp%10] = true;
					temp/=10;
				} while (temp > 0);
			}
			printf("Case #%lld: %lld\n", tc+1, num);
		}
		
	}
}