#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

void solve();
int main() {
  int test;
  scanf("%d", &test);
  char str[1000];
  fgets(str, 999, stdin);
  int test_case = 0;
  while (test--) {
    test_case++;
    printf("Case #%d: ", test_case);
    // puts("");
    solve();
  }
}


int n, k;
double p[3000];
double ps[100];
void solve() {
  scanf("%d %d", &n, &k);
  REP(i, n) {
    scanf("%lf", &p[i]);
  }
  sort(p, p + n);
  double ans = 0.0;
  FOREQ(i, 0, k) {
    REP(j, n + 10) { ps[j] = 0; }
    ps[0] = 1;
    FOR(j, 0, i) {
      // cout << j << endl;
      for (int l = n; l >= 0; l--) {
        ps[l + 1] += ps[l] * p[j];
        ps[l] = ps[l] * (1.0 - p[j]);
      }
    }
    int rest = k - i;
    // cout << i << " " << rest << endl;
    for (int j = n - 1; rest > 0; rest--, j--) {
      // cout << j << endl;
      for (int l = n; l >= 0; l--) {
        ps[l + 1] += ps[l] * p[j];
        ps[l] = ps[l] * (1.0 - p[j]);
      }
    }
    ans = max(ans, ps[k / 2]);
    // cout << ps[k / 2] << endl;
  }
  printf("%.8f\n", ans);
}
