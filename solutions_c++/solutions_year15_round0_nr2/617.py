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

const int M = 1024;
int plate[M];

void solve() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", plate + i);
  }
  int r = M;
  for (int p = 1; p < M; ++p) {
    int t = p;
    for (int i = 0; i < n; ++i) {
      t += (plate[i] - 1) / p;
    }
    r = min(r, t);
  }
  printf("%d\n", r);
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
