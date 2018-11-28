#include<iostream>
#include<stdio.h>
#define read_ freopen("in.in","r",stdin)
#define write_ freopen("out.txt","w",stdout)
using namespace std;
int main()
{
    read_;
    write_;
    int T;
    double C,F,X;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        double ret = 2;
        double ans = 0;
        double dis = X;
        int f = 0;
        while(X>0)
        {
            double dir = X/ret;
            double vaia = C/ret+X/(ret+F);
            if(vaia<dir)
            {
                ans+=C/ret;
                X = dis;
                ret+=F;
                f++;
            }
            else
            {
                ans+=dir;
                break;
            }
        }
        printf("Case #%d: %.9lf\n",t,ans);
    }
    return 0;
}
