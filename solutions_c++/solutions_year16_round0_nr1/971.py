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

void updateDigits(long long n, vector<bool> &digits, int &done) {
  for (; n; n /= 10) {
    int d = n % 10;
    if (!digits[d]) {
      digits[d] = true;
      --done;
    }
  }
}

void solve() {
  long long n;
  scanf("%lld", &n);
  if (!n) {
    printf("INSOMNIA\n");
    return;
  }
  long long dn = n;
  vector<bool> digits(10, false);
  int done = 10;
  updateDigits(n, digits, done);
  while (done) {
    n += dn;
    updateDigits(n, digits, done);
  }
  printf("%lld\n", n);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
