#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int MAX;

long long gcd(long long p, long long q) {
  while ((p %= q) && (q %= p));
  return p + q;
}

int cal(long long p, long long q, int depth) {
  if (!p || depth >= MAX) {
    return 1e8;
  }
  if (p == q) {
    return depth;
  }
  int ans = 1e8;
  q /= 2;
  for (long long l = 0; l <= p; l++) {
    if (l <= q && (p - l) <= q) {
      int left = cal(l, q, depth + 1);
      int right = cal(p - l, q, depth + 1);
      ans = min(ans, min(left, right));
      MAX = min(MAX, ans);
    }
  }
  return ans;
}

int main() {
  long long T, C = 1;
  scanf("%d", &T);
  while (T--) {
    printf("Case #%d: ", C++);
    char buf[999];
    scanf("%s", buf);
    long long P, Q;
    sscanf(buf, "%lld/%lld", &P, &Q);
    int d = gcd(P, Q);
    P /= d;
    Q /= d;
    bool ok = false;
    for (long long j = 1; j <= 50 && !ok; j++) {
      long long num = ((long long)1 << j);
      if (num % Q == 0) {
        P *= num / Q;
        Q = num;
        ok = true;
        MAX = j + 1;
      }
    }
    int ans = 1e8;
    if (ok) {
      ans = cal(P, Q, 0);
    }
    if (ans < 1e8) {
      printf("%d\n", ans);
    } else {
      puts("impossible");
    }
  }
  return 0;
}
