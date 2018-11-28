#include <cstdio>
#include <algorithm>
using namespace std;
int main(){
    double C,F,X,ans,sum=0.0,a=2,d=1;
    int T,farm;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%lf%lf%lf",&C,&F,&X);
        sum=ans=X/2.0,d=1,a=2;
      while(sum<=ans){
            sum-=X/a;
            sum+=C/a;
            a=2+d*F;
            sum+=X/a;
            d++;
            ans=min(sum,ans);
      }
      printf("Case #%d: %.7lf\n",i,ans);
    }
   return 0;
}

