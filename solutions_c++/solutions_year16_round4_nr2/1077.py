#include <bits/stdc++.h>

using namespace std;

template<class T> inline T sqr(const T& a) {
  return a * a;
}

template<class T> inline T middle(const T &a, const T &b) {
  return (a + b) / 2;
}

template<class T> inline int len(const T &c) {
  return static_cast<int>(c.size());
}

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 17;

ld pr[N];
ld qr[N];

ld d[N][N];

ld Calc(const vector<int> &ids, int k) {
  d[0][0] = 1.0;
  for (int i = 0; i < k; ++i) {
    int id = ids[i];
    d[i + 1][0] = 0.0;
    for (int j = 0; j <= i; ++j) {
      d[i + 1][j] += d[i][j] * qr[id];
      d[i + 1][j + 1] = d[i][j] * pr[id];
    }
  }
  return d[k][k / 2];
}

void HandleCase() {
  int n, k;
  scanf("%d%d", &n, &k);
  for (int i = 0; i < n; ++i) {
    double t;
    scanf("%lf", &t);
    pr[i] = t; 
    qr[i] = 1.0 - t;
  }
  int mend = 1 << n;
  vector<int> ids;
  ld ans = 0;
  for (int mask = 0; mask < mend; ++mask) {
    ids.clear();
    for (int i = 0; i < n; ++i) {
      if (mask & (1 << i)) {
        ids.push_back(i);
        if (len(ids) > k) {
          break;
        }
      }
    }
    if (len(ids) != k) {
      continue;
    }
    ans = max(ans, Calc(ids, k));
  }
  printf("%.10lf\n", (double) ans);
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    HandleCase();
  }
  return 0;
}
