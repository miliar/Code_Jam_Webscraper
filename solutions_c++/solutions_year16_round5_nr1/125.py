#include <bits/stdc++.h>
using namespace std;

int n;
char s[20005];
int t;
int aaaa;

stack<char> c;
int main() {
  scanf("%d", &t);
  for (int cs = 1; cs <= t; cs++) {
    scanf("%s", s);
    n = strlen(s);
    int res = 0;
    while (!c.empty()) {
      c.pop();
    }
    for (int i = 0; i < n; i++) {
      if (c.size() > 0 && c.top() == s[i]) {
        res += 10;
        c.pop();
      } else {
        c.push(s[i]);
      }
    }
    res += (c.size() / 2 * 5);
    printf("Case #%d: %d\n", cs, res);
  }
}
