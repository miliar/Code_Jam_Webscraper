#include <bits/stdc++.h>
using namespace std;
int main() {
  int T;
  scanf("%d\n",&T);
  for (int ts=1;ts<=T;ts++) {
    string s;
    cin >> s;
    s = s + '+';
    int ans = 0;
    for (int i=1;i<s.length();i++) {
      if (s[i-1] != s[i]) ans++;
    }
    printf("Case #%d: %d\n",ts,ans);
  }
}