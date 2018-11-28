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

const int MAXN = 10007;

int main() {
  int T, N;
  int m[MAXN];
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
      scanf("%d", &m[i]);
    }
    int ans1 = 0, ans2 = 0;
    for (int i = 1; i < N; ++i) {
      if (m[i - 1] > m[i]) {
        ans1 += m[i - 1] - m[i];
      }
    }
    int maxSpeed = 0;
    for (int i = 1; i < N; ++i) {
      if (m[i - 1] - m[i] > 0) {
        maxSpeed = MAX(maxSpeed, m[i - 1] - m[i]);
      }
    }
    for (int i = 1; i < N; ++i) {
      ans2 += MIN(maxSpeed, m[i - 1]);
    }
    printf("Case #%d: %d %d\n", t, ans1, ans2);
  }
  return 0;
}
