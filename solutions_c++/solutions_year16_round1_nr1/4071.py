#include <bits/stdc++.h>

using namespace std;

deque <char> dq;
char s[12345];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("out.out", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    printf("Case #%d: ", tt);
    scanf("%s", s);
    dq.push_back(s[0]);
    for (int i = 1; s[i]; i++) {
      if (s[i] < dq.front()) {
        dq.push_back(s[i]);
      } else {
        dq.push_front(s[i]);
      }
    }
    while (!dq.empty()) {
      printf("%c", dq.front());
      dq.pop_front();
    }
    puts("");
  }
	return 0;
}
