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

int S[10050];

void solve() {
  int N = in();
  int X = in();
  for (int i = 0; i < N; ++i) {
    S[i] = in();
  }
  
  int res = 0;
  sort(S, S + N);
  for (int i = N - 1; i >= 0; --i) {
    ++res;
    int rem = X - S[i];
    int pos = upper_bound(S, S + i, rem) - S;
    --pos;
    if (pos >= 0) {
      for (int j = pos + 1; j < i; ++j) {
        S[j - 1] = S[j];
      }
      --i;
    }
  }

  printf("%d\n", res);
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
