// 1.设置上限MAXN和MAXN 2.初始化数值src, des, nNode 3.init_adj() & ex_addEdge() 4.dinic()
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
using namespace std;

const int MAXN=120000,MAXM=600000,INF = 0x3fffffff;

struct node {
	int v, next,flw;
} e[MAXM];

int eid, p[MAXN], lv[MAXN],src, des, nNode;

#define init_adj() (eid = 0,memset(p, -1, sizeof (p)))

void ex_addEdge(int u, int v, int c1, int c2) {
    e[eid].v = v;
    e[eid].flw = c1;
    e[eid].next = p[u];
    p[u] = eid++;

    e[eid].v = u;
    e[eid].flw = c2;
    e[eid].next = p[v];
    p[v] = eid++;
}

int bfs() {
    static int que[MAXN];
    int i, u, v, c, cur, f = 0, r = 1;
    memset(lv, 0, sizeof (lv));
    lv[src] = 1, *que = src;
    while (f < r) {
        cur = que[f++], f %= MAXN;
        for (i = p[cur]; ~i; i = e[i].next) {
            u = cur, v = e[i].v, c = e[i].flw;
            if (!lv[v] && c) {
                lv[v] = lv[u] + 1;
                que[r++] = v, r %= MAXN;
            }
        }
    }
    return lv[des];
}

int dfs() {
    static int tp[MAXN], stk[MAXN];
    memcpy(tp, p, sizeof (p));
    int cur, top = -1, flow = 0, u, v, i, part, ind;
    while (1) {
        if (top < 0) {
            for (i = tp[v = src]; ~i; i = e[i].next)
                if (e[i].flw && lv[e[i].v] == 2)
                    break;
            if (i == -1)
                break;
            stk[++top] = tp[src] = i;
        }
        if (e[cur = stk[top]].v != des) {
            u = e[cur].v;
            for (i = tp[u]; ~i; i = e[i].next)
                if (e[i].flw && lv[u] + 1 == lv[e[i].v])
                    break;
            if (~i)
                stk[++top] = tp[u] = i;
            else
                lv[u] = INF, --top;
        } else {
            for (part = INF, i = 0; i <= top; i++)
                if (e[stk[i]].flw < part)
                    part = e[stk[ind = i]].flw;
            flow += part;
            for (i = 0; i <= top; i++)
                e[stk[i]].flw -= part, e[stk[i]^1].flw += part;
            top = --ind;
        }
    }
    return flow;
}

int dinic() {
    int ans = 0, t;
    while (bfs())
        while (t = dfs())
            ans += t;
    return ans;
}

int w, h, b;
bool mp[1100][5100];
int idin[1100][5100];
int idout[1100][5100];
int s, t;
void read_data() {
    scanf("%d%d%d", &w, &h, &b);
    memset(mp, 0, sizeof(mp));
    int tmp = 2;
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++) {
            idin[i][j] = tmp;
            tmp++;
        }
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++) {
            idout[i][j] = tmp;
            tmp++;
        }
    s = 1;
    t = tmp;
    //cout << tmp << endl;

/*    for (int i = h - 1; i >= 0; i--) {
        for (int j = 0; j < w; j++) {
            printf("(%d, %d)  ", idin[j][i], idout[j][i]);
        }
        printf("\n");
    }*/

    for (int i = 0; i < b; i++) {
        int x0, y0, x1, y1;
        scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
        for (int x = x0; x <= x1; x++)
            for (int y = y0; y <= y1; y++) mp[x][y] = true;
    }
}

int main()
{
    int lt;
    scanf("%d", &lt);
    for (int num = 1; num <= lt; num++) {
        init_adj();
        read_data();
        for (int i = 0; i < w; i++)
            for (int j = 0; j < h; j++) if (!mp[i][j]) {
                if (j + 1 < h) ex_addEdge(idout[i][j], idin[i][j + 1], 1, 0);
                if (i + 1 < w) ex_addEdge(idout[i][j], idin[i + 1][j], 1, 0);
                if (j - 1 >= 0) ex_addEdge(idout[i][j], idin[i][j - 1], 1, 0);
                if (i - 1 >= 0) ex_addEdge(idout[i][j], idin[i - 1][j], 1, 0);
            }
        for (int i = 0; i < w; i++)
            for (int j = 0; j < h; j++) ex_addEdge(idin[i][j], idout[i][j], 1, 0);
        for (int i = 0; i < w; i++) ex_addEdge(s, idin[i][0], 1, 0);
        for (int i = 0; i < w; i++) if (!mp[i][h - 1]) ex_addEdge(idout[i][h - 1], t, 1, 0);
	src = s;
	des = t;
	nNode = t;
        int ans = dinic();
        printf("Case #%d: %d\n", num, ans);

    }
}


