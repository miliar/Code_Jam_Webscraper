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

const int ITER = 20000;
const int maxn = 111;

int n, m;
int p[maxn], w[maxn], L[7], res[7], N[maxn];
char s[maxn], t[7][maxn], r[maxn];
bool used[maxn];

bool fnd(int it) {
	FOR(i,n-L[it]+1) {
		bool ok=1;
		FOR(j,L[it]) if (t[it][j] != r[i+j]) {
			ok = false;
			break;
		}
		if (ok) return 1;
	}
	return 0;
}

void dfs(int u) {
	N[u] = 1;
	FORI(i,n) if (p[i]==u) {
		dfs(i);
		N[u] += N[i];
	}
}

void test() {
	scanf("%d", &n);
	FORI(i,n) scanf("%d", &p[i]);
	scanf("%s%d", s, &m);
	FOR(i,m) scanf("%s", t[i]);
	FOR(i,m) res[i]=0;
	FOR(i,m+1) for (L[i]=0; t[i][L[i]]; L[i]++) ;
	dfs(0);
	used[0] = 1;
	FOR(ii,ITER) {
		FORI(i,n) used[i]=0;
		FOR(jj,n) {
			int q = 0, Ntot = 0;
			FORI(i,n) if (!used[i] && used[p[i]]) {
				Ntot += N[i];
				w[q++] = i;
			}
			int x = rand() % Ntot, y = -1;
			FOR(i,q) {
				if (x < N[w[i]]) {
					y = w[i];
					break;
				}
				x -= N[w[i]];
			}
			used[y] = 1;
			r[jj] = s[y-1];
		}
		FOR(i,m) if (fnd(i)) res[i]++;
	}
	FOR(i,m) printf("%.2lf ", 1.0 * res[i] / ITER);
	printf("\n");
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
