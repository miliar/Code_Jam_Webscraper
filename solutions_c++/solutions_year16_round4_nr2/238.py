#include<time.h>
#include<stdlib.h>
#include<assert.h>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<set>
#include<map>
#include<queue>
#include<bitset>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define rep(i,l,r) for(int i=l;i<r;i++)
#define abs(x) ((x)<(0)?(-x):(x))
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x.size()))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define de(x) cout << #x << " = " << x << endl;
#define local(x) freopen(x".in", "r", stdin);
#define setIO(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout);
const int N = 2e2 + 7;
const int INF = 2e9 + 7;
const int MOD = 1e9 + 7;
const ll LINF = 1e17 + 7;
const double Pi = acos(-1.);
const double EPS = 1e-9;
int n, m;
double ans, p[N], f[N][N];
int main() {
	setIO("B-large");
	int T, tt = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		rep(i,0,n)
			scanf("%lf", &p[i]);
		sort(p, p + n);
		ans = 0;
		for (int l = 0; l <= m; ++l) {
			f[0][0] = 1.0;
			for (int i = 1; i <= l; ++i) {
				for (int j = 0; j <= i; ++j) {
					f[i][j] = f[i - 1][j] * (1. - p[i - 1]);
					if (j > 0)
						f[i][j] += f[i - 1][j - 1] * p[i - 1];
				}
			}
			for (int i = l + 1; i <= m; ++i) {
				for (int j = 0; j <= i; ++j) {
					f[i][j] = f[i - 1][j] * (1. - p[n - (i - l)]);
					if (j > 0)
						f[i][j] += f[i - 1][j - 1] * p[n - (i - l)];
				}
			}
			ans = max(ans, f[m][m >> 1]);
		}
		printf("Case #%d: %.10lf\n", ++tt, ans);
	}
	return 0;
}
