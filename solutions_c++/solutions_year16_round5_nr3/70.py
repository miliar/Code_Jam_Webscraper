#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define fi first
#define se second

const int maxn = 1010;

int n, s, q;
int x[maxn], y[maxn], z[maxn], vx[maxn], vy[maxn], vz[maxn];
int pa[maxn];
pair<double, pii> t[maxn*maxn];

inline int sqr(int a) { return a*a; }

inline int dst(int i, int j) {
	return sqr(x[i]-x[j]) + sqr(y[i]-y[j]) + sqr(z[i]-z[j]);
}

int fi(int a) {
	return pa[a] == a ? a : pa[a] = fi(pa[a]);
}

int uni(int a, int b) {
	pa[fi(a)] = fi(b);
}

void test() {
	q=0;
	scanf("%d%d", &n, &s);
	FOR(i,n) scanf("%d%d%d%d%d%d", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
	FOR(i,n) FOR(j,i) t[q++] = mp(dst(i,j), mp(i,j));
	FOR(i,n) pa[i]=i;
	sort(t,t+q);
	FOR(i,q) {
		uni(t[i].se.fi, t[i].se.se);
		if (fi(0) == fi(1)) {
			printf("%.6lf\n", sqrt(t[i].fi));
			return;
		}
	}
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	for (int i = 1; i <= ttn; i++) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
