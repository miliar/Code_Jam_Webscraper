#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
  int main()
  {
freopen("B-large.in.txt", "r", stdin);
freopen("output.txt", "w", stdout);
      int t,k;
   double c,f,x,t1,t2,t3,ans,i;
   scanf("%d",&t);
for(k=1;k<=t;k++)
    { ans=0.0;
scanf("%lf%lf%lf",&c,&f,&x);
i=2;
 while(i)
    {
        t1=c/i;
       t2=x/(i+f);
       t2+=t1;
       t3=x/i;

         //printf("%lf %lf %lf %lf || %lf\n",time1,time2,time4,time3,ans);
       if(t2<t3)
            ans+=t1;
       else
        {
            ans+=t3;
            break;
        }
        i+=f;
    }
    printf("Case #%d: %.7lf\n",k,ans);
    }
     return 0;

}
