#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int main()
{
    int nc;
    scanf("%d",&nc);
    for(int ic=1;ic<=nc;ic++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double now=2.0,nt=0.0,ans=x/2.0;
        double tans;
        while(true)
        {
            nt+=c/now;
            now+=f;
            tans=x/now+nt;
            if (tans>ans)
                break;
            else
                ans=tans;
        }
        printf("Case #%d: %.7f\n",ic,ans);
    }
    return 0;
}
