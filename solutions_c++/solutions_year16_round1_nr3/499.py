#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

static const int N = 1002;

int f[N];
int n;
int res;
int best[N];
int two[N];
int vis[N];

int isLeaf(int i) {
  for (int j = 0; j < n; ++j) {
    if (f[j] == i) return 0;
  }
  return 1;
}

int isCycle(int i) {
  int j = i;
  for (int l = 1; l < n + 2; ++l) {
    j = f[j];
    if (j == i) return l;
  }
  return 0;
}

void go(int i) {
  if (!isLeaf(i)) return;
  int j = i;
  best[i] = 0;
  for (int l = 1; l < n + 2; ++l) {
    if (vis[j] == i) return;
    vis[j] = i;
    int nj = f[j];
    if (f[nj] == j) {
      return;
    }
    j = nj;
    best[j] = max(best[j], l);
  }
}

void solve() {
  res = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", f + i);
    --f[i];
    best[i] = 0;
    vis[i] = N;
    two[i] = 0;
  }
  int r = 0;
  for (int i = 0; i < n; ++i) {
    int cl = isCycle(i);
    res = max(res, cl);
    if (cl == 2) {
      ++r;
      two[i] = 1;
    }
    if (!cl)
      go(i);
  }
  for (int i = 0; i < n; ++i) {
    if (two[i]) {
      r += best[i];
    }
  }
  res = max(res, r);
  printf("%d\n", res);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
