#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define MP make_pair

typedef double DB;
typedef long long LL;
typedef pair<int,int> PI;

const DB eps = 1e-6;
const int N = 500 * 300;
const int M = 500 * 200 * 8;
const int MOD = 1e9 + 7;
const int INF = 1e9 + 7;

struct Edge{
    int y, next, c;
} e[M];

int head[N], h[N], vh[N], tot, augc, now[N], found, flow, v[1000][1000], n, m;

void Addedge(int x, int y, int c){
    e[++tot].y = y; e[tot].c = c; e[tot].next = head[x]; head[x] = tot;
    e[++tot].y = x; e[tot].c = 0; e[tot].next = head[y]; head[y] = tot;
}

void Aug(int x, int st, int ed, int n){
    int p = now[x], minh = n - 1, augco = augc;
    if (x == ed){
        found = 1;
        flow += augc;
        return;
    }
    while (p != -1){
        if (e[p].c > 0 && h[e[p].y] + 1 == h[x]){
            augc = min(augc, e[p].c);
            Aug(e[p].y, st, ed, n);
            if (h[st] >= n) return;
            if (found) break;
            augc = augco;
        }
        p = e[p].next;
    }
    if (found){
        e[p].c -= augc;
        e[p ^ 1].c += augc;
    }else{
        p = head[x];
        while (p != -1){
            if (e[p].c > 0 && h[e[p].y] < minh){
                minh = h[e[p].y];
                now[x] = p;
            }
            p = e[p].next;
        }
        vh[h[x]] --;
        if (!vh[h[x]]) h[st] = n;
        h[x] = minh + 1;
        vh[h[x]] ++;
    }
}

int C(int x, int y){return x * n + y;}
int main(){
    int CAS, B;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++){
        scanf("%d%d%d", &n, &m, &B);
        memset(v, 0, sizeof(v));
        for (int i = 0; i < B; i++){
            int x, _x, y, _y;
            scanf("%d%d%d%d", &x, &y, &_x, &_y);
            for (int j = min(x, _x); j <= max(x, _x); j++)
            for (int k = min(y, _y); k <= max(y, _y); k++)
                v[k][j] = 1;
        }
        tot = -1, memset(head, -1, sizeof(head));
        int st = n * m * 2, ed = n * m * 2 + 1;
        for (int i = 0; i < n; i++){
            Addedge(st, i, 1);
            Addedge(n * m * 2 - i - 1, ed, 1);
        }
        for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
        if (!v[i][j]){
            Addedge(C(i, j), C(i, j) + n * m, 1);
            if (i) Addedge(C(i, j) + n * m, C(i - 1, j), 1);
            if (j) Addedge(C(i, j) + n * m, C(i, j - 1), 1);
            if (i < m - 1) Addedge(C(i, j) + n * m, C(i + 1, j), 1);
            if (j < n - 1) Addedge(C(i, j) + n * m, C(i, j + 1), 1);
        }
        memcpy(now, head, sizeof(head));
        memset(vh, 0, sizeof(vh));
        memset(h, 0, sizeof(h));
        n = ed + 1;
        vh[0] = n;
        flow = 0;
        while (h[st] < n){
            augc = INF;
            found = 0;
            Aug(st, st, ed, n);
        }
        printf("Case #%d: %d\n", cas, flow);
    }
}
