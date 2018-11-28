#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    char s[111];
    scanf("%s", s);
    int n = strlen(s), res = 0;
    bool sawPlus = false, sawMinus = false;
    for (int i = 0; i < n; ++i) {
      if (s[i] == '+') {
        res += sawMinus;
        sawPlus = true;
        sawMinus = false;
      } else {
        if (sawPlus)
          ++res;
        sawPlus = false;
        sawMinus = true;
      }
    }
    printf("Case #%d: %d\n", tst++, res + sawMinus);
  }
}
