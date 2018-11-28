/*
 * 
 * File:   pDTrieSharding.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on May 31, 2014, 10:48:43 AM
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

namespace pDTrieSharding {

int fpow(int a, int b) {
  int res = 1;
  while (b--)
    res *= a;
  return res;
}

int prefix(const string& a, const string& b) {
  int res = 0;
  while (res < (int) a.size() && res < (int) b.size() && a[res] == b[res])
    res++;
  return res;
}

void solve(int test_num) {
  int M, N, total = 0, best = 1<<30, bestcnt = 0, cnt[4];
  string trie[4][8], str[8];
  cin >> M >> N;
  for (int i = 0; i < M; i++) {
    cin >> str[i];
    total += str[i].size();
  }
  sort(str, str + M);
  for (int mask = fpow(N, M) - 1; mask >= 0; mask--) {
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0, t = mask; i < M; i++, t /= N)
      trie[t % N][cnt[t % N]++] = str[i];
    int sum = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 1; j < cnt[i]; j++)
        sum += prefix(trie[i][j], trie[i][j - 1]);
      if (cnt[i] == 0)
        sum = 13371337;
    }
    if (sum < best) {
      best = sum;
      bestcnt = 0;
    }
    if (sum == best)
      bestcnt++;
  }
  printf("Case #%d: %d %d\n", test_num, total - best + N, bestcnt);
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
  pDTrieSharding::solve();
  return 0;
}
