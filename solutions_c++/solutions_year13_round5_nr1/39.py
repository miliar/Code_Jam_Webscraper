#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cassert>
#include <utility>
#include <algorithm>

using namespace std;

typedef long long llint;

const int SIZE = 36;

int main() {
  int re;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    int n;
    llint a, b;
    double ans;
    vector<llint> v;

    scanf("%lld%d", &b, &n);
    for (int i = 0; i < n; ++i) {
      scanf("%lld", &a);
      v.push_back(a);
    }
    for (int i = n; i <= SIZE; ++i) {
      v.push_back(0);
    }
    sort(v.begin(), v.end());

    ans = 0;
    for (int i = 1; i < SIZE; ++i) {
      llint lo = v[i - 1], hi = v[SIZE] - 1;
      while (lo < hi) {
        llint mi = (lo + hi) / 2;
        llint sum = 0;
        for (int j = 0; j < i; ++j) {
          sum += mi - v[j];
        }
        for (int j = i; j <= SIZE; ++j) {
          sum += max(0LL, mi + 1 - v[j]);
        }
        if (sum <= b) {
          lo = mi + 1;
        } else {
          hi = mi;
        }
      }
      lo = hi - 1;
      // assert(lo >= v[i - 1]);
      if (lo >= v[i - 1]) {
        llint sum = 0;
        for (int j = 0; j < i; ++j) {
          sum += lo - v[j];
        }
        llint win = sum;
        for (int j = i; j <= SIZE; ++j) {
          sum += max(0LL, lo + 1 - v[j]);
        }
        assert(sum <= b);
        ans = max(ans, (double)win * SIZE / i - (double)sum);
      }
    }

    printf("Case #%d: ", ri);
    printf("%.10lf\n", ans);
    fflush(stdout);
  }

  return 0;
}
