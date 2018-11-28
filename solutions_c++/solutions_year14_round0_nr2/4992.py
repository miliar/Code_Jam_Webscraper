#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <queue>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#define eps 1.0e-9
using namespace std;
int sgn(double f)
{
    if(fabs(f)<eps) return 0;
    else return f<0?-1:1;
}
int main()
{
    freopen("out.txt","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        double v=2.0,c,f,x,ans,tp=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x/v;
        for(int i=1;1;i++)
        {
            tp+=c/((i-1)*f+v);
            if(sgn(tp-ans)>0) break;
            double a=tp+x/(i*f+v);
            if(sgn(a-ans)<0) ans=a;
        }
        printf("Case #%d: %.7f\n",cas++,ans);
    }
    return 0;
}

