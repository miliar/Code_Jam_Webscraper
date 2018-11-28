#include <bits/stdc++.h>
using namespace std;

int t, k, c, s;

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt<=t; tt++) {
    scanf("%d%d%d", &k, &c, &s);
    printf("Case #%d:", tt);
    for (int i = 1; i<=k; i++) {
      printf(" %d", i);
    }
    printf("\n");
  }
}
