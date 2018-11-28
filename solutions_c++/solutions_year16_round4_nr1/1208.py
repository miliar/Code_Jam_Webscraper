#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int const N = 13;
int main() {
  string z[N][3], z0, z1;
  z[0][0] = "R";
  z[0][1] = "P";
  z[0][2] = "S";
  for (int i = 1; i < N; ++i) {
    z0 = z[i - 1][0];
    z1 = z[i - 1][2];
    z[i][0] = min(z0 + z1, z1 + z0);
    z0 = z[i - 1][1];
    z1 = z[i - 1][0];
    z[i][1] = min(z0 + z1, z1 + z0);
    z0 = z[i - 1][2];
    z1 = z[i - 1][1];
    z[i][2] = min(z0 + z1, z1 + z0);
  }
  int t;
  scanf("%d", &t);
  for (int ti = 1; ti <= t; ++ti) {
    int n, r, p, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    int rr, pp, ss;
    bool flag = true;
    for (int i = 0; i < n; ++i) {
      rr = (r + s - p) / 2;
      pp = (r - s + p) / 2;
      ss = (-r + s + p) / 2;
      if (rr < 0 || pp < 0 || ss < 0) {
        flag = false;
        break;
      }
      r = rr;
      p = pp;
      s = ss;
    }
    printf("Case #%d: ", ti);
    if (flag) {
      printf("%s", r ? z[n][0].c_str() : p ? z[n][1].c_str() : z[n][2].c_str());
    } else {
      printf("IMPOSSIBLE");
    }
    printf("\n");
  }
  return 0;
}
