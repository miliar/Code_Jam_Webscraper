#include <bits/stdc++.h>

using namespace std;

const int N = 210;

int n, k;
double p[N];
/*
long long c[N][N];

void init() {
  for (int i = 0; i < N; ++i) {
    c[i][0] = 1;
  }
  for (int i = 1; i < N; ++i) {
    for (int j = 1; j <= i; ++j) {
      c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
    }
  }
}*/

vector<int> getps(int msk) {
  vector<int> res;
  for (int i = 0; i < n; ++i) {
    if (msk & (1 << i)) {
      res.push_back(i);
    }
  }
  return res;
}

int main() {
  /*init();
  long long ans = 0;
  for (int i = 2; i <= 16; i += 2) {
    ans = max(c[16][i] * c[i][i / 2], ans);
  }
  printf("%lld\n", ans);*/
  int t;
  scanf("%d", &t);
  for (int _ = 1; _ <= t; ++_) {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) {
      scanf("%lf", p + i);
    }
    vector<int> v;
    for (int msk = 0; msk < 1 << n; ++msk) {
      if (__builtin_popcount(msk) == k) v.push_back(msk);
    }
    vector<int> v2;
    for (int msk = 0; msk < 1 << k; ++msk) {
      if (__builtin_popcount(msk) == k / 2) v2.push_back(msk);
    }
    double ans = 0;
    for (auto i : v) {
      vector<int> ps = getps(i);
      double sum = 0;
      for (int j : v2) {
        double tmp = 1;
        for (int pp = 0; pp < k; ++pp) {
          if (j & (1 << pp)) {
            tmp *= p[ps[pp]];
          }
          else {
            tmp *= (1 - p[ps[pp]]);
          }
        }
        sum += tmp;
      }
      ans = max(sum, ans);
    }
    printf("Case #%d: %.10f\n", _, ans);
  }
  return 0;
}
