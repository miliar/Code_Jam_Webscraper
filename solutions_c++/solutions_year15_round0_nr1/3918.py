#include <bits/stdc++.h>

using namespace std;

char str[1005];

int main() {
  int nt; scanf("%d", &nt);
  for (int _ = 1; _ <= nt; ++_) {
    int n; scanf("%d", &n);
    scanf("%s", str);
    int already_up = 0, answer = 0;
    for (int i = 0; i <= n; ++i) {
      if (already_up < i) {
        answer += i - already_up;
        already_up = i;
      }
      already_up += str[i] - '0';
    }
    printf("Case #%d: %d\n", _, answer);
  }
  return 0;
}