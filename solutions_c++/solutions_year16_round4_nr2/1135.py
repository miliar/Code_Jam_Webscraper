//TooSimple!
#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
double p[20],q[20];
double f[20][20];
int main(){
   freopen("bs.in","r",stdin);
   freopen("bs.out","w",stdout);
   int t,k,n;
   scanf("%d",&t);
   for(int tt=1;tt<=t;tt++){
      cerr<<"t="<<tt<<endl;
      scanf("%d %d",&n,&k);
      for(int i=0;i<n;i++)scanf("%lf",p+i);
      double ans=0.0;
      for(int b=0;b<(1<<n);b++){
         if(__builtin_popcount(b)!=k)continue;
         int c=0;
         for(int i=0;i<n;i++)if(b&(1<<i))q[c++]=p[i];
         for(int i=0;i<=c;i++)for(int j=0;j<=c;j++)f[i][j]=0;
         f[c][k/2]=1.0;
         for(int i=c-1;i>=0;i--){
            for(int y=0;y<=k/2;y++){
               f[i][y]=q[i]*f[i+1][y+1] + (1.0-q[i])*f[i+1][y];
            }
         }
         double bet=f[0][0];
         ans=max(ans,bet);
      }
      printf("Case #%d: %.8lf\n",tt,ans);
   }
   return 0;
}
