#include <iostream>
#include <fstream>

using namespace std;
int n;
 double C,F,X;
 double rate=2.0;
 double time;
 double time2;
void citire()
{
    scanf("%lf %lf %lf ",&C,&F,&X);
}
void rez()
{   rate=2.0;
    time=X/rate;
    if(time<C/rate+X/(rate+F))
        return;
    time2=0;
    while(time2<=time)
    {   time2+=C/rate;
        rate+=F;
        time2+=X/rate;
        if(time2<time)
            time=time2;
        time2-=X/rate;
    }
}
int main()
{
    freopen("jam.in","r",stdin);
    freopen("jam.out","w",stdout);
    scanf("%d",&n);
    for(int run=1;run<=n;run++)
    {   citire();
        rez();
        printf("Case #%d: ",run);
        printf("%.7llf\n",time);
    }
    return 0;
}
