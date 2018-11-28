#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <time.h>
#include <string>
#include<bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long ll;

ll multi(  ll a,   ll n,   ll m) {
	  ll res = 0;
	while (n) {
		if (n & 1) 
			res = (res + a) % m;
		a <<= 1;
		a %= m;
		n >>= 1;
	}
	return res;
}

ll power(ll a,ll n,ll m) {
	if (!n)
		return 1;
	ll u = power(a, n / 2, m)%m;
	u = multi(u, u, m);
	if (n & 1)
		return multi(u, a, m);
	return u;
}
bool primality(ll x) {
	if (x == 3 || x == 2)
		return true;
	for (int i = 0; i < 4; ++i) {
		  ll a = 2 + (  1ll*rand()*rand()) % (x - 3);
		if (power(a, x - 1, x) != 1)
			return false;
	}
	return true;
}
ll get(ll x, int b) {
	ll res = 0, cur = 1;
	while (x) {
		if (x & 1)
			res += cur;
		cur *= b;
		x >>= 1;
	}
	return res;
}
ll count(ll k) {
	int res = 0;
	while (k) {
		res++;
		k >>= 1;
	}
	return res;
}
ll fact(ll v) {
	for (ll i = 2; i < v; ++i)
		if (v%i == 0)
			return i;
	return -1;
}
string tobinary(ll v) {
	string res = "";
	while (v) {
		res += '0' + (v & 1);
		v >>= 1;
	}
	reverse(res.begin(), res.end());
	return res;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
#endif
	int n, c, t, cas = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d", &n, &c);
		set<ll> st;
		for (ll i = (1ll << (n - 2)); i < (1ll << (n - 1)); ++i) {
			ll k = (i << 1) | 1;
			bool ok = true;
			for (int j = 2; j <= 10; ++j) {
				if (primality(get(k, j))) {
					ok = false;
					break;
				}
			}
			if (ok) st.insert(k);
			if (st.size() == c)
				break;
		}
		printf("Case #%d:\n", cas++);
		for (auto v : st) {
			printf("%s", tobinary(v).c_str());
			for (int i = 2; i <= 10; ++i) {
				printf(" %lld", fact(get(v, i)));
			}
			puts("");
		}
	}
	return 0;
}