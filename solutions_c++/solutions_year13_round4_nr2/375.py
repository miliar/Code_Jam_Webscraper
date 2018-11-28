#ifdef SHTRIX 
#include "/Users/roman/Dev/SharedCpp/DebugOutput.h"
#endif
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <memory>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())

map<ll, ll> cache_min[51], cache_max[51];

ll minpos(ll x, int n) {
	if (cache_min[n].find(x) != cache_min[n].end()) return cache_min[n][x];
	if (!x) return cache_min[n][x] = 0;
	if (x == (1LL << n) - 1) return cache_min[n][x] = (1LL << n) - 1;
	return cache_min[n][x] = minpos(x / 2 + (x % 2 > 0), n - 1);
}

ll maxpos(ll x, int n) {
	//cerr << x << " " << n << endl;
	if (cache_max[n].find(x) != cache_max[n].end()) return cache_max[n][x];
	if (!x) return cache_max[n][x] = 0;
	if (x >= (1LL << n) - 1) 
		return cache_max[n][x] = (1LL << n) - 1;
	return cache_max[n][x] = maxpos((x - 1) / 2, n - 1) + (1LL << (n - 1));
}

ll n, p;

inline void solve(int case_id) {
    cin >> n >> p;

	ll x = 0, y = 0;
	ll l = 0, r = 1LL << n;
	while (r - l > 1) {
		ll tt = (l + r) / 2;
		if (maxpos(tt, n) < p) {
			l = tt;
		} else {
			r = tt;
		}
	}
	x = l;
	l = 0; r = 1LL << n;
	while (r - l > 1) {
		ll tt = (l + r) / 2;
		if (minpos(tt, n) < p) {
			l = tt;
		} else {
			r = tt;
		}
	}
	y = l;
	// for (ll i = 0; i < 1LL << n; i++) {
	// 	cerr << i << " minpos: " << minpos(i, n) << " maxpos: " << maxpos(i, n) << endl;
	// }
    printf("Case #%d: %lld %lld\n", case_id, x, y);
}

int main()
{
    freopen("input.txt","rt",stdin);
	int TC; scanf("%d", &TC); rep(tc, TC) solve(tc);
    return 0;
}
