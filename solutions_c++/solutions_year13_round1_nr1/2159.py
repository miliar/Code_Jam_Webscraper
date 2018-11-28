#include<stdio.h>
#include<math.h>

main()
{
  freopen("h.in","r",stdin);
  freopen("h.out","w",stdout);
  
  long long T,r,t,k,a,b;
  int TT=0;
  double sq;
  
  scanf("%lld",&T);
  while(T>0)
  {
    TT++;
    T--;
    scanf("%lld%lld",&r,&t);
    
    a=4*r*r-4*r+1+8*t;
    sq=sqrt(a)-2*r-3;
    
    k=(long long)(sq/4);
    
    printf("Case #%d: %lld\n",TT,k+1);
  }
}
