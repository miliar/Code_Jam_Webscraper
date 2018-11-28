#include <cstdio>
using namespace std;
int t,tt,n,i,j,r;
bool bad,g[28][28],u[28],w[28];
char s[28];
void check(int l) {
  if (l==n) return;
  for (int i=0; i<n; i++) if (!u[i]) {
    u[i]=true;
    bool was=false;
    for (int j=0; j<n; j++) if (!w[j] && g[i][j]) {
      w[j]=was=true;
      check(l+1);
      w[j]=false;
    }
    if (!was) bad=true;
    u[i]=false;
  }
}
void rec(int x, int y, int s) {
  if (s>=r) return;
  if (y==n) { x++; y=0; }
  if (x==n) {
    bad=false;
    check(0);
    if (!bad) r=s;
    return;
  }
  if (!g[x][y]) {
    rec(x,y+1,s);
    g[x][y]=true;
    rec(x,y+1,s+1);
    g[x][y]=false;
  } else rec(x,y+1,s);
}
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
    for (r=i=0; i<n; i++) {
      scanf("%s",s);
      for (j=0; j<n; j++) {
        g[i][j]=(s[j]=='1');
        if (s[j]=='0') r++;
      }
    }
    rec(0,0,0);
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}
