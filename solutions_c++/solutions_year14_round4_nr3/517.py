#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

const int maxs = 501;
const int inf = maxs * maxs * 5;
int F[maxs][maxs];

struct Edge
{
  int to;
  int cf;
  int bi;
};
vector<vector<Edge> > g;
void Init(int vn)
{
  g.assign(vn, vector<Edge>());
}

void addEdge(int u, int v, int cap = 1)
{
  Edge forw = {v, cap, sz(g[v])};
  Edge back = {u, 0, sz(g[u])};
  g[u].push_back(forw);
  g[v].push_back(back);
}
void addEdge2(int u, int v, int cap = 1)
{
  Edge forw = {v, cap, sz(g[v])};
  Edge back = {u, cap, sz(g[u])};
  g[u].push_back(forw);
  g[v].push_back(back);
}

vector<int> mark;
int dest = -1;
bool dfs(int v)
{
  if (v == dest)
    return true;
  mark[v] = true;

  for (auto& e : g[v])
    if (e.cf > 0 && !mark[e.to])
      if (dfs(e.to))
      {
        e.cf--;
        g[e.to][e.bi].cf++;
        return true;
      }
  return false;
}

void testCase()
{
  int w, h, b;
  scanf("%d%d%d", &w, &h, &b);

  memset(F, 0, sizeof(F));
  for (int i = 0; i < b; i++)
  {
    int l, b, r, t;
    scanf("%d%d%d%d", &l, &b, &r, &t);
    for (int y = b; y <= t; y++)
      for (int x = l; x <= r; x++)
        F[y][x] = 1;
  }

  int s = w * h * 2;
  int t = s + 1;
  int vn = t + 1;
  Init(vn);

  for (int x = 0; x < w; x++)
    if (!F[0][x])
      addEdge(s, 2 * (0 * w + x));
  for (int x = 0; x < w; x++)
    if (!F[h - 1][x])
      addEdge(2 * ((h - 1) * w + x) + 1, t);

  for (int y = 0; y < h - 1; y++)
    for (int x = 0; x < w; x++)
      if (!F[y][x] && !F[y + 1][x])
      {
        addEdge(2 * (y * w + x) + 1, 2 * ((y + 1) * w + x));
        addEdge(2 * ((y + 1) * w + x) + 1, 2 * (y * w + x));
      }

  for (int y = 0; y < h; y++)
    for (int x = 0; x < w - 1; x++)
      if (!F[y][x] && !F[y][x + 1])
      {
        addEdge(2 * (y * w + x) + 1, 2 * (y * w + x + 1));
        addEdge(2 * (y * w + x + 1) + 1, 2 * (y * w + x));
      }
  for (int y = 0; y < h; y++)
    for (int x = 0; x < w; x++)
      if (!F[y][x])
        addEdge(2 * (y * w + x), 2 * (y * w + x) + 1);

  int ans = 0;
  while (true)
  {
    dest = t;
    mark.assign(vn, 0);
    if (!dfs(s))
      break;
    ans++;
  }
  printf("%d\n", ans);
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
//  cin >> T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
