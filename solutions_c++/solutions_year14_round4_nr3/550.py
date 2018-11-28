#include <algorithm>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>

#define clr(a,b) memset(a,b,sizeof(a))
#define cpy(a,b) memcpy(a,b,sizeof(a))
#define rep(i,n) for(int i=0; i<n; i++)

using namespace std;

inline int LL(int x) { return x<<1; }
inline int RR(int x) { return x<<1|1; }

#define lson l, m, LL(rt)
#define rson m+1, r, RR(rt)

const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = 1e20;

inline bool eq(double x, double y) {
    return fabs(x - y) < eps;
}

const int INF = 0x3f3f3f3f;

const int N = 500500*2;
const int E = N*4;

int nxt[E], v[E], w[E], h[N], el;

void initEdge() {
    clr(h, -1); el = 0;
}

void addEdge(int x, int y, int z) {
    v[el] = y; w[el] = z; nxt[el] = h[x]; h[x] = el++;
    v[el] = x; w[el] = 0; nxt[el] = h[y]; h[y] = el++;
}

int dis[N], que[N], cur[N];

bool bfs(int s, int t) {
    int p, q;
    clr(dis, -1); dis[s] = 0;
    for(que[p=q=0]=s; p<=q; ++p) {
        int & x = que[p];
        for(int i=h[x]; ~i; i=nxt[i]) {
            int & y = v[i];
            if(w[i] && dis[y] == -1) {
                que[++q] = y;
                dis[y] = dis[x] + 1;
                if(y == t) return true;
            }
        }
    }
    return false;
}

int dfs(int x, int t, int f) {
    if(x == t) return f;
    int lf = f;
    for(int &i=cur[x]; ~i; i=nxt[i]) {
        int & y = v[i];
        if(dis[y] == dis[x] + 1 && w[i]) {
            int tmp = dfs(y, t, min(f, w[i]));
            w[i] -= tmp; w[i^1] += tmp; f -= tmp;
            if(!f) break;
        }
    }
    return lf - f;
}

int dinic(int s, int t) {
    int ret = 0;
    while(bfs(s, t)) {
        memcpy(cur, h, sizeof(cur));
        ret += dfs(s, t, INF);
    }
    return ret;
}

char mm[550][110];

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int T, cas(0);
    scanf("%d", &T);
    while(T--) {
        int w, h, b;
        scanf("%d%d%d", &w, &h, &b);
        clr(mm, 0);
        for(int i=0; i<b; i++) {
            int x0, y0, x1, y1;
            scanf("%d%d%d%d", &y0, &x0, &y1, &x1);
            for(int x=x0; x<=x1; x++) {
                for(int y=y0; y<=y1; y++) {
                    mm[x][y] = 1;
                }
            }
        }
        int N = w * h;
        int s = (w * h)*2;
        int t = s + 1;
        initEdge();
        for(int i=0; i<w; i++) addEdge(s, i, 1);
        for(int i=0; i<w; i++) addEdge(N+((h-1)*w+i), t, 1);
        for(int i=0; i<h-1; i++) {
            for(int j=0; j<w; j++) {
                if(!mm[i][j] && !mm[i+1][j]) {
                    addEdge(N+(i*w+j), (i+1)*w+j, 1);
                    addEdge(N+((i+1)*w+j), i*w+j, 1);
                }
            }
        }
        for(int i=0; i<h; i++) {
            for(int j=0; j<w-1; j++) {
                if(!mm[i][j] && !mm[i][j+1]) {
                    addEdge(N+(i*w+j), i*w+j+1, 1);
                    addEdge(N+(i*w+j+1), i*w+j, 1);
                }
            }
        }
        for(int i=0; i<h; i++) {
            for(int j=0; j<w; j++) {
                addEdge(i*w+j, N+(i*w+j), 1);
            }
        }
        printf("Case #%d: %d\n", ++ cas, dinic(s, t));
    }

    return 0;
}
