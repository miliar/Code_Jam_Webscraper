#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdarg>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define mp make_pair
#define pb push_back
#define sz(c) (int)(c).size()
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const int maxn = 1 << 10;
const int INF = maxn * maxn * maxn;
int a[maxn];
int b[maxn];
int c[maxn];
int dp[maxn][maxn];
int n;

int dd[maxn][2];

int calc(int first, int last) {
  int ind = first + (n - 1 - last);
  if (ind == n) return 0;
  int &res = dp[first][last];
  if (res != -1) return res;
  res = INF;
  int cnt0 = dd[ind][0];
  int cnt1 = dd[ind][1];
  res = min(res, cnt0 + calc(first + 1, last));
  res = min(res, cnt1 + calc(first, last - 1));
  return res;
}

void solve(int test) {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%d", &a[i]), b[i] = a[i];
  sort(b, b + n);
  for (int i = 0; i < n; i++) a[i] = lower_bound(b, b + n, a[i]) - b;
  for (int i = 0; i < n; i++) c[a[i]] = i;
  memset(dd, 0, sizeof dd);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (a[j] > i) {
        if (j < c[i]) {
          dd[i][0]++;
        }
        if (j > c[i]) {
          dd[i][1]++;  
        }
      }
    }
  }
  memset(dp, -1, sizeof dp);
  printf("Case #%d: %d\n", test, calc(0, n - 1));
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
