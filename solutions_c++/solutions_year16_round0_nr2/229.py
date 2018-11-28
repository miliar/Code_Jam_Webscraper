#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100 + 10;
char s[MAXN];

void run(int cas) {
  printf("Case #%d: ", cas);
  scanf("%s", s);
  int n = strlen(s);
  n = unique(s, s + n) - s;
  if (s[n - 1] == '+') --n;
  printf("%d\n", n);
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) run(cas);
  return 0;
}
