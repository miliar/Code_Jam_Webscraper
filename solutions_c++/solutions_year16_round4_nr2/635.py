#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

typedef long long lol;
typedef vector<double> VI;
typedef vector<VI> VVI;

double tr(const VI &u) {
  int k = u.size() / 2 + 1;
  VVI dd(k, VI(k));
  dd[0][0] = 1.;
  for (int i = 1; i < k; ++i) {
    dd[0][i] = dd[0][i-1] * u[i-1];
  }
  for (int j = 1; j < k; ++j) {
    dd[j][0] = (1 - u[j-1]) * dd[j-1][0];
    for (int i = 1; i < k; ++i) {
      double p = u[i + j - 1];
      dd[j][i] = (1. - p) * dd[j-1][i] + p * dd[j][i-1];
    }
  }

  return dd[k-1][k-1];
}

double solve(const int &k, const VI &pr) {
  double ans = 0., cur;
  for (int i = 0; i <= k; ++i) {
    VI u(k);
    for (int j = 0; j < i; ++j) {
      u[j] = pr[j];
    }
    for (int j = 0; j < k - i; ++j) {
      u[i + j] = pr[pr.size() - 1 - j];
    }

    cur = tr(u);

    if (ans < cur) {
      ans = cur;
    }
  }
  return ans;
}

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  freopen("B-large.in", "rt", stdin);
  //freopen("B-small-attempt0.in", "rt", stdin);
  freopen("outputBS.txt", "w", stdout);
#endif

  int line_num;
  cin >> line_num;
  for (int line = 0; line < line_num; ++line) {
    lol n, k;
    cin >> n >> k;
    VI pr(n);
    for (int i = 0; i < n; ++i) {
      cin >> pr[i];
    }
    std::sort(pr.begin(), pr.end());
    double ans = solve(k, pr);
    printf("Case #%d: %f\n", line + 1, ans);
  }
  return 0;
}
