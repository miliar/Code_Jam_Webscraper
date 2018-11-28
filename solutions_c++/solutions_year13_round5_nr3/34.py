#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define M 30
#define N 30
#define inf 1<<30
struct Node{
    int f, t, d;
}e[M];
int dis[N], next[M], point[N], q[N], cnt[N], ne;
bool u[N];
void init(){
    memset(point, -1, sizeof(point));
    ne = 0;
}
void add_edge(int f, int t, int d){
    e[ne].f = f, e[ne].t = t, e[ne].d = d;
    next[ne] = point[f], point[f] = ne++;
}
bool spfa(int s, int n){
    int i, f, r, tmp;
    for(i = 0; i < n; ++i) {
        dis[i] = inf;
        u[i] = false;
        cnt[i] = 0;
    }
    dis[s] = 0;
    q[0] = s;
    cnt[s] = 1;
    u[s] = true;
    f = 0, r = 1;
    while(f != r) {
        tmp = q[f];
        f = (f + 1) % (n + 1);
        u[tmp] = false;
        for(i = point[tmp]; i != -1; i = next[i]) {
            if(dis[e[i].t] > dis[e[i].f] + e[i].d) {
                dis[e[i].t] = dis[e[i].f] + e[i].d;
                if(!u[e[i].t]) {
                    ++cnt[e[i].t];
                    if(cnt[e[i].t] > n)
                        return false;
                    u[e[i].t] = true;
                    q[r] = e[i].t;
                    r = (r + 1) % (n + 1);
                }
            }
        }
    }
    return true;
}
struct abc{
    int x, y, a, b;
}c[2010];
int b[510];
int f0[40], f1[40];
int uu[510];
int main(){
    int T, ri = 1, n, m, p, i;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d", &n, &m, &p);
        int sum = 0;
        init();
        for (i = 0; i < m; i++){
            scanf("%d%d%d%d", &c[i].x, &c[i].y, &c[i].a, &c[i].b);
            c[i].x--;
            c[i].y--;
            add_edge(c[i].x, c[i].y, c[i].b);
        }
        for (i = 0; i < p; i++){
            uu[i] = 0;
            scanf("%d", &b[i]);
            b[i]--;
            sum += c[b[i]].a;
            add_edge(c[b[i]].x, c[b[i]].y, c[b[i]].a);
        }
        spfa(0, n);
        if (dis[1] == sum){
            printf("Case #%d: Looks Good To Me\n", ri++);
            continue;
        }
        for (int k = 0; k < (1<<m); k++){
            init();
            for (i = 0; i < m; i++){
                if (k & (1<<i)) add_edge(c[i].x, c[i].y, c[i].a);
                else add_edge(c[i].x, c[i].y, c[i].b);
            }
            spfa(0, n);
            for (i = 0; i < n; i++){
                f0[i] = dis[i];
            }
            init();
            for (i = 0; i < m; i++){
                if (k & (1<<i)) add_edge(c[i].y, c[i].x, c[i].a);
                else add_edge(c[i].y, c[i].x, c[i].b);
            }
            spfa(1, n);
            for (i = 0; i < n; i++){
                f1[i] = dis[i];
            }
            int ss = 0;
            for (i = 0; i < p; i++){
                if (k & (1<<b[i])) ss += c[b[i]].a;
                else ss += c[b[i]].b;
                int d = ss + f1[c[b[i]].y];
                if (d == f0[1]) uu[i] = 1;
            }
        }
        for (i = 0; uu[i]; i++);
        printf("Case #%d: %d\n", ri++, b[i] + 1);
    }
    return 0;
}
