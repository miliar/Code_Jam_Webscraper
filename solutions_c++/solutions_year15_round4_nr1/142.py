#include <bits/stdc++.h>
using namespace std;
const int dx[4]={-1,0,1,0};
const int dy[4]={0,-1,0,1};
const char dz[4]={'^','<','v','>'};
int t,tt,n,m,i,j,k,x,y,r;
char s[111][111];
bool q;
bool valid(int x, int y) {
  return (x>=0 && x<n && y>=0 && y<m);
}
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m); q=true;
    for (i=0; i<n; i++) scanf("%s",s[i]);
    for (r=i=0; i<n; i++) for (j=0; j<m; j++) if (q && s[i][j]!='.') {
      for (k=0; k<4; k++) if (dz[k]==s[i][j]) break;
      for (x=i+dx[k], y=j+dy[k]; valid(x,y); x+=dx[k], y+=dy[k]) if (s[x][y]!='.') break;
      if (valid(x,y)) continue;
      for (k=0; k<4; k++) {
        for (x=i+dx[k], y=j+dy[k]; valid(x,y); x+=dx[k], y+=dy[k]) if (s[x][y]!='.') break;
        if (valid(x,y)) break;
      }
      if (k<4) r++; else q=false;
    }
    printf("Case #%d: ",t);
    if (q) printf("%d\n",r); else puts("IMPOSSIBLE");
    fprintf(stderr,"Case #%d\n",t);
  }
  return 0;
}
