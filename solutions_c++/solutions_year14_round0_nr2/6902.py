#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#define db double
using namespace std;

int main()
{
#ifdef PKWV
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif // PKWV
    int T;
    scanf("%d",&T);
    int cas=1;
    while(T--)
    {
        db c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        db tolcost=0.0;
        db curf=2.0;
        while(c/curf+x/(curf+f)<x/curf)
        {
            tolcost+=c/curf;
            curf+=f;
        }
        tolcost+=x/curf;
        printf("Case #%d: %.7f\n",cas++,tolcost);
    }
    return 0;
}
