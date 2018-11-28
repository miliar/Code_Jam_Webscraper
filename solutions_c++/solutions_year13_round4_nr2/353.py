#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define ll long long

int t, n;
ll m, p;

bool worst(ll x) {
	ll num = 0;
	num = m - 1;
	ll pp = 1;
	forn(i, n) {
		if (pp - 1 >= x)
			break;
		num ^= (1ll << (n-1 - i));
		pp *= 2;
		pp++;
	}

	return (m - num) <= p;
}

bool best(ll x) {
	ll num = 0;
	ll pp = 1;
	forn(i, n) {
		if ((m - pp) <= x)
			break;
		num ^= (1ll << (n-1 - i));
		pp *= 2;
		pp++;
	}

	return (m - num) <= p;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cin >> t;
	forn(tt, t) {
		cin >> n >> p;
		m = (1ll << n);
		ll l = 0, r = m - 1;

		ll mint = -1;
		while (l <= r) {
			ll x = (l + r) >> 1;
			if (worst(x)) {
				mint = x;
				l = x + 1;
			} else
				r = x - 1;
		}

		ll maxt = -1;
		l = 0, r = m - 1;
		while (l <= r) {
			ll x = (l + r) >> 1;
			if (best(x)) {
				maxt = x;
				l = x + 1;
			} else
				r = x - 1;
		}

		cout << "Case #" << (tt + 1) << ": " << mint << " " << maxt << endl;
	}
	
	return 0;
}