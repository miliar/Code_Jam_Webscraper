#include <bits/stdc++.h>
using namespace std;

char S[2005], b[11] = {"ZWXGHSRVIO"}, c[10][6] = {
  "ZERO", "ONE", "TWO", "THREE", "FOUR",
  "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
int T, a[256], d[10] = {0, 2, 6, 8, 3, 7, 4, 5, 9, 1}, e[10];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%s", S);
    for (int i = 0; i < 256; i++) {
      a[i] = 0;
    }
    for (int i = 0; S[i]; i++) {
      a[S[i]]++;
    }
    for (int i = 0; i < 10; i++) {
      e[d[i]] = a[b[i]];
      for (int j = 0; c[d[i]][j]; j++) {
        a[c[d[i]][j]] -= e[d[i]];
      }
    }
    printf("Case #%d: ", t);
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < e[i]; j++) {
        printf("%d", i);
      }
    }
    printf("\n");
  }
  return 0;
}

