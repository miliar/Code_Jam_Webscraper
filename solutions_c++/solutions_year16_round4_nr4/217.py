#include <bits/stdc++.h>
#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define FOR(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
#define RD(x) scanf("%d", &x)
#define PB push_back
#define MP make_pair
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
int const N = 30;
ll const mod = 1000000007LL;
char g[N][N];
int a[N][N], b[N][N];
int n;
void fl(int msk) {
	rep(i, n) rep(j, n) {
		b[i][j] = msk >> (i * n + j) & 1;
	}
}

int lim;
bool vis[10];
bool dfs(int d, vector<int> v, int fb) {
	if (d == lim) return 1;
	rep(i, n) if (i != fb) {
		if (!vis[i] && b[v[d]][i]) {
			vis[i] = 1;
			if (dfs(d + 1, v, fb)) return 1;
			vis[i] = 0;
		}
	}
	return 0;
}

bool fd(vector<int>v, int fb) {
	rep(i, n) vis[i] = 0;	
	lim = v.size();
	if (dfs(0, v, fb)) return 0;
	return 1;
}

bool ck() {
	//rep(i,n){
		//rep(j,n)printf("%d",b[i][j]);
		//puts("");
	//}
	rep(i, n) {
		vector<int> v; v.clear();
		rep(j, n) if (b[j][i]) v.push_back(j);
		if (v.size() == 0) return 0;
		if (!fd(v, i)) return 0;
	}
	return 1;
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-ans", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		rep(i, n) scanf(" %s", g[i]);
		rep(i, n) rep(j, n) a[i][j] = (g[i][j] == '1') ? 1 : 0;
		int msk = 0; rep(i, n) rep(j, n) if (a[i][j]) msk |= (1 << (i * n + j));
		int m = 1 << (n * n);
		int ans = inf;
		rep(i, m) if (!(i & msk)) {
			int tmsk = i | msk;
			fl(tmsk);	
			if (ck()) {
				ans = min(ans, __builtin_popcount(i));
			}
		}	
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}


