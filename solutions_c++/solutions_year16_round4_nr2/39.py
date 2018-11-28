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

const int maxn = 222;

double p[maxn], P[maxn];
double dp[maxn][maxn];

/*
double get(vi v) {
	int N = SZ(v);
	double res = 0;
	FOR(m,(1<<N)) if (__builtin_popcount(m) == N/2) {
		double cur = 1;
		FOR(i,N) {
			if (m & (1<<i)) cur *= p[v[i]];
			else cur *= 1. - p[v[i]];
		}
		res += cur;
	}
	return res;
}*/

void test() {
	int n,k;
	scanf("%d%d", &n, &k);
	FOR(i,n) scanf("%lf", &p[i]);
	/*
	double res = 0;
	FOR(m, (1<<n)) if (__builtin_popcount(m) == k) {
		vi v;
		FOR(i,n) if (m & (1<<i)) v.push_back(i);
		res = max(res, get(v));
	}
	*/
	double res1 = 0;
	sort(p,p+n);
	FOR(m, k+1) {
		FOR(i,m) P[i] = p[i];
		FOR(i,k-m) P[m+i] = p[n-1-i];
		FOR(i,k+2) FOR(j,k+2) dp[i][j] = 0;
		dp[0][0] = 1;
		FORI(i,k) FOR(s,i+1) {
			dp[i][s] += dp[i-1][s] * (1. - P[i-1]);
			if (s>0) dp[i][s] += dp[i-1][s-1] * P[i-1];
		}
		res1 = max(res1, dp[k][k/2]);
	}
	printf("%.7lf\n", res1);
	//printf("%.7lf %.7lf %s\n", res1, res, (fabs(res1-res)>1e-4 ? "ZLE!!!!!!" : " "));
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
