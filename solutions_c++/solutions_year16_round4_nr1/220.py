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

void solve() {
  int N = in();
  int K[3];
  K[1] = in(); K[0] = in(); K[2] = in();

  string res = "Z";
  for (int top = 0; top < 3; ++top) {
    int seq[4096], tmp[4096];
    seq[0] = top;
    for (int i = 0; i < N; ++i) {
      memcpy(tmp, seq, sizeof(tmp));
      for (int j = 0; j < (1 << i); ++j) {
        seq[2 * j + 0] = tmp[j];
        seq[2 * j + 1] = (tmp[j] + 1) % 3;
      }
    }
    int ks[3] = {};
    for (int i = 0; i < (1 << N); ++i) {
      ks[seq[i]]++;
    }
    if (!(ks[0] == K[0] && ks[1] == K[1] && ks[2] == K[2])) {
      continue;
    }
    for (int i = N, sz = 1; i > 0; --i, sz *= 2) {
      for (int j = 0; j < (1 << N); j += sz * 2) {
        bool sw = false;
        for (int k = 0; k < sz; ++k) {
          if (seq[j + k] != seq[j + sz + k]) {
            sw = seq[j + k] > seq[j + sz + k];
            break;
          }
        }
        if (sw) {
          for (int k = 0; k < sz; ++k) {
            swap(seq[j + k], seq[j + sz + k]);
          }
        }
      }
    }
    string r = "";
    for (int i = 0; i < (1 << N); ++i) {
      if (seq[i] == 0) r += "P";
      if (seq[i] == 1) r += "R";
      if (seq[i] == 2) r += "S";
    }
    if (res > r) {
      res = r;
    }
  }

  if (res == "Z") {
    puts("IMPOSSIBLE");
  } else {
    puts(res.c_str());
  }
}

int main() {
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
