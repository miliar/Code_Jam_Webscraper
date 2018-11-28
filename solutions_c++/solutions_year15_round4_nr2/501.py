#include <iostream>
#include <string>
#include <list>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define FOR(i, n) for (int i = 0; i < n ; ++ i)

int N;
long double V, X;

long double rate[100];
long double temp[100];

void solve(int testcase) {
  cin >> N >> V >> X;

  FOR(i, N) cin >> rate[i] >> temp[i];

  if (N == 1) {
    if (X != temp[0]) printf("Case #%d: IMPOSSIBLE\n", testcase);
    else printf("Case #%d: %.10Lf\n", testcase, V / rate[0]);
    return;
  }

  if (N == 2) {
    if (temp[0] == temp[1]) {
      if (X != temp[0]) printf("Case #%d: IMPOSSIBLE\n", testcase);
      else printf("Case #%d: %.10Lf\n", testcase, V / (rate[0] + rate[1]));
    } else {
      long double t2 = V*(X - temp[0]) / (rate[1] * (temp[1] - temp[0]));
      long double T1 = (V - t2*rate[1]) / rate[0];
      long double t1 = (V - V*(X - temp[0]) / (temp[1] - temp[0])) / rate[0];

      if (t1 < 0 || t2 < 0) printf("Case #%d: IMPOSSIBLE\n", testcase);
      else printf("Case #%d: %.10Lf\n", testcase, max(t1, t2));
    }

    return;
  }

  printf("Case #%d: \n", testcase);
}

int main() {
  int T;
  cin >> T;
  FOR(i, T) solve(i+1);
  return 0;
}
