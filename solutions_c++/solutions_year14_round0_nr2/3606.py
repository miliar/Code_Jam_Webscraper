#include<iostream>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int d=1;d<=t;d++)
    {
            double c,f,x,s=0;
            scanf("%lf%lf%lf",&c,&f,&x);
            double r=2+f;
            double x1=x/2;
            double y1=x/(2+f);
            double a=c/2;
            
            while(a<(x1-y1))
            {
                       s+=a;  
                       a=c/r;
                       r=r+f;
                       x1=y1;
                       y1=x/(r);
            }
            s=s+x1;
            printf("Case #%d: %.7lf\n",d,s);
    }
    return 0;
}
                        
