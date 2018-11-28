#include <iostream>
#include <string>
#include <cstdio>
using namespace std;


int peeps[1001];

void solve(int CASE) {
  int delta, n = 0, seen = 0;

  cin >> delta;

  if (delta == 0) {
    printf("Case #%d: INSOMNIA\n", CASE);
    return;
  }

  while (seen != 0x3FF) {
    n += delta;
    int y = n;
    while (y) {
      seen |= 1 << (y%10);
      y /= 10;
    }
  }

  printf("Case #%d: %d\n", CASE, n);
}

int main() {
  int T;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    solve(i);
  }

  return 0;
}
