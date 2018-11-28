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

int n;
int g[55][55], vis[55];
char s[55][55];
int wr[55], ma[55], ed[55];
pii parts[55];
int q;

map<pair<int, pii>, int> dp;

int rec(int mask, int x, int y) {
	if (mask == 0) return x;
	if (dp.find(mp(mask, mp(x,y))) != dp.end()) return dp[mp(mask, mp(x,y))];
	int res = 1e9;
	for (int m = mask; m; m = (m-1) & mask) {
		int A = 0, B = 0, S = 0;
		FOR(i,q) if (m&(1<<i)) {
			A += parts[i].fi;
			B += parts[i].se;
			S += parts[i].fi * parts[i].se;
		}
		int tx = x, ty = y;
		if (A > B) {
			ty -= A-B;
			B=A;
		}
		if (B > A) {
			tx -= B-A;
			A = B;
		}
		if (tx<0 || ty<0) continue;
		S = A*B-S;
		res = min(res, S + rec(mask ^ m, tx, ty));
	}
	return dp[mp(mask, mp(x,y))] = res;
}

void dfs(int u, int x) {
	vis[u] = x;
	FOR(i,2*n) if (g[u][i] && vis[i] == -1) dfs(i,x);
}

void test() {
	scanf("%d", &n);
	FOR(i,n) scanf("%s", s[i]);
	FOR(i,n) FOR(j,n) {
		g[i][j]=0; g[n+i][n+j]=0;
		g[i][n+j] = s[i][j]=='1';
		g[n+j][i] = s[i][j]=='1';
	}
	FOR(i,2*n) {
		vis[i]=-1;
		wr[i] = ma[i] = ed[i] = 0;
	}
	FOR(i,2*n) if (vis[i] == -1) dfs(i, i);
	FOR(i,n) {
		wr[vis[i]]++;
		ma[vis[n+i]]++;
		FOR(j,n) if (vis[i] == vis[n+j] && g[i][n+j]) ed[vis[i]]++;
	}
	int res = 0;
	vector<pii> v;
	q = 0;
	int x=0, y=0;
	FOR(i,2*n) {
		//printf("%d %d %d\n", wr[i], ma[i], ed[i]);
		res += wr[i]*ma[i]-ed[i];
		if (wr[i]==ma[i]) continue;
		if (wr[i]>0 && ma[i]>0) {
			parts[q++] = mp(wr[i], ma[i]);
		}
		if (wr[i]>0 && ma[i]==0) x++;
		if (wr[i]==0 && ma[i]>0) y++;
	}
	dp.clear();
	sort(parts, parts+q);
	printf("%d\n", res + rec((1<<q)-1, x, y));
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
