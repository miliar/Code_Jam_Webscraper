//============================================================================
// Author       : LAM PHAN VIET - lamphanviet@gmail.com
// Problem Name : 
// Time Limit   : .000s
// Description  : 
//============================================================================
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 100111
#define mod 1000002013

struct Segment {
	int lo, hi, p;
	Segment() {}
	Segment(int _lo, int _hi, int _p) {
		lo = _lo;
		hi = _hi;
		p = _p;
	}
	bool operator < (const Segment &a) const {
		if (lo == a.lo) return hi < a.hi;
		return lo < a.lo;
	}
};
int n, m;
vector<Segment> a;

int64 get(int64 dist) {
	int64 res = (n * dist) % mod;
	res -= ((dist * (dist - 1)) / 2) % mod;
	res %= mod;
	if (res < 0) res += mod;
	return res;
}

int64 getCost() {
	int64 res = 0;
	rep(i, a.size()) {
		res += (get(a[i].hi - a[i].lo) * a[i].p) % mod;
		res %= mod;
	}
	return res;
}

void process() {
	bool stop;
	sort(all(a));
	do {
		stop = true;
		m = a.size();
		rep(i, m) {
			/*for (int j = i + 1; j < m && a[i].p; j++) if (a[j].p) {
				if (a[j].lo <= a[i].hi && a[i].lo != a[j].lo && a[i].hi < a[j].hi) {
					maxDist = max(maxDist, a[j].hi - a[i].lo);
					stop = false;
				}
			}*/
			for (int j = i + 1; j < m && a[i].p; j++) if (a[j].p) {
				//if (a[j].lo <= a[i].hi && a[i].lo != a[j].lo && a[i].hi < a[j].hi && maxDist != a[j].hi - a[i].lo) {
				if (a[j].lo <= a[i].hi && a[i].lo != a[j].lo && a[i].hi < a[j].hi) {
					//printf("%d %d: %d %d %d | %d %d %d\n", i, j, a[i].lo, a[i].hi, a[i].p, a[j].lo, a[j].hi, a[j].p);
					int p = min(a[i].p, a[j].p);
					a.pb(Segment(a[i].lo, a[j].hi, p));
					a[i].p -= p; a[j].p -= p;
					if (a[j].p == 0) {
						a[j].p = p;
						a[j].hi = a[i].hi;
					}
					else if (a[i].p == 0) {
						a[i].p = p;
						a[i].lo = a[j].lo;
					}
					stop = false;
				}
			}
		}
		//rep(i, a.size()) printf("%d: %d %d %d\n", i, a[i].lo, a[i].hi, a[i].p);
		sort(all(a));
		if (a[0].p > 0 && a[0].lo < a[0].hi) m = 1;
		else m = 0;
		fr(i, 1, a.size() - 1) {
			if (a[m - 1].lo == a[i].lo && a[m - 1].hi == a[i].hi)
				a[m - 1].p += a[i].p;
			else if (a[i].p > 0 && a[i].lo < a[i].hi) a[m++] = a[i];
		}
		a.resize(m);
	} while (!stop);
	//rep(i, a.size()) printf("%d: %d %d %d\n", i, a[i].lo, a[i].hi, a[i].p);
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("Asmall.inp", "r", stdin);
		freopen("Asmall.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d %d", &n, &m);
		a.resize(m);
		rep(i, m) scanf(" %d %d %d ", &a[i].lo, &a[i].hi, &a[i].p);
		int64 c1 = getCost();
		process();
		int64 c2 = getCost();
		//cout << c1 << " " << c2 << endl;
		printf("Case #%d: ", ++caseNo);
		cout << (((c1 - c2) % mod) + mod) % mod << endl;
	}
	return 0;
}
