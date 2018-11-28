#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef unsigned long long UInt;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
Int lin() { Int x; scanf("%lld", &x); return x; }

char F[128][128];
int RS[128], CS[128];

void solve() {
  int R = in();
  int C = in();

  memset(RS, 0, sizeof(RS));
  memset(CS, 0, sizeof(CS));
  for (int i = 0; i < R; ++i) {
    scanf("%s", F[i]);
    for (int j = 0; j < C; ++j) {
      if (F[i][j] != '.') {
        ++RS[i];
        ++CS[j];
      }
    }
  }

  bool ok = true;
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (F[i][j] != '.') {
        ok &= RS[i] >= 2 || CS[j] >= 2;
      }
    }
  }
  if (!ok) {
    puts("IMPOSSIBLE");
    return;
  }

  int cnt = 0;
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (F[i][j] != '.') {
        int dx = 0, dy = 0;
        if (F[i][j] == '>') dx = 1;
        if (F[i][j] == '<') dx = -1;
        if (F[i][j] == '^') dy = -1;
        if (F[i][j] == 'v') dy = 1;
        int ii = i + dy, jj = j + dx;
        while (0 <= ii && ii < R && 0 <= jj && jj < C) {
          if (F[ii][jj] != '.') {
            break;
          }
          ii += dy;
          jj += dx;
        }
        if (ii < 0 || ii >= R || jj < 0 || jj >= C) {
          ++cnt;
        }
      }
    }
  }

  printf("%d\n", cnt);
}

int main() {
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
