#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,t;
    double c,f,x,speed;
    double ans;
    scanf("%d",&cases);
    for(t=1;t<=cases;++t)
    {
        printf("Case #%d: ",t);
        scanf("%lf%lf%lf",&c,&f,&x);
        speed=2.0;
        ans=0.0;
        if(x<=c)
        {
            printf("%.7f\n",x/speed);
            continue;
        }
        while(x*speed<=(x-c)*(speed+f))
        {
            ans+=c/speed;
            speed+=f;
        }
        printf("%.7f\n",ans+x/speed);
    }
    return 0;
}
