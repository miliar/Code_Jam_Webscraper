/*
  Author : Enjoy
  Method : 网络流dinic，小俊姐的模板。
         maxflow()表示最大流算法。
         bfs()分层。
         dfs()非递归dfs。
         improve流量推进。
         oo是improve中需要的。 
         fs,ft表示源汇。n,m表示点数边数。flow表示最大流。ro[]表示容量，bj[]表示指向，h[]是距离，now[]是当前边，pre[]是表示由哪一个节点来的。
         qu[]是bfs队列。 
*/
#include<iostream>
#include<iomanip>
#include<math.h>
#include<stdlib.h>
using namespace std;
#define maxn 100000 + 10
#define maxm 1000000 + 10
#define intmax 99999999
int n, m, flow, oo, bs = 1, ft, fs, ro[maxm], bj[maxm], bi[maxm], di[maxn], pre[maxn], h[maxn], now[maxn], qu[1000000 + 10];

void add(int x, int y, int z)
{
     bj[++bs] = y; bi[bs] = di[x]; di[x] = bs; ro[bs] = z;
}

void improve()
{
     int x, zx;
     x = pre[ft]; zx = intmax;
     while (x)
     {
           if (ro[now[x]] <= zx) {zx = ro[now[x]]; oo = x;}
           x = pre[x];
     }
     x = pre[ft];
     while (x)
     {
           ro[now[x]] -= zx; ro[now[x] ^ 1] += zx;
           x = pre[x];
     }
     flow += zx;
}

void dfs()
{
     int i, x, y;
     bool can;
     for (i = 1; i <= n; i++) now[i] = di[i];
     x = fs; pre[x] = 0;
     while (x)
     {
           i = now[x]; can = false;
           while (i)
           {
                 if (ro[i])
                 {
                    y = bj[i];
                    if (h[y] == h[x] + 1) 
                    {
                       now[x] = i; pre[y] = x; x = y; can = true;
                       if (y == ft) {improve(); x = oo;}
                       break;  
                    }
                 }
                 i = bi[i];
           }
           if (can == false) {h[x] = -1; x = pre[x];}
     }
}

bool bfs()
{
     int i, he, ta, x, y;
     for (i = 1; i <= n; i++)  h[i] = -1;
     h[fs] = 1; qu[1] = fs; he = 0; ta = 1;
     while (he < ta)
     {
           x = qu[++he]; i = di[x];
           while (i)
           {
                 if (ro[i])
                 {
                    y = bj[i];
                    if (h[y] == -1) {h[y] = h[x] + 1; qu[++ta] = y;}
                    if (y == ft) return true;
                 }
                 i = bi[i];
           }
     }
     return false; 
}

void maxflow()
{
     flow = 0;
     while (bfs()) dfs();
}

bool bo[2000 + 10][2000 + 10];
int  W, H;
int tr(int x, int y)
{
    return (x - 1) * H + y;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int ts, ks,b;
    int x, y, x0, y0, x1, y1;
    int i, j;
    cin >> ts;
    for (ks = 0; ks < ts; ks++){
        cin >> W >> H >> b;
        memset(bo, true, sizeof(bo));
        for (i = 0; i < b; i++){
            cin >> x0 >> y0 >> x1 >> y1;
            x0++;y0++;x1++;y1++;
            for (x = x0; x <= x1; x++)
                for (y = y0; y <= y1; y++)
                    bo[x][y] = false;
        }
        
        fs = W * H * 2 + 1;
        ft = W * H * 2 + 2;
        n = ft;
        bs = 1;
        for (i = 0; i <= n; i++) di[i] = 0;
        int base =W * H;
        for (i = 1; i <= W; i++)
            for (j = 1; j <= H; j++)
                if (bo[i][j]){
                   add(tr(i, j), base + tr(i, j), 1);
                   add(base + tr(i, j), tr(i, j), 0);
                }
        for (i = 1; i <= W; i++)
            for (j = 1; j <= H; j++){
                if (i > 1){
                   add(base + tr(i, j), tr(i - 1, j), 1);
                   add(tr(i - 1, j), base + tr(i, j), 0);
                }
                if (i < W){
                   add(base + tr(i, j), tr(i + 1, j), 1);
                   add(tr(i + 1, j), base + tr(i, j), 0);
                }
                if (j > 1){
                   add(base + tr(i, j), tr(i, j - 1), 1);
                   add(tr(i, j - 1), base + tr(i, j), 0);
                }
                if (j < H){
                   add(base + tr(i, j), tr(i, j + 1), 1);
                   add(tr(i, j + 1), base + tr(i, j), 0);
                }
            }
        for (i = 1; i <= W; i++){
            add(fs, tr(i, 1), 1);
            add(tr(i, 1), fs, 0);
            add(base + tr(i, H), ft, 1);
            add(ft, base + tr(i, H), 0);
        }
        maxflow();
        printf("Case #%d: %d\n", ks + 1, flow);
    }
    
}
