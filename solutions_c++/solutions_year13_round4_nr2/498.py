//written by HTTPs - Ho Sy Viet Anh
#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
 #include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
 #include <complex>

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
 #define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define sqr(x) ((x) * (x))
#define PB push_back
 #define MP make_pair
#define F first
#define S second
#define Aint(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define ll long long
#define PII pair <int, int>
#define VI vector<int>

using namespace std;

#define maxn 100011
#define oo 1000000000

int n;
ll rank;

bool chk1(ll p) {
	if (p == 0) return true;	
	p++;
	ll x = 0;
	FORD(i, 60, 0) if ((1ll << i) & p) {
		FORD(j, n - 1, n - i) {
			x = x | (1ll << j);
		}
		return x < rank;
	}
}

bool chk2(ll p) {
	if (p == 0) return true;
	p = (1ll << n) - p;
	ll x = 0;
	FORD(i, 60, 0) if ((1ll << i) & p) {
		FOR(j, 1, n - i) {
			x = x * 2 + 1;
		}
		return x < rank;
	}	
}

void process() {
	ll l = 0, r = (1ll << n) - 1, res;
	while (l <= r) {
		ll m = (l + r)/2;
		if (chk1(m)) {
			res = m;
			l = m + 1;
		} else r = m - 1;
	}
	cout << res << ' ';
	l = 0; r = (1ll << n) - 1;
	while (l <= r) {
		ll m = (l + r)/2;
		if (chk2(m)) {
			res = m;
			l = m + 1;
		} else r = m - 1;
	}
	cout << res << endl;
}

int main () {
	int ntest;
	cin >> ntest;
	FOR(test, 1, ntest) {
		cin >> n >> rank;
		cout << "Case #" << test << ": ";		
		process();
	}
	return 0;
}
			
