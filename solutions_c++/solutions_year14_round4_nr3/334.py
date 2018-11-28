#pragma  comment(linker, "/STACK:36777216")
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define  lc(x) (x << 1)
#define  rc(x) (lc(x) + 1)
#define  lowbit(x) (x & (-x))
#define  PI    (acos(-1))
#define  lowbit(x) (x & (-x))
#define  EPS   1e-10
#define  MAXN  100055
#define  MAXM  1000005
#define  LL    long long
#define  DB    double
#define  ULL   unsigned long long
#define  INF   0x7fffffff
#define  pb    push_back
#define  mp    make_pair
#define  MOD   1000000007

using namespace std;

struct edge{
    int v, next, flow;
}e[MAXM];

int first[MAXN], level[MAXN], ecnt;

void addedge(int u, int v, LL flow){
    e[++ ecnt].next = first[u], first[u] = ecnt, e[ecnt].v = v, e[ecnt].flow = flow;
    e[++ ecnt].next = first[v], first[v] = ecnt, e[ecnt].v = u, e[ecnt].flow = 0;
}

bool make_level(int S, int T){
     memset(level, 0, sizeof(level));
     level[S] = 1;
     queue <int> Q;
     Q.push(S);
     while(!Q.empty()){
        int f = Q.front(); Q.pop();
        for(int i = first[f]; i != -1; i = e[i].next)
           if(e[i].flow && !level[e[i].v]){
              level[e[i].v] = level[f] + 1;
              Q.push(e[i].v);
              if(e[i].v == T) return true;
           }
     }
     return level[T];
}

int maxflow(int u, int T, int flow){
    if(u == T) return flow;
    int d, temp = 0;
    for(int i = first[u]; i != -1 && temp < flow; i = e[i].next)
       if(level[e[i].v] == level[u] + 1 && e[i].flow)
          if(d = maxflow(e[i].v, T, min(e[i].flow, flow - temp)))
             temp += d, e[i].flow -= d, e[i ^ 1].flow += d;
    if(!temp) level[u] = 0;
    return temp;
}

int ANS;

void Dinic(int S, int T){
     int d;
     while(make_level(S, T))
        while(d = maxflow(S, T, INF))
           ANS += d;
}


int d[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int t, cas, w, h, b, x_0[15], x_1[15], y_0[15], y_1[15], S, T, ID, in[105][505], out[105][505];

void getID(int &x){
    x = ++ ID;
}

bool check(int x, int y){
    if(x < 0 || y < 0) return false;
    if(x >= w || y >= h) return false;
    for(int i = 1; i <= b; i ++){
        if(x >= x_0[i] && x <= x_1[i] && y >= y_0[i] && y <= y_1[i]) return false;
    }
    return true;
}

int main(){
    //freopen("in.txt", "r", stdin);
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    cin >> t;
    while(t --){
        scanf("%d%d%d", &w, &h, &b);

        ID = 0, ANS = 0;
        memset(first, -1, sizeof(first)), ecnt = -1;
        memset(in, 0, sizeof(in)), memset(out, 0, sizeof(out));

        for(int i = 1; i <= b; i ++) scanf("%d%d%d%d", &x_0[i], &y_0[i], &x_1[i], &y_1[i]);

        getID(S), getID(T);
        for(int i = 0; i < h; i ++)
            for(int j = 0; j < w; j ++){
                if(check(j, i)){
                    getID(in[j][i]), getID(out[j][i]);
                    addedge(in[j][i], out[j][i], 1);
                }
            }

        for(int i = 0; i < h; i ++)
            for(int j = 0; j < w; j ++)
                if(check(j, i)){
                    for(int k = 0; k < 4; k ++){
                        int ii = i + d[k][0], jj = j + d[k][1];
                        if(check(jj, ii)){
                            addedge(out[j][i], in[jj][ii], 1);
                        }
                    }
                }
        for(int i = 0; i < w; i ++) if(check(i, 0)) addedge(S, in[i][0], 1);
        for(int i = 0; i < w; i ++) if(check(i, h - 1)) addedge(out[i][h - 1], T, 1);

        Dinic(S, T);

        printf("Case #%d: %d\n", ++ cas, ANS);
    }
}
