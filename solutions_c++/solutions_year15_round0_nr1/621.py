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

char buffer[2000];

void solve() {
  int n;
  scanf("%d%s", &n, buffer);
  int ret = 0;
  int s = 0;
  for (int i = 0; i <= n; ++i) {
    if (s < i) {
      ret += i - s;
      s = i;
    }
    s += buffer[i] - '0';
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
