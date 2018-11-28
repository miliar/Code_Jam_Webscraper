#include <iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.in","w",stdout);
    int test,tt;
    double c,f,x,r,tim,t1,t2;
    scanf("%d",&test);
    for(tt=1;tt<=test;tt++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        r=2;tim=0;
        while(1)
        {
            t1=x/r;
            t2=c/r+(x/(r+f));
            if(t1>t2)
            {
                tim=tim+(c/r);
                r=r+f;
            }
            else
            {
                tim=tim+t1;
                break;
            }
        }
        printf("Case #%d: ",tt);
        printf("%0.9lf\n",tim);
    }
    return 0;
}
