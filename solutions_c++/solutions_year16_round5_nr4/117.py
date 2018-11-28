#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,i,j;
char s[102][102],b[102];
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    for (i=0; i<n; i++) scanf("%s",s[i]);
    scanf("%s",b);
    printf("Case #%d: ",t);
    for (i=0; i<n; i++) {
      for (j=0; j<m; j++) if (s[i][j]!=b[j]) break;
      if (j>=m) { puts("IMPOSSIBLE"); break; }
    }
    if (i<n) continue;
    if (m==1) {
      puts("? 0");
      continue;
    }
    for (i=1; i<m; i++) putchar('?');
    printf(" 10?");
    for (i=0; i<m; i++) printf("10");
    putchar('\n');
    fprintf(stderr,"Case #%d\n",t);
  }
  return 0;
}
