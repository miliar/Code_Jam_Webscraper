#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
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

map<ll, ll> a;


ll mod = 1000002013;

ll len(ll x) {
	if (x < 2)
		return 0;
	return ((x - 1) * 1ll * (x - 0) / 2) % mod;
}

ll st[12345];

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	forn(tt, t) {
		ll res = 0;
		ll res2 = 0;
		int n, m;
		cin >> n >> m;
		vector<pair<pair<ll, int>, ll> > v;
		v.clear();
		a.clear();
		forn(i, m) {
			ll o, e, p;
			cin >> o >> e >> p;
			res2 = (res2 + (((e - o) * n) % mod) * 1ll * p) % mod;
			res2 = (res2 - (p * len(e - o)) % mod + mod) % mod;
			v.pb(mp(mp(o, -1), p));
			v.pb(mp(mp(e, +1), p));
		}

		sort(all(v));
		
		ll sts = 0;
		forn(i, v.size()) {
			ll j = v[i].first.first;
			if (v[i].first.second < 0) {
				if (sts == 0 || st[sts - 1] != j)
					st[sts++] = j;
				a[j] += v[i].second;
			} else {
				ll p = v[i].second;
				while(p > 0) {
					if (sts <= 0)
						cerr << "palevo!\n";

					ll c = st[sts - 1];
					ll cnt = a[c];
					if (cnt <= 0){
						sts--;
						continue;
					}

					if (cnt > p)
						cnt = p;

					cnt %= mod;
					res = (res + (((j - c) * n)%mod) * 1ll * cnt) % mod;
					res = (res - (cnt * len(j - c)) % mod + mod) % mod;
					a[c] -= cnt;
					p -= cnt;
				}
			}
		}
		cout << "Case #" << (tt + 1) << ": " << ((res2-res+mod)%mod) << endl;
	}
	
	return 0;
}