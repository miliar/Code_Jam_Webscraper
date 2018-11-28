#include <cassert>
#include <cstdlib>
#include <cstdio>

#include <functional>
#include <iostream>
#include <algorithm>
#include <valarray>
#include <iterator>
#include <complex>
#include <numeric>
#include <utility>
#include <bitset>
#include <limits>
#include <memory>
#include <random>
#include <string>
#include <tuple>
#include <new>

#include <unordered_set>
#include <unordered_map>
#include <forward_list>
#include <vector>
#include <deque>
#include <array>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define ALL(c) begin(c), end(c)
#define SIZE(c) (int)(c).size()
#define TIMESTAMP(x) eprintf("["#x"] Time : %.3lf s.\n", 1. * clock() / CLOCKS_PER_SEC)
#define TIMESTAMPf(x, ...) eprintf("[" x "] Time : %.3lf s.\n", __VA_ARGS__, 1. * clock() / CLOCKS_PER_SEC)

using namespace std;

std::random_device rd;
std::mt19937 gena(rd());

double get(vector<double> v) {
  vector<vector<double>> c(v.size() + 1, vector<double>(v.size() + 1));
  c[0][0] = 1.;
  for (int i = 0; i < (int)v.size(); i++) {
    c[i + 1][0] = c[i][0] * (1 - v[i]);
    for (int j = 1; j <= i + 1; j++) {
      c[i + 1][j] = v[i] * c[i][j - 1] + (1 - v[i]) * c[i][j];
    } 
  }
  return c[(int)v.size()][v.size() / 2];
}

void solve(int test) {
  int n, k;
  scanf("%d%d", &n, &k);
  vector<double> p(n);
  for (int i = 0; i < n; i++) {
    scanf("%lf", &p[i]);
  }
  sort(p.begin(), p.end());
  double res = 0.;
  /*
  for (int mask = 0; mask < (1<<n); mask++) {
    if (__builtin_popcount(mask) != k) continue;
    vector<double> v;
    for (int i = 0; i < n; i++) {
      if ((mask >> i) & 1) {
        v.push_back(p[i]);
      }
    }
    double cur = get(v);
    if (res <= cur) {
      //eprintf("%lf -> %lf\n", res, cur);
      //for (int i = 0; i < n; i++) eprintf("%d", (mask >> i) & 1);
      //eprintf("\n");
      res = cur;
    }
  }*/
  for (int i = 0; i <= k; i++) {
    vector<double> v;
    for (int j = 0; j < i; j++) {
      v.push_back(p[j]);
    }
    for (int j = n - (k - i); j < n; j++) {
      v.push_back(p[j]);
    }
    assert((int)v.size() == k);
    double cur = get(v);
    if (res < cur) {
      res = cur;
    }
  } 
  printf("Case #%d: %lf\n", test, res);
}
int main () {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
