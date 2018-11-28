#include <bits/stdc++.h>
using namespace std;

char str[105];
int n, t;

int main() {
  scanf("%d", &t);
  for(int tt = 1; tt<=t; tt++) {
    int ans = 0;
    scanf("%s", str);
    n = strlen(str);
    for (int i = 1; i<n; i++) {
      if(str[i]==str[0]) continue;
      str[0] = (str[0]=='-')?'+':'-';
      ans++;
    }
    if(str[0] == '-') ans++;
    printf("Case #%d: %d\n", tt, ans);
  }
}
