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

char str[100];

int good(vector<vector<int>> a) {
  int n = (int)a.size();
  vector<int> p(n);
  for (int i = 0; i < n; i++) p[i] = i;
  int fail = 0;
  do {
    //eprintf("check!\n");
    vector<int> f(1 << n);
    vector<int> q(1 << n);
    f[0] = 1;
    for (auto x : p) {
      //eprintf("x = %d\n", x);
      for (int i = 0; i < (int)f.size(); i++) {
        if (f[i]) {
          int tt = 0;
          for (int j = 0; j < n; j++) {
            if (a[x][j] == 1 && (((i >> j) & 1) == 0)) {
              tt = 1;
              q[i | (1 << j)] = 1;
            }
          }
          if (!tt) fail = 1;
        }
      }
      if (fail) break;
      f = q;
    }
    if (fail) break;
  } while(next_permutation(begin(p), end(p)));
  /*
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      eprintf("%d", a[i][j]);
    }
    eprintf("\n");
  }
  eprintf("fail = %d\n", fail);
  */
  return !fail;
}

void solve(int test) {
  int n;
  scanf("%d", &n);
  vector<vector<int> > a(n, vector<int>(n)); 
  vector<pair<int, int>> pos;
  for (int i = 0; i < n; i++) {
    scanf("%s", str);
    for (int j = 0; j < n; j++) {
      a[i][j] = str[j] - '0';
      if (!a[i][j]) {
        pos.push_back(make_pair(i, j));
      }
    }
  }
  int res = (int)pos.size();
  for (int mask = 0; mask < (1 << pos.size()); mask++) {
    //eprintf("mask = %d\n", mask);
    vector<vector<int>> tmp = a;
    for (int i = 0; i < (int)pos.size(); i++) {
      if ((mask >> i) & 1) {
        tmp[pos[i].first][pos[i].second] = 1;
      }
    }
    if (good(tmp)) {
      //eprintf("mask = %d\n", mask);
      res = min(res, __builtin_popcount(mask));
    }
  }
  printf("Case #%d: %d\n", test, res);
 // eprintf("test = %d\n", test);
}

int main () {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
