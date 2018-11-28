#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,tt=0;
    double c,f,x,rate,time1,time2,beforetime;
    scanf("%d",&t);
    while(t--)
    {
        tt++;
        scanf("%lf%lf%lf",&c,&f,&x);
        rate=2.0;
        beforetime=0;
        time1=beforetime+x/rate;
        beforetime+=c/rate;
        rate+=f;
        time2=beforetime+x/rate;
        while(time1>time2)
        {
            time1=time2;
            beforetime+=c/rate;
            rate+=f;
            time2=beforetime+x/rate;
        }
        printf("Case #%d: %.10lf\n",tt,time1);
    }
    return 0;
}
