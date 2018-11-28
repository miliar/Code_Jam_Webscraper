#include<cstdio>
#include<algorithm>
using namespace std;
main(){
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    double C,F,X;
    scanf("%lf %lf %lf",&C,&F,&X);
    long double cur=0,time=0,ans=1e10,cnt=2;
    while(time<ans){
      ans=min(ans,time+(cur>X?0:(X-cur)/cnt));
      long double needs=(C-cur)/cnt;
      time+=needs;
      cur=0;
      cnt+=F;
    }
    printf("Case #%d: %.7lf\n",t,(double)ans);
  }
}
