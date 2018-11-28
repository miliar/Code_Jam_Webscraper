#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int kMaxn = 1010;
const int kMod = 1000002013;

struct Node {
  int pos, type, p;
  friend bool operator < (const Node &a, const Node &b) {
    return a.pos < b.pos || (a.pos == b.pos && a.type > b.type);
  }
} a[kMaxn << 1];
Node stack[kMaxn << 1];
int stn;
int an;
int n, m;
long long calc(long long n) {
  return (n * n + n - 2) / 2 % kMod;
}
int main() {
  int T, cp;
  for (scanf("%d", &T), cp = 1; cp <= T; cp++) {
    scanf("%d%d", &n, &m);
    an = 0;
    int tot = 0;
    for (int i = 0; i < m; i++) {
      int o, e, pi;
      scanf("%d%d%d", &o, &e, &pi);
      tot += (long long)pi * calc(e - o) % kMod;
      tot %= kMod;
      a[an].pos = o;
      a[an].type = 1;
      a[an++].p = pi;

      a[an].pos = e;
      a[an].type = -1;
      a[an++].p = pi;
    }
    sort(a, a + an);
    stn = 0;
    int ans = 0;
    for (int i = 0; i < an; i++) {
      if (a[i].type == 1) {
        stack[++stn] = a[i];
      } else {
        for (int x = a[i].p; x; ) {
          long long d = min(stack[stn].p, x);
          ans += d * calc(a[i].pos - stack[stn].pos) % kMod;
          ans %= kMod;
          stack[stn].p -= d;
          x -= d;
          if (stack[stn].p == 0) --stn;
        }
      }
    }
    ans = ans - tot;
    if (ans < 0) ans += kMod;
    printf("Case #%d: %d\n", cp, ans);
  }
  return 0;
}
