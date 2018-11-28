#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <set>
#include <map>
#include <complex>
#include <iostream>
#include <time.h>
#include <stack>
#include <stdlib.h>
#include <memory.h>
#include <bitset>
#include <math.h>
#include <string>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

const int MaxN = 100000 + 10;
const int MOD = 1e9 + 7;
const int INF = 1e9;

double arr[MaxN], prod[MaxN], uprod[MaxN];
int bits[MaxN];

void solve() {
  int n, k;
  scanf("%d%d", &n, &k);
  for (int i = 0; i < n; ++i) {
    scanf("%lf", &arr[i]);
  }
  for (int i = 0; i < 1 << n; ++i) {
    prod[i] = uprod[i] = 1.0;
    bits[i] = 0;
    for (int j = 0; j < n; ++j) {
      if (i & (1 << j)) {
        prod[i] *= arr[j];
        uprod[i] *= 1.0 - arr[j];
        bits[i]++;
      }
    }
  }
  double ans = 0;
  for (int i = 0; i < 1 << n; ++i) {
    if (bits[i] != k) {
      continue;
    }
    double cur = 0;
    for (int j = i; j > 0; j = (j - 1) & i) {
      if (bits[j] == k / 2) {
        cur += prod[j] * uprod[i ^ j];
      }
    }
    ans = max(ans, cur);
  }
  printf("%.6lf\n", ans);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int it = 1; it <= t; ++it) {
    printf("Case #%d: ", it);
    solve();
  }
  return 0;
}
