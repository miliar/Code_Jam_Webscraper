#include <bits/stdc++.h>

using namespace std;

int seen[10];

bool all_seen(int caso) {
  for (int i = 0; i < 10; ++i) {
    if (seen[i] != caso) return false;
  }
  return true;
}

void do_it(int n, int caso) {
  if (n == 0) seen[0] = caso;
  while (n > 0) {
    int x = n % 10;
    n /= 10;
    seen[x] = caso;
  }
}

long long tries(int caso, int n) {
  for (int i = 0; i < 1000000; ++i) {
    do_it(n * (i + 1), caso);
    if (all_seen(caso)) return i + 1;
  }
  return -1;
}

int main() {
  int nt; scanf("%d", &nt);
  for (int caso = 1; caso <= nt; ++caso) {
    int n; scanf("%d", &n);
    if (n == 0) printf("Case #%d: INSOMNIA\n", caso);
    else printf("Case #%d: %lld\n", caso, tries(caso, n) * n);
  }
  return 0;
}