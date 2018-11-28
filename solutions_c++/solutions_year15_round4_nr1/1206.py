#include <cstdio>
#define REP(i, a, b) for (int i = (a), _end_ = (b); i < _end_; ++i)
using namespace std;
const int maxn = 100;

int T;
int n, m;
char g[maxn + 5][maxn + 5];
int walk[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
int ty[256];

inline bool in(const int &x, const int &y) { return x >= 0 && x < n && y >= 0 && y < m; }

inline bool yes(const int &x, const int &y, const int &k, const bool &first = 1)
{
	if (!in(x, y)) return 0;
	if (!first && g[x][y] != '.') return 1;
	return yes(x + walk[k][0], y + walk[k][1], k, 0);
}

int main()
{
	ty['>'] = 0;ty['<'] = 1;ty['v'] = 2;ty['^'] = 3;
	scanf("%d", &T);
	for (int i = 1; i <= _; ++i)
	{
		printf("Case #%d: ", i);
		scanf("%d%d", &n, &m);
		REP(i, 0, n) scanf("%s", g[i]);
		int ans = 0;
		REP(i, 0, n)
			REP(j, 0, m)
				if (g[i][j] != '.' && !yes(i, j, ty[int(g[i][j])]))
				{
					++ans;
					REP(k, 0, 4)
						if (yes(i, j, k)) goto wrl;
					goto prime;
                    wrl:;
				}
		printf("%d\n", ans);
		continue;
        prime:;
		printf("IMPOSSIBLE\n");
	}
	return 0;
}
