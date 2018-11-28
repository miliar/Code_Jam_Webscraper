#include <bits/stdc++.h>
using namespace std;
int t,tt,i,n,m,r;
char a[20200],s[20200];
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%s",s);
    n=strlen(s);
    for (r=m=i=0; i<n; i++) if (m>0 && a[m]==s[i]) { m--; r++; } else a[++m]=s[i];
    printf("Case #%d: %d\n",t,r*10+(m/2)*5);
    fprintf(stderr,"Case #%d\n",t);
  }
  return 0;
}
