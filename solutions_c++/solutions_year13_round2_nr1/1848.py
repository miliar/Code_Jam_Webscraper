//__builtin_ffs (find first set), __builtin_ctz (count trailing zeros), builtin_clz (count leading zeros)

#include <cassert>
#include <cfloat>     // DBL_EPSILON (min 1E-9); DBL_MAX
#include <climits>    // INT_MIN, INT_MAX; LONG_MIN, LONG_MAX; LLONG_MIN, LLONG_MAX
#include <cmath>      // atan2; ext, log, log10; pow, sqrt; ceil, floor; fabs
#include <cstdio>     // puts
#include <cstdlib>    // malloc, free; rand; abs, div; bsearch, qsort
#include <cstring>    // memset

#include <algorithm>
#include <bitset>
#include <deque>
#include <ext/hash_set>
#include <functional> // greater
#include <iterator>   // back_inserter
#include <iostream>
#include <list>
#include <map>
#include <numeric>    // accumulate, adjacent_difference, inner_product, partial_sum
#include <queue>      // queue, priority_queue
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace __gnu_cxx;	// iota
using namespace std;

typedef unsigned long long ull;

const int MAX = 101;
int v[MAX];

int solve(int A, int mote) {
  double arg = static_cast<double>(mote - 1);
  arg /= A - 1.0;
  double bin_log = log2(arg);
  int ans = static_cast<int>(floor(bin_log)) + 1;
  // cout << "solve " << A << " " << mote << " " << ans << endl;
  return ans;
}

int main() {
  // log2 = log(2.0);
  int T;
  cin >> T;
  int A, N;
  for (int t = 1; t <= T; ++ t) {
    cin >> A >> N;
    for (int i = 0; i < N; ++ i) {
      scanf("%d ", v + i);
    }

    int cnt = N;
    if (A != 1) {
      sort(v, v + N);
      int res = 0;
      for (int i = 0; i < N; ++ i) {
        if (A <= v[i]) {
          int k = solve(A, v[i]);
          res += k;
          int pow_k = 1L << k;
          A = pow_k * A - pow_k + 1;
        }
        A += v[i];
        cnt = min(cnt, res + N - i - 1);
      }
    }
    printf("Case #%d: %d\n", t, cnt);
  }
  return 0;
}
