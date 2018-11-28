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

static const int N = 2501;
int cnt[N];

void solve() {
  int n;
  for (int i = 0; i < N; ++i) cnt[i] = 0;
  scanf("%d", &n);
  for (int i = 0; i < 2 * n - 1; ++i) {
    for (int j = 0; j < n; ++j) {
      int h;
      scanf("%d", &h);
      ++cnt[h];
    }
  }
  for (int i = 0; i < N; ++i) {
    if (cnt[i] & 1) {
      printf(" %d", i);
    }
  }
  printf("\n");
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
