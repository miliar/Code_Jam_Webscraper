#include <cstdio>
#include <memory.h>
#include <algorithm>
using namespace std;
int t,tt,n,inf,i,j,k,r,rr,f[1010][1010],b[1010],back[1010],d[1010];
pair<int,int> a[1010];
bool u[1010];
void rec(int l, int z) {
  if (l==n) {
    int c=0;
    for (int i=0; i<n; i++) d[i]=i;
    //for (int i=0; i<n; i++) printf("%d, ",back[i]); puts("");
    for (int i=0; i<n; i++) {
      for (int j=1; j<n; j++) if (back[d[j-1]]>back[d[j]]) {
        swap(d[j-1],d[j]);
        c++;
      }
    }
    //printf("%d %d\n",c,rr);
    rr=min(rr,c);
    return;
  }
  for (int i=0; i<n; i++) if (!u[i]) {
  b[l]=a[i].first;
  back[i]=l;
  int cz=z;
  if (l>0) {
    if (z==0) {
      if (b[l]<b[l-1]) cz=1;
    } else {
      if (b[l]>b[l-1]) continue;
    }
  }
  u[i]=true;
  rec(l+1,cz);
  u[i]=false;
  }
}
int main() {
  freopen("Bs.in","r",stdin);
  freopen("Bs.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
    for (i=0; i<n; i++) {
      scanf("%d",&a[i].first);
      a[i].second=i;
    }
    rr=1000000000;
    rec(0,0);/*
    sort(a,a+n);
    memset(f,120,sizeof(f));
    r=inf=f[0][0];
    f[0][0]=0;
    for (i=0; i<n; i++) for (j=0; j<=i; j++) if (f[i][j]<inf) {
      if (i==n-1) {
        r=min(r,f[i][j]+abs(i-j-a[i].second));
      } else {
        f[i+1][j]=min(f[i+1][j],f[i][j]+abs(i-j-a[i].second));
        f[i+1][j+1]=min(f[i+1][j+1],f[i][j]+abs(n-1-j-a[i].second));
      }
    }*/
    //if (r&1) puts("!!!!");
    //if (r==inf) puts("~~~~");
    printf("Case #%d: %d\n",t,rr);
    //printf("Case #%d: %d %d %d\n",t,r/2,rr,r==rr);
    //if (r/2>rr) break;
    //break;
  }
  return 0;
}
