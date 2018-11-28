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
int const N = 211;
ll const mod = 1000000007LL;
double p[N], a[N];
double f[N][N];
double cal(int n) {
	rep(i, n + 1) rep(j, n + 1) f[i][j] = 0;
	f[0][0] = 1;
	rep(i, n) rep(j, n) if (f[i][j] > 0) {
		f[i+1][j] += f[i][j] * (1.0 - a[i]);
		f[i+1][j+1] += f[i][j] * a[i];
	}
	return f[n][n/2];
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large-ans", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		int n, k; scanf("%d%d", &n, &k);
		rep(i, n) scanf("%lf", &p[i]);
		sort(p, p + n);
		double ans = 0;
		rep(i, n) {
			rep(j, k + 1) {
				int m = 0;
				for (int l = 0; l < j; ++l) a[m++] = p[l];
				for (int l = 0; l < k - j; ++l) a[m++] = p[n - l - 1];
				ans = max(ans, cal(m));
			}
		}
		cerr<<T<<endl;
		printf("Case #%d: %.10lf\n", ca++, ans);
	}
	return 0;
}



