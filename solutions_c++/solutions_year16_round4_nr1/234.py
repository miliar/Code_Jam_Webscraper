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
int const N = 211111;
ll const mod = 1000000007LL;

int a[15][1<<15];
char sp[11];
char ans[N];
int main() {
	a[0][0] = 0;
	for (int i = 0; i <= 12; ++i) {
		int mx = 1 << i;
		for (int j = 0; j < mx; ++j) {
			a[i+1][j*2] = a[i][j];
			a[i+1][j*2+1] = (a[i][j] + 1) % 3;
		}
	}

	freopen("A-large.in", "r", stdin);
	freopen("A-large-ans", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		int n, r, p, s; scanf("%d%d%d%d", &n, &r, &p, &s);
		int c[3]; rep(i, 3) c[i] = 0;
		for (int i = 0; i < (1 << n); ++i) {
			c[a[n][i]]++;
		}
		bool f = 0;
		if (c[0] == r && c[1] == s && c[2] == p) {
			sp[0] = 'R', sp[1] = 'S', sp[2] = 'P';
		} else if (c[0] == s && c[1] == p && c[2] == r) {
			sp[0] = 'S', sp[1] = 'P', sp[2] = 'R';
		} else if (c[0] == p && c[1] == r && c[2] == s) {
			sp[0] = 'P', sp[1] = 'R', sp[2] = 'S';
		} else f = 1;
		if (f) printf("Case #%d: IMPOSSIBLE\n", ca++);
		else {
			rep(i, 1 << n) ans[i] = sp[a[n][i]];
			ans[1<<n] = 0;
			int lev = 2, w = 1 << n;
			for (int i = n; i > 0; --i) {
				for (int j = 0; j < w; j += lev) {
					bool b = 0;
					int s1 = j, s2 = j + lev / 2;
					rep(k, lev / 2) {
						if (ans[s1 + k] > ans[s2 + k]) {
							b = 1; break;
						}
					}
					if (b) {
						rep(k, lev / 2) swap(ans[s1 + k], ans[s2 + k]);
					}
				}
				lev *= 2;
			}
			printf("Case #%d: %s\n", ca++, ans);
		}
	}
	return 0;
}

