#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

int u, n;
char s[N];

void flip(char &u) {
  if (u == '-') {
    u = '+';
  } else {
    u = '-';
  }
}

int main() {
//  freopen("input.txt", "r", stdin);
//  freopen("output.txt", "w", stdout);
  int tc;
  scanf("%d", &tc);
  for (int test = 1; test <= tc; test++) {
    scanf("%s", s + 1);
    scanf("%d", &u);
    n = strlen(s + 1);
    int res = 0;
    for (int i = 1; i <= n - u + 1; i++) {
      if (s[i] == '-') {
        res++;
        for (int j = 0; j < u; j++) {
          flip(s[j + i]);
        }
      }
    }
    int f = 0;
    for (int i = 1; i <= n; i++) {
      if (s[i] != '+') {
        f = 1;
        break;
      }
    }
    printf("Case #%d: ", test);
    if (f) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", res);
    }
  }
  return 0;
}
