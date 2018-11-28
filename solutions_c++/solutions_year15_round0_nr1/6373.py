#include <bits/stdc++.h>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int c=1; c<=t; c++) {
    int sm;
    cin >> sm;
    int extra = 0;
    int current = 0;
    string s;
    cin >> s;
    for (int i=0; i<=sm; i++) {
      int num = s[i]-'0';
      if (current >= i) {
        current += num;
      } else {
        extra += i-current;
        current += i-current;
        current += num;
      }
    }
    printf("Case #%d: %d\n", c, extra);
  }
}
