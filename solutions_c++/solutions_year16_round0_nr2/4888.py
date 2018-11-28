#include <bits/stdc++.h>
using namespace std;

char S[105], curr;
int T, n, flip;

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%s", S);
    n = strlen(S);
    flip = 0;
    curr = '+';
    for (int i = n-1; i >= 0; i--) {
      if (S[i] == curr) continue;
      curr = S[i];
      flip++;
    }
    printf("Case #%d: %d\n", t, flip);
  }
  return 0;
}

