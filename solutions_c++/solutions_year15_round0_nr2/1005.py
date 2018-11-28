#include <iostream>
#include <string>
#define INF 1000000000
using namespace std;

int solve() {
  int n, a[1024];
  cin >> n;
  int maxn = 0;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    maxn = max(maxn, a[i]);
  }
  int ans = INF;
  for (int i = 1; i <= maxn; i++) {
    int now = 0;
    for (int j = 0; j < n; j++) {
      now += (a[j] / i - 1) + (a[j] % i > 0);
    }
    ans = min(ans, now + i);
  }
  return ans;
}

int main() {
  int _;
  cin >> _;
  for (int i = 1; i <= _; i++) {
    printf("Case #%d: %d\n", i, solve());
  }
}
