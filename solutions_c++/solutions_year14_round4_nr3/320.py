#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <queue>
#include <stack>
#define zero(x) (((x)>0?(x):-(x))<eps)
//#include <bits/stdc++.h>
#define mem(a,b) memset((a),(b),sizeof((a)))
#define lld long long
#define INF 0x3f3f3f3f
#define eps 1e-6

#define MAXV 160010
#define MAXE 3200100
#define INF 1000000000

using namespace std;

struct Edge {
    int u, v, flow, next;
} edge[MAXE];

int head[MAXV], nEdge;
int dis[MAXV], cur[MAXV];

int que[MAXV], front, tail;
int stk[MAXV], top;

void init() {
    memset(head, -1, sizeof(head));
    nEdge = 0;
}

void addEdge(int a, int b, int f) {
//    cout<<a<<"  "<<b<<"  "<<f<<endl;
    edge[nEdge].u = a;
    edge[nEdge].v = b;
    edge[nEdge].flow = f;
    edge[nEdge].next = head[a];
    head[a] = nEdge++;
    edge[nEdge].u = b;
    edge[nEdge].v = a;
    edge[nEdge].flow = 0;
    edge[nEdge].next = head[b];
    head[b]= nEdge++;
}

bool bfs(int src, int dst) {
    int i, p, cur;

    memset(dis, -1, sizeof(dis));
    front = tail = 0;
    dis[src] = 0;
    que[tail++] = src;
    while (front < tail) {
        cur = que[front++];
        for (i = head[cur]; ~i; i = edge[i].next) {
            if (edge[i].flow && dis[p = edge[i].v] < 0) {
                dis[p] = dis[cur] + 1;
                if (p == dst) return true;
                que[tail++] = p;
            }
        }
    }

    return false;
}

int dinic(int v, int src, int dst) {
    int i, x = src, p, nowFlow, totalFlow = 0;

    while (bfs(src, dst)) {
        top = 0;
        for (i = 0; i < v; ++i) cur[i] = head[i];
        while (1) {
            if (x == dst) {
                nowFlow = INF;
                for (i = 0; i < top; ++i) {
                    if (edge[stk[i]].flow < nowFlow) {
                        nowFlow = edge[stk[i]].flow;
                        p = i;
                    }
                }
                totalFlow += nowFlow;
                for (i = 0; i < top; ++i) {
                    edge[stk[i]].flow -= nowFlow;
                    edge[stk[i] ^ 1].flow += nowFlow;
                }
                top = p;
                x = edge[stk[top]].u;
            }

            for(i = cur[x]; ~i; i = edge[i].next) {
                if (edge[i].flow && dis[edge[i].v] == dis[x] + 1) break;
            }
            cur[x] = i;
            if (~i) {
                stk[top++] = i;
                x = edge[i].v;
            } else {
                if (!top) break;
                dis[x] = -1;
                x = edge[stk[--top]].u;
            }
        }
    }

    return totalFlow;
}

int num[109][509];
int W, H, B;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int getp1(int i, int j) {
    return i * H + j + 1;
}

int getp2(int i, int j) {
    return getp1(i, j) + W * H;
}

int MAIN() {
    scanf("%d%d%d", &W, &H, &B);
    init();
    mem(num, 0);
    int a, b, c, d;
    for(int i = 0; i < B; i++) {
        scanf("%d%d%d%d", &a, &b, &c, &d);
        for(int j = a; j <= c; j++) {
            for(int k = b; k <= d; k++) {
                num[j][k] = 1;
            }
        }
    }
    int src = 0;
    int dst = W * H * 2 + 1;
    for(int i = 0; i < W; i++) {
        if(num[i][0] == 0) {
            addEdge(src, getp1(i, 0), 1);
        }
        if(num[i][H - 1] == 0) {
            addEdge(getp2(i, H - 1), dst, 1);
        }
    }
    for(int i = 0; i < W; i++) {
        for(int j = 0; j < H; j++) {
            if(num[i][j] == 1) continue;
            int p1 = getp1(i, j);
            int p2 = getp2(i, j);
            addEdge(p1, p2, 1);
            for(int k = 0; k < 4; k++) {
                int ni = i + dx[k];
                int nj = j + dy[k];
                if(ni < 0 || ni >= W || nj < 0 || nj >= H) continue;
                if(num[ni][nj] == 1) continue;
                int pp1 = getp1(ni, nj);
                addEdge(p2, pp1, 1);
            }
        }
    }
    int ans = dinic(dst + 1, src, dst);
    printf("%d\n", ans);
    return 0;
}

int main() {
#ifdef LOCAL_TEST
    freopen("F:/ACMData.txt","r",stdin);
    freopen("F:/out1.txt","w",stdout);
#endif
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    while(cases--) {
        printf("Case #%d: ", cc++);
        MAIN();
    }
    return 0;
}
