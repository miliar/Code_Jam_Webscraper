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

bool solve(int x, int r, int c) {
  if ((r * c) % x) return false;
  switch (x) {
    case 1:
    return true;
    case 2:
    return c >= 2;
    case 3:
    return c >= 3 && r >= 2;
    case 4:
    return c >= 4 && r >= 3;
    default:
    return false;
  }
}

void solve() {
  int x, r, c;
  scanf("%d%d%d", &x, &r, &c);
  printf("%s\n", solve(x, min(r, c), max(r, c)) ? "GABRIEL" : "RICHARD");
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
