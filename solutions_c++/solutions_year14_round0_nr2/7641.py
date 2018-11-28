#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int T;
double c, f, x;
double t[100010];
double F(int n) {
  return t[n] + x / (2. + f * n);
}
int main() {
  scanf("%d", &T);
  for (int ca = 1; ca <= T; ++ca) {
    scanf("%lf%lf%lf", &c, &f, &x);
    t[0] = 0;
    for (int i = 1; i <= 100000; ++i) {
      t[i] = t[i - 1] + c / (2. + f * (i - 1));
    }
    int l = 0, r = 100000, lmid, rmid;
    while (l < r)  {
      if (l + 1 == r) {
        if (F(l) > F(r)) l = r;
        break;
      }
      if (l + 2 == r) {
        if (F(l + 1) < F(r) && F(l + 1) < F(l)) l = l + 1;
        else if (F(r) < F(l) && F(r) < F(l + 1)) l = r;
        break;
      }
      lmid = int((r - l) / 3.) + l;
      rmid = int((r - l) / 3. * 2) + l;
      if (F(lmid) < F(rmid)) r = rmid;
      else l = lmid;
    }
    printf("Case #%d: %.10f\n", ca, F(l));
  }
  return 0;
}
