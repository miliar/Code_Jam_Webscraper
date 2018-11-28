#include <bits/stdc++.h>
using namespace std;

bool d[10];
int T, N;

bool check(int k) {
  while (k) {
    d[k%10] = 1;
    k /= 10;
  }
  for (int i = 0; i < 10; i++) {
    if (!d[i]) return 0;
  }
  return 1;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    scanf("%d", &N);
    if (N == 0) {
      printf("INSOMNIA\n");
      continue;
    }
    for (int i = 0; i < 10; i++) {
      d[i] = 0;
    }
    int i = 1;
    while (!check(N*i)) {
      i++;
    }
    printf("%d\n", N*i);
  }
  return 0;
}

