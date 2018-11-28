#include <bits/stdc++.h>
using namespace std;
char s[20005];
int solve() {
  scanf("%s", s);
  int n = strlen(s);
  stack<char> st;
  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (!st.empty() && s[i] == st.top()) {
      st.pop();
      ans++;
    } else {
      st.push(s[i]);
    }
  }
  return 5 * (n / 2 + ans);
}
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: %d\n", t, solve());
  }
  return 0;
}


