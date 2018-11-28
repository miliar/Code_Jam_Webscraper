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

static const int N = 1000;

void solve() {
  char pancakes[N];
  scanf("%s", pancakes);
  int n = strlen(pancakes);
  pancakes[n] = '+';
  int res = 0;
  for (int i = 1; i <= n; ++i) {
    res += pancakes[i] != pancakes[i-1];
  }
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
