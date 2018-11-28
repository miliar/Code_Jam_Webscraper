#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <cfloat>
#define zero(x) (((x)>0?(x):-(x))<eps)

#define pause cout << " press ansy key to continue...",  cin >> chh
#define file_r(x) freopen(x,  "r",  stdin)
#define file_w(x) freopen(x,  "w",  stdout)
#define lowbit(x) ((x) & (-x))
#define repit(i, c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rep(i, n) for (int i = 0; i < (n); i++)
#define repe(i, u) for (int i = head[u]; i != -1; i = nxt[i])
#define repd(i, n) for (int i = (n - 1); i >= 0; i--)
#define FOR(i, n, m) for (int i = (n); i <= (m); i++)
#define FORD(i, n, m) for (int i = (n); i >= (m); i--)
#define pb push_back
#define X first
#define Y second
#define ins insert
#define rb rbegin
#define be begin
#define er erase
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define SZ(c) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define sqr(r) ((r) * (r))
#define dis(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))
#define FASTIO ios::sync_with_stdio(false);cin.tie(0)

#define sc(x) cout << #x" = " << x << endl, pause
#define sc2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl, pause
#define sc3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl, pause
#define sc4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl, pause

#define in(n) scanf("%d", &n)
#define in2(n, m) scanf("%d %d", &n, &m)
#define in3(x, y, z) scanf("%d %d %d", &x, &y, &z)

using namespace std;
int chh;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef pair<int, pii> pi3;
typedef vector< pair<int, int> > vpii;
typedef long long LL;

const int N = 32, M = 16;

int T, n, m, cnt;
int a[N], b[N];

LL cvt(int a[N], int idx) {
	LL ans = 0;
	rep (i, M) ans = ans * idx + a[i];
	return ans;
}

int gao(LL x, int idx) {
	int d, y;
	for (LL i = 2; i * i <= x; i++) {
		d = x % i, y = 1;
		rep (j, N - 1) y = y * idx % i;
		d = d + y;
		if (d % i) continue;
//		sc4(x, i, y, idx);
		return i;
	}
	return -1;
}

vi h;

void check() {
	bool flag;
	FOR (i, 2, 10) {
		int x = 0;
		rep (j, N) x = (x * i + b[j]) % h[i - 2];//, sc2(j, x);
		if (x == 0) cout << "mod " << i << " ok\n";
		else cout << "mod " << i << " fail " << x << '\n';
	}
}

void dfs(int id) {
	if (cnt == 500) return ;
	if (id == M - 2) {
		LL x;
		int y;
		h.clear();
		FOR (i, 2, 10) {
			x = cvt(a, i);
			y = gao(x, i);
			if (y == -1) return ;
			h.pb(y);
		}
		cnt++;
	//	printf("cnt= %d ", cnt);
		int e = 0;
		b[e++] = 1;
		rep (i, 31 - M) b[e++] = 0;
		rep (i, M) b[e++] = a[i];
		rep (i, e) printf("%d", b[i]);
		rep (i, 9) printf(" %d", h[i]);
		puts("");
//		check();
//		pause;
		return ;
	}
	a[id] = 0;
	dfs(id + 1);
	a[id] = 1;
	dfs(id + 1);
}

int main() {
	int cas = 0;
//	scanf("%d", &T);
//	while (T--) {
//		scanf("%d %d", &n, &m);
		m = 500;
		printf("Case #%d:\n", ++cas);
		cnt = 0;
		a[M - 1] = 1;
		dfs(0);
//	}
    return 0;
}
