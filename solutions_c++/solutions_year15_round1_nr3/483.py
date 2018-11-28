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

inline long long sig(int x0, int y0, int x1, int y1, int x, int y) {
  long long dx = x0 - x1;
  long long dy = y0 - y1;
  return dx * (y - y1) - dy * (x - x1);
}

int n;
int px[4000];
int py[4000];

void solve() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d%d", px + i, py + i);
  }
  if (n < 4) {
    for (int i = 0; i < n; ++i) {
      printf("0\n");
    }
    return;
  }
  
  for (int i = 0; i < n; ++i) {
    int r = n;
    for (int j = 0; j < n; ++j) {
      if (i == j) continue;
      int a = 0;
      int b = 0;
      for (int k = 0; k < n; ++k) {
        if (k == i) continue;
        if (k == j) continue;
        long long t = sig(px[i], py[i], px[j], py[j], px[k], py[k]);
        if (t < 0) ++a;
        if (t > 0) ++b;
      }
      r = min(r, min(a, b));
    }
    printf("%d\n", r);
  }
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d:\n", tc);
    solve();
  }
  return 0;
}
