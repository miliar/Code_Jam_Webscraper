#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <string>
#include <set>
#include <utility>
#include <vector>

using namespace std;

template <typename T> inline T MIN(T a, T b) { return a < b ? a : b; }
template <typename T> inline T MAX(T a, T b) { return a < b ? b : a; }
template <typename T> inline T ABS(T a)      { return a < 0 ? -a : a;}

typedef long long int64;

const int MAXN = 1007;

inline bool cmp(int a, int b) {
  return a > b;
}

int main() {
  int T, D;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d", &D);
    vector<int> P(D + 1, 0);
    for (int i = 0; i < D; ++i) {
      scanf("%d", &P[i]);
    }
    sort(P.begin(), P.end(), cmp);

    int opt = INT_MAX;
    for (int i = 1; i <= P[0]; ++i) {
      int cnt = 0;
      for (int j = 0; j < D; ++j) {
        if (P[j] < i) {
          break;
        }
        cnt += ceil(1. * P[j] / i) - 1;
      }
      opt = MIN(opt, cnt + i);
    }
    printf("Case #%d: %d\n", t, opt);
  }
  return 0;
}
