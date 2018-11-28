#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#define LEN 100005

double C,F,X;
double time_BF[LEN];
double bake_R[LEN];
double time_toX[LEN];
double ans;


int main(void)
{
  int tc,tt;
  scanf("%d",&tt);
  for(int tc=1;tc<=tt;++tc){
    scanf("%lf%lf%lf",&C,&F,&X);
    time_BF[0]=0.0;
    bake_R[0]=2.0;
    time_toX[0]=X/bake_R[0];
    ans=time_toX[0];
    for(int i=1;i<LEN;++i){
      time_BF[i]=time_BF[i-1]+C/bake_R[i-1];
      if(time_BF[i]>ans)break;
      bake_R[i]=bake_R[i-1]+F;
      time_toX[i]=time_BF[i]+X/bake_R[i];
      ans=std::min(time_toX[i],ans);
    }
    printf("Case #%d: %.7f\n",tc,ans);
  }
  return 0;
}
