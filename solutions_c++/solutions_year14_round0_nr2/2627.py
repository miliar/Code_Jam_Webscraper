#include <cstdio>

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    double C,F,X;
    scanf("%lf%lf%lf",&C,&F,&X);
    double p=2,m=X/p,tm=0;
    while(tm<m){
      tm+=C/p;
      p+=F;
      if(m>tm+X/p){
	m=tm+X/p;
      }
    }
    printf("Case #%d: %.7lf\n",t,m);
  }
  return 0;
}
