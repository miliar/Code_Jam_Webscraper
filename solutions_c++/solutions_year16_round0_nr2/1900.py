#include <bits/stdc++.h>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; ++caso) {
    string inp;
    cin >> inp;
    int ans = 0;
    char last = inp[0];
    for (int i = 1; i < inp.size(); ++i) {
      if (inp[i] != last) {
        ++ans;
        last = inp[i];
      }
    }
    if (last == '-') ++ans;
    printf("Case #%d: %d\n", caso, ans);
  }
  return 0;
}