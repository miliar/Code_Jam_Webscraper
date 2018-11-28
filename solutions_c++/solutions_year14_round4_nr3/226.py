#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXW = 100;
const int MAXH = 500;
const int MAXN = MAXW * MAXH * 2 + 2;
const int MAXM = MAXN * 50;
const int inf = 0x3f3f3f3f;
struct Edge
{
  int to, next, flow, cost;
}edge[MAXM * 2];
int head[MAXN];
int N, L;
void init(int n)
{
  N = n;
  L = 0;
  memset(head, -1, 4 * n);
}
void add_edge(int u, int v, int cap, int rcap)
{
  edge[L].to = v;
  edge[L].flow = cap;
  edge[L].next = head[u];
  head[u] = L ++;
  edge[L].to = u;
  edge[L].flow = rcap;
  edge[L].next = head[v];
  head[v] = L ++;
}
int gap[MAXN];
int dis[MAXN], pre[MAXN], cur[MAXN];
int maxflow(int s, int t)
{
  memset(gap, 0, N * 4);
  gap[0] = N;
  memset(dis, 0, N * 4);
  for (int i = 0; i < N; ++ i)
    cur[i] = head[i];
  pre[s] = -1;
  int u = s, ret = 0;
  while (1)
  {
    if (u == t)
    {
      int flow = inf;
      for (int i = pre[t]; i != -1; i = pre[edge[i ^ 1].to])
        flow = min(flow, edge[i].flow);
      for (int i = pre[t]; i != -1; i = pre[edge[i ^ 1].to])
      {
        edge[i].flow -= flow;
        edge[i ^ 1].flow += flow;
      }
      ret += flow;
      u = s;
      continue;
    }
    bool flag = 0;
    for (int i = cur[u]; i != -1; i = edge[i].next)
    {
      int v = edge[i].to;
      if (edge[i].flow && dis[v] + 1 == dis[u])
      {
        cur[u] = pre[v] = i;
        u = v;
        flag = 1;
        break;
      }
    }
    if (!flag)
    {
      cur[u] = head[u];
      int mins = N;
      for (int i = head[u]; i != -1; i = edge[i].next)
        if (edge[i].flow)
          mins = min(mins, dis[edge[i].to] + 1);
      if (mins != dis[u])
      {
        if (mins == N || gap[dis[u]] == 1)
          return ret;
        --gap[dis[u]];
        ++gap[dis[u] = mins];
      }	
      if (u != s)
        u = edge[pre[u] ^ 1].to;
    }
  }	
  return ret;
}

const int step[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
int id[MAXW][MAXH][2];
bool mp[MAXW][MAXH];
int W, H, B;

bool ck(int x, int y) {
  return 0 <= x && x < W && 0 <= y && y < H;
}

int main() {
  int totCas;
  scanf("%d", &totCas);
  for (int cas = 1; cas <= totCas; cas++) {
    scanf("%d%d%d", &W, &H, &B);
    memset(mp, false, sizeof(mp));
    for (int i = 0; i < B; i++) {
      int X0, Y0, X1, Y1;
      scanf("%d%d%d%d", &X0, &Y0, &X1, &Y1);
      for (int x = X0; x <= X1; x++) {
        for (int y = Y0; y <= Y1; y++) {
          mp[x][y] = true;
        }
      }
    }

//    for (int i = 0; i < W; i++) {
//      for (int j = 0; j < H; j++) {
//        printf("%d", mp[i][j]);
//      }
//      printf("\n");
//    }

    int cnt = 0;
    for (int i = 0; i < W; i++) {
      for (int j = 0; j < H; j++) {
        id[i][j][0] = cnt++;
        id[i][j][1] = cnt++;
      }
    }
    int S = cnt++;
    int T = cnt++;
    init(cnt);
    for (int i = 0; i < W; i++) {
      if (mp[i][0] == false) {
        add_edge(S, id[i][0][0], 1, 0);
      }
      if (mp[i][H - 1] == false) {
        add_edge(id[i][H - 1][1], T, 1, 0);
      }
    }

    for (int i = 0; i < W; i++) {
      for (int j = 0; j < H; j++) {
        if (mp[i][j] == false) {
          add_edge(id[i][j][0], id[i][j][1], 1, 0);
          for (int d = 0; d < 4; d++) {
            if (ck(i + step[d][0], j + step[d][1])) {
              if (mp[i + step[d][0]][j + step[d][1]] == false) {
                add_edge(id[i][j][1], id[i + step[d][0]][j + step[d][1]][0], 1, 0);
              }
            }
          }
        }
      }
    }

    printf("Case #%d: %d\n", cas, maxflow(S, T));
  }
  return 0;
}

