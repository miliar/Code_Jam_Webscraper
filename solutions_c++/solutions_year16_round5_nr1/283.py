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
  char S[20050];
  scanf("%s", S);
  int N = strlen(S);
  
  stack<int> stk;
  int res = 0;
  for (int i = 0; i < N; ++i) {
    if (stk.empty()) {
      stk.push(S[i]);
    } else if (stk.top() == S[i]) {
      stk.pop();
      ++res;
    } else if (stk.size() + 1 > N - i - 1) {
      stk.pop();
    } else {
      stk.push(S[i]);
    }
  }

  printf("%d\n", 5 * N / 2 + 5 * res);
}

int main() {
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
