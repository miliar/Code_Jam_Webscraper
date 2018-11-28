#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;


const int kMaxn = 40;

long long x[kMaxn];
long long B;
int n;
long long check(int k, long long l) {
  long long m = B;
  for (int i = 0; i < k; i++) {
    if (x[i] > l) return -1;
    m -= l - x[i];
  }
  for (int i = k; i < 37; i++) {
    if (x[i] < l + 1) m -= l + 1 - x[i];
  }
  return m;
}
double calc(int k) {
  long long ret = 0;
  long long left = 1, right = max(x[36], B), mid;
  while (left <= right) {
    mid = left + ((right - left) >> 1);
    if (check(k, mid) >= 0) {
      ret = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  double ans = 0;
  for (int dt = -5000; dt <= 5000; dt++) {
    int cc = dt + mid;
    double tmp = check(k, cc);
    if (tmp < 0) continue;
    for (int i = 0; i < k; i++) {
      double c = cc - x[i];
      c *= 36;
      tmp += c / k;
    }
    ans = max(ans, tmp);
  }
  return ans;
}
int main() {
  int tn, cp;
  for (scanf("%d", &tn), cp = 1; cp <= tn; cp++) {
    scanf("%lld%d", &B, &n);
    memset(x, 0, sizeof x);
    for (int i = 0; i < n; i++) scanf("%lld", x + i);
    sort(x, x + 37);
    double ans = 0;
    for (int i = 1; i <= 37; i++) {
      ans = max(ans, calc(i) - B);
    }
    printf("Case #%d: %.8lf\n", cp, ans);
  }
  return 0;
}
