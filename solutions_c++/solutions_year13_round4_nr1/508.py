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

#define PIII pair<PII, int>
#define base 1000002013

multiset<PIII> S;
vector<PIII> ls;

int n, m, ntest;
ll origin, after;
ll res;

bool cmp(PIII a, PIII b) {
	return a.F.S > b.F.S;
}

ll calc(PIII a) {
	ll x = a.F.S - a.F.F;
	return (x * n - x * (x - 1)/2) * a.S;
}

void print(PIII P) {
	DEBUG(P.F.F);
	DEBUG(P.F.S);
	DEBUG(P.S);
}
void process() {
//	cerr << "START" << endl;
	while (!S.empty()) {
		__typeof(S.begin()) it = S.begin();
		PIII P = *it;
		S.erase(it);
		ls.clear();
		//print(P);		
		while (!S.empty()) {
			__typeof(S.begin()) it2 = S.begin();
			PIII P2 = *it2;
			if (P2.F.F > P.F.S) break;
			ls.PB(P2);
			S.erase(it2);		
		}
		sort(ls.begin(), ls.end(), cmp);
		REP(i, ls.size()) {
			PIII Q = ls[i];
			//print(Q);
			if (Q.F.F == P.F.F) {
				S.insert(Q);
				continue;
			}
			if (Q.F.S <= P.F.S) {
				FORN(j, i, ls.size()) S.insert(ls[j]);
				break;
			}
			if (P.S == 0) {
				FORN(j, i, ls.size()) S.insert(ls[j]);
				break;				
			}
			int d = min(P.S, Q.S);
			S.insert(MP(MP(P.F.F, Q.F.S), d));
			S.insert(MP(MP(Q.F.F, P.F.S), d));
			if (Q.S > d) {
				S.insert(MP(Q.F, Q.S - d));
			}
			P.S -= d;
		}
		//print(P);		
		if (P.S > 0) after = (after + calc(P)) % base;
		// DEBUG(S.size());
		//DEBUG(after);
	}
//	DEBUG(origin);
//	DEBUG(after);
	res = (origin - after + base) % base;
}

int main () {
	ios_base::sync_with_stdio(false);
	cin >> ntest;
	FOR(test, 1, ntest) {
		cin >> n >> m;
		after = origin = 0;
		FOR(i, 1, m) {
			int l, r, p;
			cin >> l >> r >> p;
			PIII P = MP(MP(l, r), p);
			origin = (origin + calc(P))%base;
			S.insert(MP(MP(l, r), p));

		}
		process();		
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}
			
