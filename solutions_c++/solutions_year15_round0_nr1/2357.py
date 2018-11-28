#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <string>
#include <set>
#include <utility>
#include <vector>

using namespace std;

template <typename T> inline T MIN(T a, T b) { return a < b ? a : b; }
template <typename T> inline T MAX(T a, T b) { return a < b ? b : a; }
template <typename T> inline T ABS(T a)      { return a < 0 ? -a : a;}

typedef long long int64;

const int MAXN = 1007;

int main() {
  int T, N;
  char s[MAXN];
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%s", &N, s);
    int ans = 0, acc = 0;
    for (int i = 0; i <= N; ++i) {
      int cur = s[i] - '0';
      if (acc >= i) {
        acc += cur;
      } else {
        ans += i - acc;
        acc = i + cur;
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
