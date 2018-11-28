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

int P[1024];
char S[1024];

void solve() {
  int N, K;
  scanf("%s%d", S, &K);
  N = strlen(S);
  fill(P, P + N, 0);

  int res = 0, parity = 0;
  for (int i = 0; i < N; ++i) {
    parity ^= P[i];
    if ((S[i] == '-') ^ parity) {
      if (i + K > N) {
        puts("IMPOSSIBLE");
        return;
      }
      ++res;
      parity ^= 1;
      P[i + K] ^= 1;
    }
  }

  printf("%d\n", res);
}

int main() {
  int T = in();

  for (int TC = 1; TC <= T; ++TC) {
    printf("Case #%d: ", TC);
    solve();
  }

  return 0;
}
