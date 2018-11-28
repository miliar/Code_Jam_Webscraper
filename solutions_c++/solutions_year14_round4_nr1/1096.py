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

const int N = 10020;
int tab[N];

void solve() {
  int n, x;
  scanf("%d%d", &n, &x);
  for (int i = 0; i < n; ++i) {
    scanf("%d", tab + i);
  }
  sort(tab, tab + n);
  int a, b;
  a = 0;
  b = n;
  int ret = 0;
  for (--b; b >= a; --b) {
    ++ret;
    if (tab[a] + tab[b] > x) {
      continue;
    }
    ++a;
  }
  printf("%d\n", ret);
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
