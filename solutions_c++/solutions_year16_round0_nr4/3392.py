#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  int t; cin >> t;
  for (int i = 1; i <= t; i++) {
    int k, c, s; cin >> k >> c >> s;
    printf("Case #%d:", i);
    for (int i = 1; i <= k; i++) printf(" %d", i);
    printf("\n");
  }
  return 0;
}
