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

using namespace std;

typedef unsigned uint;
typedef long long Int;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }

int possible[16][1<<16];

void solve() {
  int N = in();
  vector<int> ps;
  vector<int> ev, ids;

  for (int i = 0; i < N; ++i) {
    char s[4];
    int id;
    scanf("%s%d", s, &id);
    if (s[0] == 'E') {
      ev.push_back(0);
    } else {
      ev.push_back(1);
    }
    ids.push_back(id);
    if (id != 0) ps.push_back(id);
  }

  sort(ps.begin(), ps.end());
  ps.erase(unique(ps.begin(), ps.end()), ps.end());
  for (int i = 0; ps.size() < N; ++i) {
    ps.push_back(3000 + i);
  }

  memset(possible, 0, sizeof(possible));
  for (int i = 0; i < (1<<N); ++i) {
    possible[0][i] = 1;
  }

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < (1<<N); ++j) {
      if (possible[i][j]) {
        if (ev[i] == 0) {
          for (int k = 0; k < N; ++k) {
            if ((ids[i] == 0 || ids[i] == ps[k]) && !(j & (1 << k))) {
              possible[i + 1][j | (1<<k)] = 1;
            }
          }
        } else {
          for (int k = 0; k < N; ++k) {
            if ((ids[i] == 0 || ids[i] == ps[k]) && (j & (1 << k))) {
              possible[i + 1][j ^ (1<<k)] = 1;
            }
          }
        }
      }
    }
  }

  int res = 1024;
  for (int i = 0; i < (1<<N); ++i) {
    if (possible[N][i]) {
      chmin(res, __builtin_popcount(i));
    }
  }

  if (res == 1024) {
    puts("CRIME TIME");
  } else {
    printf("%d\n", res);
  }
}

int main()
{
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
