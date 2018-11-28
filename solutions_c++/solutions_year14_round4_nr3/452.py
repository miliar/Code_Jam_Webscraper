#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 100050;
int const M = 5000100;
int n, m;
struct edges{ int u, c, next; } e[M];
int p[N], idx;
void addedge(int u, int v, int c, int r = 0) {
	//printf("add(%d,%d)\n",u,v);
	e[idx].u = v, e[idx].c = c, e[idx].next = p[u], p[u] = idx++;
	e[idx].u = u, e[idx].c = r, e[idx].next = p[v], p[v] = idx++;
}
void init() { idx = 0; clr(p, 0xff); }
int gap[N], lev[N], cur[N], pre[N];
int sap(int s, int t) {
  clr(gap, 0), clr(lev, 0), memcpy(cur, p, sizeof p);
  int u, v, ret(0), step(inf), mi;
  gap[0] = n, u = pre[s] = s;
  while (lev[s] < n) { loop:
    for (int &i = cur[u]; ~i; i = e[i].next) {
      v = e[i].u;
      if (e[i].c && lev[u] == lev[v] + 1) {
        step = min(step, e[i].c);
        pre[v] = u;
        u = v;
        if (v == t) {
          while (v != s) {
            u = pre[v];
            e[cur[u]].c -= step;
            e[cur[u] ^ 1].c += step;
            v = u;
          }
          ret += step;
          step = inf;
        }
        goto loop;
      }
    }
    mi = n;
    for (int i = p[u]; ~i; i = e[i].next) {
      v = e[i].u;
      if (e[i].c && lev[v] < mi) {
        mi = lev[v];
        cur[u] = i;
      }
    }
    if (!--gap[lev[u]]) break;
    ++gap[lev[u] = mi + 1];
    u = pre[u];
  }
  return ret;
}
bool vis[505*505];
int dir[4][2] = {
	0, 1, 0, -1, 1, 0, -1, 0
};

int main() {
#if 1
	freopen("C-small-attempt1.in", "r", stdin);
	//freopen("C-large.in", "r", stdin);
	freopen("C-ans.txt", "w", stdout);
#endif
	int w, h, b;
	int T, ca = 1;
	for (scanf("%d", &T); T--; ) {
		cerr<<T<<endl;
		scanf("%d%d%d", &w, &h, &b);
		init(); clr(vis, 0);
		int x1, y1, x2, y2;
		rep(i, b) {
			scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
			for (int j = x1; j <= x2; ++j) for (int k = y1; k <= y2; ++k) {
				vis[j * w + k + 1] = 1;
				//cout<<j*w+k+1<<endl;
			}
		}
		n = w * h * 2 + 2; int S =  n - 1, P = n;
		int z = w * h;
		Rep(i, w * h) {
			if (!vis[i])
			addedge(i, i + z, 1);
		}
		rep(i, w) {
			int id = i + 1;
			if (!vis[id]) addedge(S, id, 1);
			id = (h - 1) * w + i + 1;
			if (!vis[id]) addedge(id + z, P, 1);
		}
		rep(i, h) rep(j, w) {
			int id = i * w + j + 1;
			if (!vis[id]) {
				rep(k, 4) {
					int tx = i + dir[k][0], ty = j + dir[k][1];
					if (tx >= 0 && tx < h && ty >= 0 && ty < w) {
						int id2 = tx * w + ty + 1;
						if (!vis[id2]) {
							addedge(id + z, id2, 1);
							addedge(id2 + z, id, 1);
						}
					}
				}
			}
		}
		int ret = sap(S, P);
		printf("Case #%d: %d\n", ca++, ret);
		cerr<<ret<<endl;
	}
	return 0;
}


