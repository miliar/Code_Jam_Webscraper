#include <bits/stdc++.h>
using namespace std;

int T, ans, c;
char s[5000];

int main(){

  scanf("%d", &T);
  for(int ct = 1; ct <= T; ct ++){
    scanf("%*d %s", s);
    ans = c = 0;
    for(int i = 0; s[i]; i ++){
      ans = max(ans, i - c);
      c += (int)(s[i] - '0');
    }
    printf("Case #%d: %d\n", ct, ans);
  }
  
  return 0;
}
