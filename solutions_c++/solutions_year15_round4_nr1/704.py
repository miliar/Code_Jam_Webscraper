#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cassert>

#define REP(i, a, b) for (int i = (a), _end_ = (b); i < _end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define EXIT(...) printf(__VA_ARGS__), exit(0)
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

using namespace std;

const int maxn = 100, maxm = 100;

int T;
int n, m;
char g[maxn + 5][maxm + 5];

int walk[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int ty[256];

inline bool in(const int &x, const int &y) { return x >= 0 && x < n && y >= 0 && y < m; }

inline bool ok(const int &x, const int &y, const int &k, const bool &first = 1)
{
	if (!in(x, y)) return 0;
	if (!first && g[x][y] != '.') return 1;
	return ok(x + walk[k][0], y + walk[k][1], k, 0);
}

int main()
{
	ty[int('>')] = 0;
	ty[int('<')] = 1;
	ty[int('v')] = 2;
	ty[int('^')] = 3;
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		scanf("%d%d", &n, &m);
		REP(i, 0, n) scanf("%s", g[i]);
		int ans = 0;
		REP(i, 0, n)
			REP(j, 0, m)
				if (g[i][j] != '.' && !ok(i, j, ty[int(g[i][j])]))
				{
					++ans;
					REP(k, 0, 4)
						if (ok(i, j, k)) goto lyc;
					goto yyt;
lyc:;
				}
		printf("%d\n", ans);
		continue;
yyt:;
		printf("IMPOSSIBLE\n");
	}
	return 0;
}
