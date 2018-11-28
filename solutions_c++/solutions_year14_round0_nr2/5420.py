#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

double c,f,x;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B2.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int ca=1;ca<=cas;ca++)
    {
        printf("Case #%d: ",ca);
        scanf("%lf%lf%lf",&c,&f,&x);
        double tmp=0,v=2.0,t=0;
        while (1)
        {
            if (x/v>c/v+x/(v+f))
            {
                t+=c/v;
                tmp+=c;
                v+=f;
            }
            else
            {
                t+=x/v;
                break;
            }
        }
        printf("%.8f\n",t);
    }
    return 0;
}

