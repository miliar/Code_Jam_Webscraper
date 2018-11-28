#include<cstdio>
#include<algorithm>
using namespace std;
const int N=222;
int T,C,i,j,k,K,n,m;double a[N],b[N],ans,f[N][N];
int main(){
  scanf("%d",&T);
  for(C=1;C<=T;C++){
    scanf("%d%d",&n,&K);
    for(i=1;i<=n;i++)scanf("%lf",&a[i]);
    sort(a+1,a+n+1);
    ans=0;
    for(i=0;i<=K;i++){
      if(n-K+i+1>n+1)continue;
      for(m=0,j=1;j<=i;j++)b[++m]=a[j];
      for(j=n-K+i+1;j<=n;j++)b[++m]=a[j];
      for(j=0;j<=m;j++)for(k=0;k<=m;k++)f[j][k]=0;
      f[0][0]=1;
      for(j=1;j<=m;j++)for(k=0;k<=m;k++){
        f[j][k]=f[j-1][k]*(1.0-b[j]);
        if(k)f[j][k]+=f[j-1][k-1]*b[j];
      }
      ans=max(ans,f[m][m/2]);
    }
    printf("Case #%d: %.9f\n",C,ans);
  }
  return 0;
}