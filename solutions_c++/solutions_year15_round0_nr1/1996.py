#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n;
    cin >> n;
    char s[1042];
    scanf("%s", s);

    int have = 0, need = 0, res = 0;

    int len = strlen(s);

    for (int i = 0; i < len; ++i) {
      int cur = s[i] - '0';

      if (have < need) {
        res += need - have;
        have = need;
      }

      have += cur;
      ++need;
    }

    cout << "Case #" << tt << ": " << res << endl;
  }
}
