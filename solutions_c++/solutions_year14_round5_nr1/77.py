/*
 * 
 * File:   pAMagicalMarvelousTour.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on Jun 14, 2014, 10:02:01 AM
 */

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

using namespace std;

namespace pAMagicalMarvelousTour {
typedef long long ll;
int x[1 << 20];
ll sum[1 << 20];

void solve(int test_num) {
  int N, P, Q, R, S;
  cin >> N >> P >> Q >> R >> S;
  for (int i = 1; i <= N; i++)
    x[i] = ((i - 1LL) * P + Q) % R + S;
  sum[0] = sum[N + 1] = 0;
  for (int i = 1; i <= N; i++)
    sum[i] = sum[i - 1] + x[i];
  ll best = 0;
  for (int i = 1; i <= N; i++) {
    ll her = sum[N] - sum[i];
    int pos = lower_bound(sum, sum + i, sum[i] / 2) - sum;
    if (max(sum[i] - sum[pos], sum[pos]) < max(sum[i] - sum[pos - 1], sum[pos - 1]))
      her = max(her, max(sum[i] - sum[pos], sum[pos]));
    else
      her = max(her, max(sum[i] - sum[pos - 1], sum[pos - 1]));
    best = max(best, sum[N] - her);
  }
  printf("Case #%d: %.9lf\n", test_num, ((double) best / sum[N]));
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  int tests;
  cin >> tests;
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  pAMagicalMarvelousTour::solve();
  return 0;
}
