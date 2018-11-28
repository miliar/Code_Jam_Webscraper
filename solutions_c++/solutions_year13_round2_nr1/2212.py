#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std; 

int _c, m, n, res, in[105];
bool f;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
  scanf ("%d", &_c);
  for (int c = 1; c <= _c; c++) {
    f = false;
    res = 0;
    scanf ("%d%d", &m, &n);
    for (int i = 0; i < n; i++) scanf ("%d", &in[i]);
    sort (in, in + n);
    for (int i = 0; i < n; i++) {
      if (m <= in[i]) {
        for (int j = 0, _m = m; ; _m += _m - 1, j++) {
          if (n - i <= j) {
            res += n - i;
            f = true;
            break;
          }
          if (_m > in[i]) {
            res += j;
            m = _m;
            break;
          }
        }
      }
      if (f) break;
      m += in[i];
    }
    printf ("Case #%d: %d\n", c, res);
  }
	return 0;
}