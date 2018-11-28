#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int kMaxn = 22;

char s[kMaxn];
double f[1 << kMaxn];
int n;
int main() {
  int tn, cp;
  for (scanf("%d", &tn), cp = 1; cp <= tn; cp++) {
    scanf("%s", s);
    n = strlen(s);
    int init = 0;
    for (int i = 0; i < n; i++)
      if (s[i] == 'X') init |= (1 << i);
    memset(f, 0, sizeof f);
    for (int mask = (1 << n) - 1; mask > init; mask--) {
      for (int i = 0; i < n; i++) {
        if ((mask & (1 << i)) == 0) continue;
        int tmask = (mask ^ (1 << i));
        int k = i, t = n;
        while (t > 0 && (mask & (1 << k)) > 0) {
          f[tmask] += (f[mask] + t) / n;
          --t;
          --k;
          if (k == -1) k = n - 1;
        }
      }
    }
    printf("Case #%d: %.9lf\n", cp, f[init]);
  }
  return 0;
}
