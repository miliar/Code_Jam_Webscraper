#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<long double> gao(const vector<long double>& ps) {
  int n = ps.size();
  vector<long double> ret(n + 1, 0.0);
  ret[0] = 1;
  for (long double p: ps) {
    for (int i = n; i > 0; --i) {
      ret[i] = ret[i] * (1 - p) + ret[i - 1] * p;
    }
    ret[0] *= 1 - p;
  }
  return ret;
}

int main() {
  int re, n, m;
  long double ans;
  vector<long double> p;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    scanf("%d%d", &n, &m);
    p.resize(n);
    for (int i = 0; i < n; ++i) {
      scanf("%Lf", &p[i]);
    }
    sort(p.begin(), p.end());

    ans = 0;
    for (int i = 0; i <= m; ++i) {
      vector<long double> t;
      t.insert(t.end(), p.begin(), p.begin() + i);
      t.insert(t.end(), p.rbegin(), p.rbegin() + (m - i));
      ans = max(ans, gao(t)[m / 2]);
    }
    printf("Case #%d: %.12Lf\n", ri, ans);
  }

  return 0;
}
