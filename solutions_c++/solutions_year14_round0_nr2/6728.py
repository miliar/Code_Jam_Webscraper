#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    double c,f,x;
    double temp=0;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        temp=0;
        double ans=1000000000;
        double s=2;
        double t=0;
        while(1)
        {
            temp=x/s;
            if((t+temp)<ans)
            {
                ans=t+temp;
                t=t+c/s;
                s=s+f;
            }
            else
                break;
        }
        printf("Case #%d: %.7lf\n",k,ans);
    }
    return 0;
}
