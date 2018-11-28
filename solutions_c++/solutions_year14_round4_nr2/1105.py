#include<stdio.h>
#include<algorithm>

using namespace std;

int T,TT,n,a[11];
int p[11];
int best,cnt;

int main() {
  int i,j,k;
  p[0]=1;
  for(i=1;i<=10;i++)p[i]=p[i-1]<<1;
  scanf("%d",&T);
  for(TT=1;TT<=T;TT++) {
    scanf("%d",&n);
    for(i=0;i<n;i++)scanf("%d",&a[i]);
    best=1000;
    for(k=0;k<p[n];k++){
      cnt=0;

      for(i=0;i<n;i++)
        for(j=i+1;j<n;j++)
          cnt+=((k&p[i]) && !(k&p[j]) ? 1 : 0);

      for(i=0;i<n;i++)if(!(k&p[i]))
        for(j=i+1;j<n;j++)if(!(k&p[j]))
          cnt+=(a[i] > a[j] ? 1 : 0);

      for(i=0;i<n;i++)if((k&p[i]))
        for(j=i+1;j<n;j++)if((k&p[j]))
          cnt+=(a[i] < a[j] ? 1 : 0);

      best=min(best,cnt);
    }
    printf("Case #%d: %d\n",TT,best);
  }
  return 0;
}
