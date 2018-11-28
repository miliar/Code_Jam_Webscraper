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

int main() {
  int T, x, r, c;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%d%d", &x, &r, &c);
    if (x == 1) {
      printf("Case #%d: GABRIEL", t);
    } else if (x == 2) {
      if (r % 2 == 0 || c % 2 == 0) {
        printf("Case #%d: GABRIEL", t);
      } else {
        printf("Case #%d: RICHARD", t);
      }
    } else if (x == 3) {
      if ((r == 3 && c != 1) || (c == 3 && r != 1)) {
        printf("Case #%d: GABRIEL", t);
      } else {
        printf("Case #%d: RICHARD", t);
      }
    } else {
      if (r * c >= 12) {
        printf("Case #%d: GABRIEL", t);
      } else {
        printf("Case #%d: RICHARD", t);
      }
    }
    puts("");
  }
  return 0;
}
