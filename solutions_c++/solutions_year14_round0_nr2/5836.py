#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;

double C,F,X;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int test=0;
    while(T--)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        double ans=0;
        double sp=2;
        while(true)
        {
            double t1=X/sp;
            double t2=C/sp+X/(sp+F);
            if(t1<t2)
            {
                ans+=X/sp;
                break;
            }
            else
            {
                ans+=C/sp;
                sp+=F;
            }
        }
        printf("Case #%d: %.7lf\n",++test,ans);
    }
    return 0;
}
