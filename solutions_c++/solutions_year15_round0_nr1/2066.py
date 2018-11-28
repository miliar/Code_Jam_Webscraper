/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 * Date: 2015.04.12
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int n;
char s[1003];

void solve() {
  scanf("%d%s", &n, s);
  int add = 0, cnt = 0;
  forn(i, n + 1) {
    if (cnt < i)
      add += i - cnt, cnt = i;
    cnt += s[i] - '0';
  }
  printf("%d\n", add);
}

int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}

