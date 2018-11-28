#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <utility>
#include <cstdlib>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <memory.h>
#include <ctime>
#include <cctype>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long double ld;
typedef long long ll;
typedef unsigned char uc;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;

const ld pi = 3.141592653589793238462643l;

const ll mod = 1000002013;

vector<pair<int, int> > v;

ll n;

ll cst (ll st, ll fn, ll cnt) {
	return (((fn - st) * (n * 2 - (fn - st - 1)) / 2) % mod * cnt) % mod;
}

void solve () {
	int m;
	cin >> n >> m;
	ll ans = 0;
	v.clear();
	forn (i, m) {
		int st, fn, cnt;
		cin >> st >> fn >> cnt;
		(ans += cst(st, fn, cnt)) %= mod;
		v.pb(mp(st, -cnt));
		v.pb(mp(fn, cnt));
	}
	sort(all(v));
	while (v.size()) {
		int s = -v[0].sc;
		int i = 0;
		int mn = 2000000000;
		while (s) {
			mn = min(mn, s);
			s -= v[++i].sc;
		}
		(ans += mod - cst(v[0].fs, v[i].fs, mn)) %= mod;
		v[0].sc += mn;
		v[i].sc -= mn;
		if (!v[i].sc) {
			v.erase(v.begin() + i);
		}
		if (!v[0].sc) {
			v.erase(v.begin());
		}
	}
	cout << ans << endl;
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);	
	int t;
	cin >> t;
	forn (i, t) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
