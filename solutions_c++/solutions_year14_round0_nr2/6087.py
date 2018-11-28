#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        double C,F,X,step=2,tm=0;
        scanf("%lf%lf%lf",&C,&F,&X);
        while(C/step+X/(step+F)<X/step)
        {
            tm+=C/step;
            step+=F;
        }
        tm+=X/step;
        printf("Case #%d: %.7lf\n",cas,tm);
    }
    return 0;
}
