#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cassert>
#include <utility>
#include <algorithm>

using namespace std;

const int MAXN = 1024;
const int MAXM = 2013;
const int INF = 1000000007;

struct Edge {
  int u, v, a, b;
  int id;
} edge[MAXM];

vector<pair<int, int> > e[MAXN];
int w[MAXN][MAXN];

void floyd(int n) {
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        w[i][j] = min(w[i][j], w[i][k] + w[k][j]);
      }
    }
  }
}

bool test(int i, int j) {
  return ((i >> j) & 1) != 0;
}

int main() {
  int re;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    int n, m, p;
    vector<int> path;

    scanf("%d%d%d", &n, &m, &p);
    for (int i = 0; i < m; ++i) {
      scanf("%d%d%d%d", &edge[i].u, &edge[i].v, &edge[i].a, &edge[i].b);
      --edge[i].u;
      --edge[i].v;
      edge[i].id = -1;
    }
    path.resize(p);
    for (int i = 0; i < p; ++i) {
      scanf("%d", &path[i]);
      --path[i];
      edge[path[i]].id = i;
    }

    int ans = -1;
    for (int i = 0; i < (1 << m); ++i) {
      for (int j = 0; j < n; ++j) {
        fill(w[j], w[j] + n, INF);
        w[j][j] = 0;
      }
      for (int j = 0; j < m; ++j) {
        int& k = w[edge[j].u][edge[j].v];
        k = min(k, test(i, j) ? edge[j].a : edge[j].b);
      }
      floyd(n);
      int d = 0;
      for (int j = 0; j < p; ++j) {
        d += test(i, path[j]) ? edge[path[j]].a : edge[path[j]].b;
        if (w[0][1] < d + w[edge[path[j]].v][1]) {
          // printf("[%d][%d] %d %d %d\n", i, j, w[0][1], d,  w[edge[path[j]].v][1]);
          ans = max(ans, j);
          break;
        }
        if (j == p - 1) {
          ans = p;
          goto OUTPUT;
        }
      }
    }

OUTPUT:
    printf("Case #%d: ", ri);
    if (ans == p) {
      puts("Looks Good To Me");
    } else {
      printf("%d\n", path[ans] + 1);
    }
    fflush(stdout);
  }

  return 0;
}
