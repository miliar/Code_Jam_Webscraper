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

void solve() {
  int n;
  int tab[1024];
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", tab + i);
  }
  int s1 = 0;
  for (int i = 1; i < n; ++i) {
    if (tab[i] < tab[i - 1]) s1 += tab[i - 1] - tab[i];
  }
  int p2 = 0;
  for (int i = 1; i < n; ++i) {
    p2 = max(tab[i - 1] - tab[i], p2);
  }
  int s2 = 0;
  for (int i = 0; i < n - 1; ++i) {
      s2 += min(p2, tab[i]);
  }
  printf("%d %d\n", s1, s2);
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
