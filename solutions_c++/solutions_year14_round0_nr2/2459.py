#include<stdio.h>
#include<iostream>
using namespace std;
double c,f,x;
int main()
{
    freopen("Bout.txt","w",stdout);
    int t;
    double i;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double ix=c/2.0;
        double ans=x/2.0;
        for(i=1;i*c<=x;i++)
        {
            if(ix+x/(i*f+2.0)<ans)
            {
                ans=ix+x/(i*f+2.0);
            }
            ix=ix+c/(i*f+2.0);
        }
        printf("Case #%d: %.7lf\n",cas++,ans);
    }
    return 0;
}
