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
#include <ctime>

using namespace std;

int x[17];

int main() {
  freopen("in", "r", stdin); freopen("out", "w", stdout);
  int tt; scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    for (int i = 1; i <= 16; ++i) x[i] = 0;
    for (int k = 0; k < 2; ++k) {
      int r; scanf("%d", &r);
      for (int i = 1; i <= 4; ++i)
        for (int j = 1; j <= 4; ++j) {
          int y; scanf("%d", &y);
          if (i == r) ++x[y];
        }
    }
    int ans = -1, cnt = 0;
    for (int i = 1; i <= 16; ++i)
      if (x[i] == 2) {
        ans = i; ++cnt;
      }
    printf("Case #%d: ", cc);
    if (cnt == 0) puts("Volunteer cheated!"); else
    if (cnt == 1) printf("%d\n", ans);
    else puts("Bad magician!");
  }
  return 0;
}