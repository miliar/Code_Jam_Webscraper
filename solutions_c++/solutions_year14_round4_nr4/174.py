#include <cstdio>
#include <memory.h>
using namespace std;
int t,tt,r,cr,i,j,k,n,m,num,a[111],b[111][26],cnt[111],mask[111],d[111],cc[1<<16];
char s[111];
void dfs(int i) {
  mask[i]=0;
  cnt[i]=0;
  if (a[i]>=0) mask[i]|=(1<<d[a[i]]);
  for (int j=0; j<26; j++) if (b[i][j]) {
    dfs(b[i][j]);
    cnt[i]+=cnt[b[i][j]];
    mask[i]|=mask[b[i][j]];
  }
  cnt[i]+=cc[mask[i]];
}
void rec(int l) {
  if (l==n) {
    dfs(0);
    if (cnt[0]>r) {
      r=cnt[0];
      cr=0;
    }
    if (cnt[0]==r) cr++;
    return;
  }
  for (int i=0; i<m; i++) {
    d[l]=i;
    rec(l+1);
  }
}
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (i=1; i<(1<<16); i++) cc[i]+=cc[i/2]+(i&1);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    memset(a,255,sizeof(a));
    memset(b,0,sizeof(b));
    for (num=r=i=0; i<n; i++) {
      scanf("%s",s);
      for (j=k=0; s[j]!=0; j++) {
        int cur=s[j]-'A';
        if (b[k][cur]==0) b[k][cur]=++num;
        k=b[k][cur];
      }
      a[k]=i;
    }
    r=cr=0;
    rec(0);
    printf("Case #%d: %d %d\n",t,r,cr);
  }
  return 0;
}
