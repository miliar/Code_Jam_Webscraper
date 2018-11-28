#include <stdio.h>
#include<algorithm>
#define min(a,b) a>b?b:a
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    double c,f,x;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double time1=1500,sum=0,p=2.0;
        while(1)
        {
            double t1=x/p;
            double t2=c/p+x/(p+f);
            if(t1>t2)
            {
                sum+=c/p;p=f+p;
            }
            if(t1<=t2) {printf("%.7lf\n",sum+t1);break;}
        }
    }
}
