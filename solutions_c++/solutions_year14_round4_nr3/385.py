#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define ll long long
#define pb push_back 
#define mp make_pair
#define FOR(x, l, r) for(x = (l); x <= (r); x++)
#define FORD(x, r, l) for(x = (r); x >= (l); x --)
using namespace std;

int b[1000000], link[1000000], last[1000000];
int e[1000000], w[1000000], tt[1000000], nnxt[1000000], g[1000000], now[1000000], f[1000000], ff[1000000];
int flow, top, n, m, st, sw;
int ans;
void connect(int j, int k, int l)
{
   top ++;  e[top] = k;  w[top] = l;
   tt[top]  =  j;
   nnxt[top]  =  link[j];
   link[j] = top;
   top ++;  e[top] = j; w[top] = 0;
   tt[top] = k;
   nnxt[top] = link[k];
   link[k] = top;
}
int mpp[510][510];
void readin()
{
   int j, k, l, i, x0, y0, x1, y1, tp;
   int dx[5] = {0, 0, 0, -1, 1};
   int dy[5] = {0, -1, 1, 0, 0};
   cin >> n >> m >> tp;
   top = 1;
   st = 1; sw = n * m * 2 + 2; memset(mpp, 0, sizeof(mpp));
   for (i = 0; i <= sw; i ++) link[i] = 0;
   //connect(st, sw, 1);
   for (i = 1; i <= tp; i ++) {
   		cin >> x0 >> y0 >> x1 >> y1;
   		x0 ++; y0 ++; x1 ++; y1 ++;
   		for (j = x0; j <= x1; j ++)
   			for (k = y0; k <= y1; k ++)
   				mpp[j][k] = 1;
   }
   for (i = 1; i <= n; i ++) {
   		if (mpp[i][1] == 0) connect(st, i + 1, 1);
   		if (mpp[i][m] == 0) connect(n * (m - 1) + 1 + i + n * m, sw, 1);
   	}
   for (i = 1; i <= n; i ++)
   		for (j = 1; j <= m; j ++) connect((j - 1) * n + i + 1, (j - 1) * n + i + n * m + 1, 1);
   	for (i = 1; i <= n; i ++)
   		for (j = 1; j <= m; j ++) if (mpp[i][j] == 0){
   			for (k = 1; k <= 4; k ++) {
   				x1 = i + dx[k]; y1 = j + dy[k];
   				if (x1 < 1 || x1 > n || y1 < 1 || y1 > m) continue;
   				if (mpp[x1][y1] > 0) continue;
   				connect((j - 1) * n + 1 + i + n * m, (y1 - 1) * n + x1 + 1, 1);
   			}
   		}
   
}  
int bfs()
{
  int t, ww, q;
  for (t = 1; t <= sw; t ++) {
    f[t] = -1;
    now[t] = link[t];
    }
  t = 0; ww = 1;  b[ww] = st;
  f[st] = 1;
  while (t < ww) {
    t ++;  q = link[b[t]];
    while (q) {
      if (w[q] > 0 && f[e[q]] < 0) 
        {
          f[e[q]] = f[b[t]] + 1;
          if (e[q] == sw) return 1;
          ww ++; b[ww] = e[q];
        }
         q = nnxt[q];
      }
   }
  return 0;
}
int min(int a, int b) { return (a > b ? b : a); }
void dinic()
{
   int i, q, t;
   i = st;     ff[st] = 10000000;
   while (f[st] != -1)   {
    q = now[i];
    while (q)  if (w[q] > 0 && f[e[q]] - 1 == f[i]) break;
               else q = nnxt[q];
    if (q) {
     now[i] = q;  i = e[q]; g[e[q]] = q;
     ff[e[q]] = min(ff[tt[q]], w[q]);
     if (i == sw) {
         ans += ff[sw];
         while (i != st)
          {
           w[g[i]] -= ff[sw];
           w[g[i] ^ 1] += ff[sw];
           i = tt[g[i]];
          }
       }
   }
   else {
      f[i] = -1;
      i = tt[g[i]];
     }
   }
}
int main(){
  int tt, cas = 0;
  cin >> tt;
  while (tt --) {
  readin();
  ans = 0;
  while (bfs())  dinic();
  printf("Case #%d: ", ++cas);
  printf("%d\n", ans);
  }
}
