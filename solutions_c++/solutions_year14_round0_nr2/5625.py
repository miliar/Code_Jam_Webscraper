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

int main() {
  freopen("in", "r", stdin); freopen("out", "w", stdout);
  int tt; scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    double x, delta, goal; scanf("%lf %lf %lf", &x, &delta, &goal);
    double co = 2, ans = 0;
    while (goal / co > x / co + goal / (co + delta)) {
      ans += x / co;
      co += delta;
    }
    ans += goal / co;
    printf("Case #%d: %.17lf\n", cc, ans);
  }
  return 0;
}