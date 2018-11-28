#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;
const int N = 100+5;
int s[N];
void solve() {
  int a, n;
  scanf("%d%d", &a, &n);

  for (int i = 0; i < n; i++) {
    scanf("%d", &s[i]);
  }
  if (a == 1) {
    printf("%d\n", n);
    return;
  }
  sort(s, s + n);
  int res = 0;
  int cur = a;
  int ans = n;
  for (int i = 0; i < n; i++) {
    if (s[i] >= cur) {
      int x = 0;
      while (s[i] >= cur) {
        x++;
        cur += cur-1;
      }
      cur += s[i];
      ans = min(ans, res+(n-i));
      res += x;
    } else {
      cur += s[i];
    }
  }
  ans = min(ans, res);
  printf("%d", ans);
  puts("");
}
int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}

