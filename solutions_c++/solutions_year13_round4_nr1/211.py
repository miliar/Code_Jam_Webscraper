#pragma comment(linker, "/STACK:67108864")

#include <iostream>
#include <fstream> 
#include <cstdio>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <complex>
#include <bitset>
#include <map>
#include <set>
#include <ctime>

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for(int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for(int i = (int)(n) - 1; i >= (int)(k); i--)

#define vi vector<int>
#define pii pair<int, int>
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;

const long double pi = 3.1415926535897932384626433832795;
const long double eps = 0.000000001;
const int INF = 1E9;
const int MAXN = 100500;
const ll MOD = 1000002013;

int t;
int n, m, cr, ost;
vector<pair<pii, int> > a;
vector<pair<pii, int> > w;
ll nn, num, val;
ll a1, a2, ans;
stack<pii> lib;
pii cps;

inline ll cntval(ll x) {
	ll res = 1ll * x * n - (x - 1) * x / 2;
	res %= MOD;
	return res;
}

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	forn(tt, t) {
		scanf("%d%d", &n, &m);
		a.clear();
		w.clear();
		a.resize(m);
		
		a1 = 0;
		forn(i, m) {
			scanf("%d%d%d", &a[i].ff.ff, &a[i].ff.ss, &a[i].ss); 
			nn = a[i].ff.ss - a[i].ff.ff;
			num = a[i].ss;
			val = (cntval(nn) * num) % MOD;
			a1 = (a1 + val) % MOD;
			w.pb(mp(mp(a[i].ff.ff, 0), a[i].ss));
			w.pb(mp(mp(a[i].ff.ss, 1), a[i].ss));
		}

		sort(all(w));
		a2 = 0;
		forn(i, w.size()) {
			if (w[i].ff.ss == 0)
				lib.push(mp(w[i].ff.ff, w[i].ss));
			else {
				ost = w[i].ss;
				while (ost > 0) {
					cps = lib.top();
					lib.pop();

					cr = cps.ss;
					nn = w[i].ff.ff - cps.ff;
					if (ost - cr < 0) {
						num = ost;
						lib.push(mp(cps.ff, cr - ost));
						ost = 0;
					} else {
						num = cr;
						ost -= cr;
					}

					val = (cntval(nn) * num) % MOD;
					a2 = (a2 + val) % MOD;
				}
			}
		}

		ans = (MOD + a1 - a2) % MOD;
		printf("Case #%d: %lld\n", tt + 1, ans);
	}

	return 0;
}