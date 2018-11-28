/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home

int arr[1000002];

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  int n, p, q, rr, s;
  scanf("%d%d%d%d%d", &n, &p, &q, &rr, &s);
  long long all = 0;
  for (int i = 0; i < n; ++i) {
    arr[i] = (1LL * i * p + q) % rr + s;
    all += arr[i];
  }
  long long mn = all;
  int l = 0, r = 0;
  long long cur = arr[0], left = 0;
  for (int i = 0; i < n; ++i) {
    mn = min(mn, max(left, max(cur, all - cur - left)));
    while (r + 1 < n && cur < all - left - cur) {
      cur += arr[r + 1];
      ++r;
      mn = min(mn, max(left, max(cur, all - cur - left)));
    }
    // cout << i << "  " << left << "  " << cur << " " << all - cur - left << endl;
    left += arr[l]; cur -= arr[l];
    ++l;
  }
  printf("%.15lf\n", 1.0 * (all - mn) / all);
}

int main() {
// #ifndef Fdg_Home
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
// #endif
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}