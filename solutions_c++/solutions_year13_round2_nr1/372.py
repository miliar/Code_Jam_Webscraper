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

long long motes[200];

void solve() {
  long long a;
  int n;
  scanf("%lld%d", &a, &n);
  for (int i = 0; i < n; ++i) {
    scanf("%lld", motes + i);
  }
  sort(motes, motes + n);
  int i = 0;
  int r = 10000000;
  int t = 0;
  while (i < n) {
    for (; i < n && motes[i] < a; ++i) {
      a += motes[i];
    }
    if (i < n) {
      r = min(r, t + n - i);
      if (a == 1) {
        t = r; 
        break;
      }
      while (a <= motes[i]) {
        ++t;
        a += a - 1;
      }
    }
  }
  r = min(r, t);
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
