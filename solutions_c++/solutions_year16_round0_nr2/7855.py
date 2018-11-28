#include <bits/stdc++.h>
using namespace std;

char s[1234];

int main() {
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  int T;
  scanf("%d", &T);
  for(int cs = 1; cs <= T; cs++) {
    scanf("%s", s);
    int l = strlen(s);
    int nu = 0, ans = 0;
    for(int i = l - 1; i >= 0; i--) {
      if(nu == 0) {
        if(s[i] == '-') nu ^= 1, ans++;
      }
      else {
        if(s[i] == '+') nu ^= 1, ans++;
      }
    }
    printf("Case #%d: %d\n", cs, ans);
  }
  return 0;
}
