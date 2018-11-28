#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int a[1005];

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    printf("Case #%d: ", cc);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", a + i);
    }
    int ans_x = 0, mx = 0;
    for (int i = 1; i < n; ++i) {
      int diff = max(0, a[i - 1] - a[i]);
      ans_x += diff;
      mx = max(mx, diff);
    }
    int ans_y = 0;
    for (int i = 0; i < n - 1; ++i) {
      ans_y += min(a[i], mx);
    }
    printf("%d %d\n", ans_x, ans_y);
  }
  return 0;
}