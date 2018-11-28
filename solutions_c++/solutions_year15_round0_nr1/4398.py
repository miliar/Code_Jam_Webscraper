#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int t;
  scanf("%d ",&t);
  for (int cs=1;cs<=t;cs++) {
    int  l,r=0;
    char a[1001];
    scanf("%d%s\n",&l,a);
    int c=a[0]-'0';
    for (int i=1;i<l+1;i++) {
      if (c<i) {
        r+=i-c;
        c+=i-c;
      }
      c+=a[i]-'0';
    }
    printf("Case #%d: %d\n",cs,r);
  }
}
