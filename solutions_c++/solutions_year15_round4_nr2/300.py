/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home

long double r[102], x[102];

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  int n;
  long double V, X;
  cin >> n >> V >> X;
  r[0] = r[1] = 0;
  for (int i = 0; i < n; ++i) {
    cin >> r[i] >> x[i];
  }
  if (n == 1 || fabs(x[0] - x[1]) < 1e-8) {
    if (n == 2) {
      r[0] += r[1];
      // cout << "fuck\n";
    }
    if (fabs(X - x[0]) < 1e-8)
      printf("%.10lf\n", (double)(V / r[0]));
    else
      puts("IMPOSSIBLE");
    return;
  }
  long double ll = 0, rr = 1e+20;//5 * V / 1e-5;
  for (int it = 0; it < 200; ++it) {
    long double m = (ll + rr) / 2;

    long double v0 = V * (X - x[1]) / (x[0] - x[1]);
    long double eps = 1e-12;
    if (v0 >= -eps && v0 <= r[0] * m + eps && (V - v0) >= -eps && (V - v0) <= r[1] * m + eps) rr = m;
    else ll = m;
  }
  if (ll > 1e+9) {
    puts("IMPOSSIBLE");
    if (min(x[0], x[1]) <= X + 1e-8 && X <= max(x[0], x[1]) + 1e-8)
      puts("fuck");
  } else
    printf("%.10lf\n", (double)ll);
}

int main() {
// #ifndef Fdg_Home
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
// #endif
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}