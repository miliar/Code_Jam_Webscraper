#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef complex<double> cd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

#define rep(i, n) for(int i = 0; i < n; ++i)
#define ri(a) scanf("%d", &a)
#define rii(a, b) scanf("%d%d", &a, &b)
#define riii(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define rs(s) scanf("%s", s)
#define pi(n) printf("%d\n", n)
#define pia(a, n) rep(_, n) printf("%d%c", a[_], _ == n - 1 ? '\n' : ' ')
#define ria(a, n) rep(_, n) scanf("%d", &a[_])
#define Ttimes int T; ri(T); for(int ks = 1; ks <= T; ++ks)
#define PB push_back
#define MP make_pair

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
const int maxn = 100010;
const double eps = 1e-8;
char g[110][110];

int main() {
	Ttimes {
		int n, m; rii(n, m);
		rep(i, n) rs(g[i]);
		int ans = 0;
		bool fail = false;
		rep(i, n) {
			rep(j, m) {
				// printf("in %d %d\n", i, j);
				if(g[i][j] == '.') continue;
				int d;
				if(g[i][j] == '<') d = 3;
				else if(g[i][j] == '>') d = 1;
				else if(g[i][j] == 'v') d = 0;
				else d = 2;

				// printf("%c %d %d\n", g[i][j], dx[d], dy[d]);

				int x = i + dx[d], y = j + dy[d];
				bool f = false;
				while(x >= 0 && x < n && y >= 0 && y < m) {
					if(g[x][y] != '.') {
						f = true;
						break;
					}
					x += dx[d]; y += dy[d];
				}

				if(!f) {
					ans++;
					bool qq = false;
					for(int d = 0; d < 4; ++d) {
						int x = i + dx[d], y = j + dy[d];
						bool f = false;
						while(x >= 0 && x < n && y >= 0 && y < m) {
							if(g[x][y] != '.') {
								f = true;
								break;
							}
							x += dx[d]; y += dy[d];
						}
						if(f) {
							qq = true;
							break;
						}
					}
					if(!qq) {
						fail = true;
						break;
					}
				}
			}
			if(fail) break;
		}
		printf("Case #%d: ", ks);
		if(fail) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}

