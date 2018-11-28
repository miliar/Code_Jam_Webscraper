/*
 * 
 * File:   pCCrimeHouse.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on Jun 14, 2014, 11:32:31 AM
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

namespace pCCrimeHouse {
char type[1111];
int id[1111];
int dp[1 << 15];
int score[1 << 15];
int N;

void chmin(int& a, int b) {
  if (b < a)
    a = b;
}

void solve(int test_num) {
  int seq[15], party[15];
  cin >> N;
  for (int i = 0; i < N; i++)
    cin >> skipws >> type[i] >> id[i];
  memset(dp, 0x3F, sizeof(dp));
  dp[0] = 0;
  for (int mask = 1; mask < (1 << N); mask++) {
    int M = 0;
    for (int i = 0; i < N; i++) {
      if (1 << i & mask) {
        seq[M] = type[i];
        party[M++] = id[i];
      }
    }
    bool ok = true;
    int person = -1;
    for (int i = 0; i < M; i++) {
      if (i > 0 && seq[i] == seq[i - 1])
        ok = false;
      if (party[i] > 0 && person != -1 && party[i] != person)
        ok = false;
      if (party[i] > 0 && person == -1)
        person = party[i];
    }
    for (int i = 0; i < N; i++)
      if ((1 << i & ~mask) && id[i] == person)
        ok = false;
    if (!ok)
      score[mask] = -1;
    else
      score[mask] = seq[M - 1] == 'E';
  }
  for (int mask = 1; mask < (1 << N); mask++)
    for (int sub = mask; sub > 0; sub = (sub - 1) & mask)
      if (score[sub] != -1)
        dp[mask] = min(dp[mask], score[sub] + dp[mask ^ sub]);
  printf("Case #%d: ", test_num);
  if (dp[(1 << N) - 1] > 1111)
    puts("CRIME TIME");
  else
    printf("%d\n", dp[(1 << N) - 1]);
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
  pCCrimeHouse::solve();
  return 0;
}
