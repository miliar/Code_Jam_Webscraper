#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdio>
#include <string>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef pair<int,int> pii;
int t,tt,n,i,r,a[2020],ok[2020];
bool e[2020],u[2020],w[22][2020];
char s[5];
void rec(int l, int c) {
  if (l==n) {
    bool q=true;
    for (int j=l-1; j>=0; j--) if (e[j] && a[j]>0) {
      if (!u[j] && w[l][a[j]]) q=false;
      w[l][a[j]]=true;
    }
    for (int j=l-1; j>=0; j--) if (e[j] && a[j]>0) w[l][a[j]]=false;
    if (q) r=min(r,c);
    return;
  }
  if (e[l]) {
    rec(l+1,c+1);
    return;
  }
  for (int j=l-1; j>=0; j--) {
    if (e[j] && !u[j]) {
      u[j]=true;
      ok[l]=j;
      if (a[l]==0) {
        if (a[j]==0) rec(l+1,c-1); else 
          if (!w[l][a[j]]) rec(l+1,c-1);
      } else if (!w[l][a[l]]) {
        if (a[j]==0 || a[j]==a[l]) rec(l+1,c-1);
      }
      u[j]=false;
    }
    if (a[j]) w[l][a[j]]=true;
  }
  ok[l]=-1;
  if (a[l]==0 || !w[l][a[l]]) rec(l+1,c);
  for (int j=0; j<l; j++) if (a[j]) w[l][a[j]]=false;
}
int main() {
  //freopen("in","r",stdin);
  freopen("Cs.in","r",stdin);
  freopen("Cs.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
    for (i=0; i<n; i++) {
      scanf("%s",s);
      e[i]=(s[0]=='E');
      scanf("%d",&a[i]);
    }
    r=2020;
    rec(0,0);
    printf("Case #%d: ",t);
    if (r==2020) puts("CRIME TIME"); else printf("%d\n",r);
  }
  return 0;
}
