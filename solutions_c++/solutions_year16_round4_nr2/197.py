#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    int n,k;
    cin >> n >> k;
    vd p(n);
    for (int i = 0; i < n; ++i) if (scanf("%lf", &p[i]) != 1) cerr << "FAIL\n";
    printf("Case #%d: ", test);
    sort(p.begin(), p.end());
    double res = 0;
    for (int m = 0; m <= k; ++m) {
      vector<long double> q;
      for (int i = 0; i < m; ++i) q.push_back(p[i]);
      for (int i = 0; i < k-m; ++i) q.push_back(p[n-i-1]);
      sort(q.begin(), q.end());
//      reverse(q.begin(), q.end());
      vector<long double> d(k + 1);
      d[0] = 1;
      for (int i = 0; i < k; ++i) {
        auto nd = d;
        for (int j = 0; j < d.size(); ++j) nd[j] *= 1 - q[i];
        for (int j = 0; j + 1 < d.size(); ++j) nd[j + 1] += d[j] * q[i];
        d.swap(nd);
      }
      res = max(res, (double)d[k/2]);
    }
    printf("%.8lf\n", res);
  }
  return 0;
}
