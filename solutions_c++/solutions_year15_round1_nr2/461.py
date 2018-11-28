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

long long mb[1024];
int bn;

inline long long barber(size_t b, int i) {
  long long t = mb[b] * i;
  long long ret = i;
  for (size_t j = 0; j < b; ++j) {
    ret += t / mb[j] + 1;
  }
  for (size_t j = b + 1; j < (size_t)bn; ++j) {
    ret += (t + mb[j] - 1) / mb[j];
  }
//  printf("barber(%2d, %3d): %5lld\n", (int)b, i, ret);
  return ret;
}

bool checkBarber(size_t bi, long long n) {
    int a = -1; 
    int b = (int)n + 1;
    while (a + 1 < b) {
      int c = (a + b) / 2;
      long long m = barber(bi, c);
      if (m == n) return true;
      if (m < n) a = c;
      else b = c;
    }
    return false;
}

void solve() {
  int n;
  scanf("%d%d", &bn, &n);
  for (int i = 0; i < bn; ++i) {
    scanf("%lld", mb + i);
  }
  for (int i = 0; i < bn; ++i) {
    if (checkBarber(i, n - 1)) {
      printf("%d\n", i + 1);
      break;
    }
  }
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
