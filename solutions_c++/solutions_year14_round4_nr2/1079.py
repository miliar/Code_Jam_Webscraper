#include <iostream>
using namespace std;
int c[1000];
int n;
int a[1000], b[1000];
int na, nb;

int GetAns1() {
  int ans = 2147473647;
  for (int k = 0; k < (1 << n); ++k) {
    na = 0;
    nb = 0;
    for (int i = 0; i < n; ++i)
      if ((1 << i) & k) {
        a[na++] = i;
      } else {
        b[nb++] = i;
      }
    int count = 0;
    for (int i = 0; i < na; ++i) {
      for (int j = i + 1; j < na; ++j) {
        if (c[a[i]] > c[a[j]]) ++count;
      }
      for (int j = 0; j < nb; ++j) {
        if (a[i] > b[j]) ++count;
      }
    }
    for (int i = 0; i < nb; ++i)
      for (int j = i + 1; j < nb; ++j) {
        if (c[b[i]] < c[b[j]]) ++count;
      }
    if (count < ans) ans = count;
  }
  return ans;
}

int main() {
  int tc;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%d", &c[i]);
    int ans = GetAns1();
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
