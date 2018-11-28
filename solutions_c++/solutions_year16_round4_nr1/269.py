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

map<char, vector<string>> dp;

void solve(int test) {
  int n;
  scanf("%d", &n);
  int r, p, s;
  scanf("%d%d%d", &r, &p, &s);
  int r0, p0, s0;
  int g = 0;
  r0 = p0 = s0 = 0;
  string res = "IMPOSSIBLE";
  for (auto x : dp['R'][n]) {
    if (x == 'R') r0++;
    if (x == 'S') s0++;
    if (x == 'P') p0++;
  }
  if (r0 == r && s0 == s && p0 == p) {
    g++;
    res = dp['R'][n];
  }
  r0 = p0 = s0 = 0;
  for (auto x : dp['P'][n]) {
    if (x == 'R') r0++;
    if (x == 'S') s0++;
    if (x == 'P') p0++;
  }
  if (r0 == r && s0 == s && p0 == p) {
    g++;
    res = dp['P'][n];
  }
  r0 = p0 = s0 = 0;
  for (auto x : dp['S'][n]) {
    if (x == 'R') r0++;
    if (x == 'S') s0++;
    if (x == 'P') p0++;
  }
  if (r0 == r && s0 == s && p0 == p) {
    g++;
    res = dp['S'][n];
  }
  assert(g <= 1);
  printf("Case #%d: %s\n", test, res.c_str());
}
int main () {
  dp['R'] = vector<string>(13);
  dp['S'] = vector<string>(13);
  dp['P'] = vector<string>(13);
  dp['R'][0] = "R";
  dp['S'][0] = "S";
  dp['P'][0] = "P";
  eprintf("!!!\n");
  for (int n = 1; n <= 12; n++) {
    dp['R'][n] = min(dp['R'][n - 1] + dp['S'][n - 1], dp['S'][n - 1] + dp['R'][n - 1]);
    dp['S'][n] = min(dp['P'][n - 1] + dp['S'][n - 1], dp['S'][n - 1] + dp['P'][n - 1]);
    dp['P'][n] = min(dp['R'][n - 1] + dp['P'][n - 1], dp['P'][n - 1] + dp['R'][n - 1]);
  }
  eprintf("!!!\n");
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
