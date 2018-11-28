#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

static const int N = 101;
vector<long long> results[N][N];

void solve() {
  int k, c, s;
  scanf("%d%d%d", &k, &c, &s);
  if (results[k][c].size() > (size_t)s) printf("IMPOSSIBLE\n");
  else {
    for (size_t i = 0; i < results[k][c].size(); ++i) {
      printf("%lld ", results[k][c][i] + 1);
    }
    printf("\n");
  }
}

long long myPow(long long a, long long b) {
  long long ret = 1;
  while (b--) ret *= a;
  return ret;
}

void init(int k, int c) {
  for (int i = 0; i < k; i += c) {
    long long n = 0;
    long long pw = 1;
    for (int j = 0; j < c && i + j < k; ++j) {
      n += (i + j) * pw;
      pw *= k;
    }
    results[k][c].push_back(n);
  }
}

void init() {
  for (int k = 1; k < N; ++k) {
    for (int c = 1; c < N; ++c) {
      init(k, c);
    }
  }
}
int main() {
  int t;
  init();
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
