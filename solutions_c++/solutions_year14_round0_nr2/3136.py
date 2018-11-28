#include<cstdio>
using namespace std;
int main()
{
    long long t,i,j;
    double c,f,x,r,count;
    scanf("%lld",&t);
    for(i=0;i<t;i++)
    {
         scanf("%lf%lf%lf",&c,&f,&x);
         r=2.0;         
         count=0.0;         
         while(count + (x/r) > count + (x/(r+f)) + (c/r))
         {
             count+= (c/r);
             r=r+f;
         }
         count+= (x/r);           
         printf("Case #%lld: %.7lf\n",i+1,count);
     }                            
      return 0;
}      
                       
                                   
                    
