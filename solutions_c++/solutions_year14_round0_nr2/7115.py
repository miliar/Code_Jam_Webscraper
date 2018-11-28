#include<cstdio>
#include<algorithm>
typedef long double LL;
using namespace std;
main()
{
 LL c,x,t,f,i,r,time;
 scanf("%Lf",&t);
 for(i=1;i<=t;i++)
 {
  
scanf("%Lf%Lf%Lf",&c,&f,&x);
  r=2;
  time=0;
  while(true)
  {
   if((c/r+x/(r+f))<x/r)
    {   
     time+=c/r;
    r+=f;
    }
   else
    {
      time+=x/r;
       break;    
    }
  }

  printf("Case #%.0Lf: %.7Lf\n",i,time);
 }

return 0;
}


