#include <cstdio>
#include <iostream>
#include <ctime>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>

using namespace std;

typedef long long int int64;
typedef long double ext;

int tests;

const int maxw = 110;
const int maxh = 510;
const int maxv = 1000000;

const int inf = 1000000000;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

int w, h, b;
bool river[maxw][maxh];
int vcnt;
bool was[maxv];

struct edge{
  int u, v, f, c;
};

vector<edge> g;
vector<int> net[maxv];


inline int getnum(int x, int y) {
  return 1 + 2 * x * h + 2 * y;
}

void print(int u) {
  if (u == 0)
    cerr << "Source ";
  else if (u == vcnt - 1) {
    cerr << "Target ";    
  }
  else {
    cerr << "(" << ((u - 1) / 2) / h << ", " << ((u - 1) / 2) % h << ") ";
  }
  
}

void add_edge(int u, int v, int c) {
  
  //cerr << u << " --> " << v << "\n";
  edge e;
  e.u = u;
  e.v = v;
  e.c = c;
  e.f = 0;
  g.push_back(e);
  net[u].push_back(g.size() - 1);
  
  swap(e.u, e.v);
  e.c = 0;
  g.push_back(e);
  net[v].push_back(g.size() - 1);
}


int dfs(int u, int f) {
  if (u == vcnt - 1) {
    //print(u);
    return f;
  }
  was[u] = true;
  for (int i = 0; i < int(net[u].size()); i++) {
    int x = net[u][i];
    int v = g[x].v;
    if (was[v])
      continue;
    int nf = min(f, g[x].c - g[x].f);
    if (nf == 0)
      continue;
    int d = dfs(v, nf);
    if (d > 0) {
      g[x].f += d;
      g[x ^ 1].f -= d;
      //print(u);
      return d;
    }
  }
  return 0;  
}


int main() {
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
  scanf("%d", &tests);
  for (int test = 0; test < tests; test++) {
    printf("Case #%d: ", test + 1);
    scanf("%d %d %d", &w, &h, &b);
    for (int i = 0; i < w; i++) {
      for (int j = 0; j < h; j++) {
        river[i][j] = true;
      }
    }
    for (int i = 0; i < b; i++) {
      int x1, y1, x2, y2;
      scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
      for (int x = x1; x <= x2; x++)
        for (int y = y1; y <= y2; y++) {
          river[x][y] = false;
        }
    }
    vcnt = 2 * h * w + 2;
    for (int i = 0; i < vcnt; i++)
      net[i].clear();
    g.clear();
    for (int i = 0; i < w; i++)
      for (int j = 0; j < h; j++) {
        if (!river[i][j])
          continue;
        int u = getnum(i, j);
        int v = u + 1;
        add_edge(u, v, 1);        
      }
    for (int i = 0; i < w; i++) {
      if (river[i][0]) {
        int u = getnum(i, 0);
        add_edge(0, u, 1);
      }
      if (river[i][h - 1]) {
        int u = getnum(i, h - 1) + 1;
        add_edge(u, vcnt - 1, 1);       
      }
    }
    
    for (int i = 0; i < w; i++) {
      for (int j = 0; j < h; j++) {
        if (!river[i][j])
          continue;
        int u = getnum(i, j) + 1;
        for (int k = 0; k < 4; k++) {
          int ni = i + dx[k];
          int nj = j + dy[k];
          if (ni < 0 || ni >= w || nj < 0 || nj >= h)
            continue;
          if (!river[ni][nj])
            continue;
          int v = getnum(ni, nj);
          add_edge(u, v, 1);
        }
      }
    }
    cerr << "Vcnt = " << vcnt << "\n";      
    int res = 0;
    for (int i = 0; i < vcnt; i++)
      was[i] = false;
    while (dfs(0, inf)) {      
      res++;
      for (int i = 0; i < vcnt; i++)
        was[i] = false;
    }    
    printf("%d\n", res);
  }
  return 0;
}