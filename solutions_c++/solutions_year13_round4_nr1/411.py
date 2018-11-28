#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

typedef long long ll;

int N, M;
#define MOD 1000002013ll

ll extended_eculdien(ll a, ll b, ll& x, ll& y) {
	ll nx = 0, ny = 1, r, tmp;
	x = 1;
	y = 0;
	while (b) {
		r = a / b;
		tmp = a - b * r;
		a = b;
		b = tmp;
		tmp = x - nx * r;
		x = nx;
		nx = tmp;
		tmp = y - ny * r;
		y = ny;
		ny = tmp;
	}
	return a;
}
ll modInv(ll a, ll mod) {
	ll x, y;
	extended_eculdien(a, mod, x, y);
	return ((x % mod) + mod) % mod;
}

ll calc2(ll d) {
	ll res = d;
	res %= MOD;
	res *= (d + 1);
	res %= MOD;
	res *= modInv(2, MOD);
	res %= MOD;
	return res;
}

ll calc(ll dist) {
	return ((calc2(N) - calc2(N - dist)) % MOD + MOD) % MOD;
}

int main() {
#ifndef ONLINE_JUDGE
//	freopen("1.in", "rt", stdin);
	freopen("2/A-large.in", "rt", stdin);
	freopen("2/A-large.out", "wt", stdout);
#endif
	int n;
	cin >> n;
	for (int tt = 0; tt < n; ++tt) {
//		cerr << tt << endl;
		cout << "Case #" << tt + 1 << ": ";
//		cout << 6 << " " << (6*modInv(2, MOD))%MOD << endl;

		cin >> N >> M;
		vector<ll> s(M), e(M), c(M);
		vector < pair<ll, ll> > ev;
		ll res2 = 0;
		for (int i = 0; i < M; ++i) {
			cin >> s[i] >> e[i] >> c[i];
			ev.push_back(make_pair(s[i]-1, -c[i]));
			ev.push_back(make_pair(e[i]-1, c[i]));
			res2 += calc(e[i]-s[i]) * c[i];
			res2 %= MOD;
		}
		sort(ev.begin(), ev.end());
		vector < pair<ll, ll> > available;
		ll res = 0;
		for (int i = 0; i < ev.size(); ++i) {
			if (ev[i].second > 0) { // leave
				ll toLeave = ev[i].second;
				while (toLeave > 0) {
					ll curT = available.back().first;
					ll curS = available.back().second;
					res += calc(ev[i].first - curT) * min(curS, toLeave);
					res %= MOD;
					if (toLeave >= curS)
						available.pop_back();
					else
						available.back().second -= toLeave;
					toLeave -= curS;
				}
			} else { // enter
				available.push_back(make_pair(ev[i].first, -ev[i].second));
			}
		}
		cout << ((((res2-res)%MOD)+MOD)%MOD) << endl;
	}
	return 0;
}
