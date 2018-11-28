#include <bits/stdc++.h>

using namespace std;

char s[123456];
int n;

int solve(int i, char c) {
  if (i < 0) {
    return 0;
  }
  if (s[i] == c) {
    return solve(i - 1, c);
  } else {
    return 1 + solve(i - 1, s[i]);
  }
}

int main() {
  freopen("/home/youssef/Downloads/B-large.in", "r", stdin);
  freopen("out.out", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    printf("Case #%d: ", tt);
    scanf("%s", s);
    n = strlen(s);
    printf("%d\n", solve(n - 1, '+'));
  }
  return 0;
}
