#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define LOG(x) cerr << #x << " = " << (x) << "\n"

typedef long long llint;
typedef pair<int,int> pii;
typedef double ldouble;
const ldouble EPS = 1e-7;

void solve() {
  int n;
  ldouble V, C;
  ldouble v1, c1;
  ldouble v2, c2;

  scanf("%d%lf%lf", &n, &V, &C);
  if (n == 1) {
    scanf("%lf%lf", &v1, &c1);
    ldouble t1 = V / v1;
    if (c1 != C) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%.7lf\n", t1);
    }
  } else {
    scanf("%lf%lf", &v1, &c1);
    scanf("%lf%lf", &v2, &c2);
    if (c2 == c1) {
      v1 += v2;
      ldouble t1 = V / v1;
      if (c1 != C) {
        printf("IMPOSSIBLE\n");
      } else {
        printf("%.7lf\n", t1);
      }
    } else {
      ldouble t2 = V * (C - c1) / (v2 * (c2 - c1));
      ldouble t1 = (V - t2 * v2) / v1;
      if ((c1 < C && c2 < C) || (c1 > C && c2 > C)) {
        printf("IMPOSSIBLE\n");
      } else {
        printf("%.7lf\n", max(t1, t2));
      }
    }
  }
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}

