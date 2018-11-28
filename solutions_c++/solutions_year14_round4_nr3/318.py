#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int DinicN = 1010 * 2010 * 2;
const int DinicM = DinicN * 8;
int oo = 1<<30;
struct Dinic{   //先init,再add加边,调用calc计算
    int n, S, T, m;
    int head[DinicN], dis[DinicN], l[DinicN], work[DinicN];
    int point[DinicM], next[DinicM], flow[DinicM], capa[DinicM];
    void init(int _n, int _S, int _T){ //节点数,源,汇
        n = _n; S = _S; T = _T; m = 0;
        memset(point, -1, sizeof(point));
        for (int i = 0; i < n; i++) head[i] = -1;
    }
    void add(int u, int v, int c1, int c2){    //起点,终点,正向流量,反向流量
        //printf("add %d->%d: %d %d\n", u, v, c1, c2);
        point[m] = v; capa[m] = c1; flow[m] = 0; next[m] = head[u]; head[u] = m++;
        point[m] = u; capa[m] = c2; flow[m] = 0; next[m] = head[v]; head[v] = m++;
    }
    bool bfs(){
        memset(dis, -1, sizeof (dis));
        int w = 0; l[w++] = S; dis[S] = 0;
        for (int r = 0; r < w; r++)
            for (int x = l[r], i = head[x]; i >= 0; i = next[i])
                if (flow[i] < capa[i] && dis[point[i]] < 0) {
                    dis[point[i]] = dis[x] + 1;
                    l[w++] = point[i];
                }
        return dis[T] >= 0;
    }
    int dfs(int x, int exp){
        if (x == T || exp == 0) return exp;
        for (int &i = work[x]; i >= 0; i = next[i]){
            int v = point[i], tmp;
            if (flow[i] < capa[i] && dis[v] == dis[x] + 1 && (tmp = dfs(v, min(exp, capa[i] - flow[i])))){
                flow[i] += tmp; flow[i ^ 1] -= tmp; return tmp;
            }
        }
        return 0;
    }
    int calc(){
        int re = 0, t;
        while (bfs()){
            for (int i = 0; i < n; i++) work[i] = head[i];
            while ((t = dfs(S, oo)) > 0) re += t;
        }
        return re;
    }
}sol;
const int DiscreteN = 2010;
struct Discrete{    //先init,之后add数,add完调用discretize,最后query,离散后为[1,size]
    int t[DiscreteN], size;
    void init(){ size = 0; }
    void add(int x){ t[size++] = x; }
    void discretize(){ sort(t, t + size); size = unique(t, t + size) - t; }
    int query(int x){ return lower_bound(t, t + size, x) - t; }
}dct;
struct abc{
    int x0, y0, x1, y1;
}c[1010];
int u[1010][2010];
int main(){
    int T, ri = 1, n, m, K, i, j, k;
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d", &n, &m, &K);
        for (i = 0; i < K; i++){
            scanf("%d%d%d%d", &c[i].x0, &c[i].y0, &c[i].x1, &c[i].y1);
        }
        int ss = n * m * 2, tt = n * m * 2 + 1;
        sol.init(n * m * 2 + 2, ss, tt);
        for (i = 0; i < n; i++){
            sol.add(ss, (i * m + 0) * 2, 1, 0);
            sol.add((i * m + m - 1) * 2 + 1, tt, 1, 0);
        }
        for (i = 0; i < n; i++){
            for (j = 0; j < m; j++){
                u[i][j] = 0;
            }
        }
        for (k = 0; k < K; k++){
            for (i = c[k].x0; i <= c[k].x1; i++){
                for (j = c[k].y0; j <= c[k].y1; j++){
                    u[i][j] = 1;
                }
            }
        }
        for (i = 0; i < n; i++){
            for (j = 0; j < m; j++){
                if (u[i][j]) continue;
                sol.add((i * m + j)* 2, (i * m + j) * 2 + 1, 1, 0);
                if (i + 1 < n && u[i + 1][j] == 0){
                    sol.add((i * m + j) * 2 + 1, ((i + 1) * m + j) * 2, 1, 0);
                    sol.add(((i + 1) * m + j) * 2 + 1, (i * m + j) * 2, 1, 0);
                }
                if (j + 1 < m && u[i][j + 1] == 0){
                    sol.add((i * m + j) * 2 + 1, (i * m + j + 1) * 2, 1, 0);
                    sol.add((i * m + j + 1) * 2 + 1, (i * m + j) * 2, 1, 0);
                }
            }
        }
        printf("Case #%d: %d\n", ri++, sol.calc());
    }
    return 0;
}
