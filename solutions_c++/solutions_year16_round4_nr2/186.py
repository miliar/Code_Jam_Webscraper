#include <bits/stdc++.h>
using namespace std;

double dp[205][205];
vector <double> p;
double pp[205];


double hitung(int num, int y) {
  if (num == -1) {
    if (y == 0) return 1;
    return 0;
  }
  double &res = dp[num][y];
  if (res == res) {
    return res;
  }
  res = hitung(num - 1, y) * (1 - p[num]);
  if (y > 0) {
    res += hitung(num - 1, y - 1) * p[num];
  }
  return res;
}
int main() {
  int t;
  int cs  =0;
  scanf("%d", &t);
  while (t--) {
    ++cs;
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
      scanf("%lf", &pp[i]);
    }
    sort(pp, pp + n);
    double res = 0;
    for (int i = 0; i <= k; i++) {
      memset(dp, -1, sizeof(dp));
      p.clear();
      for (int xx = 0; xx < i; xx++) {
        p.push_back(pp[xx]);
      }
      for (int xx = n - k + i; xx  < n; xx++) {
        p.push_back(pp[xx]);
      }
      double tmp = hitung(k - 1, k / 2);
      if (tmp > res) {
        res = tmp;
      }
    }
    printf("Case #%d: ", cs);
    printf("%.10lf\n", res);
  }
}
