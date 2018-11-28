#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

#define MAXN 1010

int n, v[MAXN];

int main() {
  int nt, nteste=1, ans, mx, t;
  scanf("%d", &nt);
  while (nt--) {
    scanf("%d", &n);
    mx = 0;
    for (int i=0; i<n; i++)
      scanf("%d", &v[i]), mx = max(mx, v[i]);
    ans = 0x3f3f3f3f;
    for (int k=1; k<=mx; k++) {
      t = 0;
      for (int i=0; i<n; i++)
        t += int(ceil(double(v[i])/k)) - 1;
      ans = min(ans, t + k);
    }
    printf("Case #%d: %d\n", nteste++, ans);
  }

  return 0;
}