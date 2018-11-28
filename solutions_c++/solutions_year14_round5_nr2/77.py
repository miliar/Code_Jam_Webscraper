/*
 * 
 * File:   pBLastHit.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on Jun 14, 2014, 10:23:59 AM
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

namespace pBLastHit {
int P, Q, N, hp[111], gold[111], dp[111][1111][2]; //<= i dead, free turns, i killed last?

void chmax(int& a, int b) {
  if (b > a)
    a = b;
}

void solve(int test_num) {
  //my hit, tower hit
  cin >> P >> Q >> N;
  for (int i = 1; i <= N; i++)
    cin >> hp[i] >> gold[i];
  memset(dp, 0xC0, sizeof(dp));
  dp[0][0][0] = 0;
  for (int i = 1; i <= N; i++) {
    const int tower = (hp[i] + Q - 1) / Q;
    for (int t = 0; t <= 1000; t++) {
      chmax(dp[i][t + tower][0], dp[i - 1][t][0]);
      chmax(dp[i][t + tower - 1][0], dp[i - 1][t][1]);
      for (int use = 0; use <= t; use++) {
        const int now = hp[i] - use * P;
        if (now <= 0) {
          chmax(dp[i][t - use][1], max(dp[i - 1][t][0], dp[i - 1][t][1]) + gold[i]);
          break;
        }
        //# of tower hits
        for (int thit = 0;; thit++) {
          if (now - thit * Q <= 0)
            break;
          int moves = (now - thit * Q + P - 1) / P;
          //i go first
          if (moves <= thit + 1)
            chmax(dp[i][t - use + thit + 1 - moves][1], dp[i - 1][t][0] + gold[i]);
          //i go second
          if (moves <= thit)
            chmax(dp[i][t - use + thit - moves][1], dp[i - 1][t][1] + gold[i]);
        }
      }
    }
  }
  int res = 0;
  for (int t = 0; t <= 1000; t++)
    chmax(res, max(dp[N][t][0], dp[N][t][1]));
  printf("Case #%d: %d\n", test_num, res);
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  pBLastHit::solve();
  return 0;
}
