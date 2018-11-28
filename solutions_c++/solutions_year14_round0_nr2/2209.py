/**
 * @author neko01
 */
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <math.h>
using namespace std;
typedef long long LL;
#define INF 0x7fffffff
const double eqs=1e-8;
int main()
{
    int t,cnt=0;
    //freopen("B-large.in" , "r" , stdin);
    //freopen("B-large.out" , "w" , stdout);
    scanf("%d",&t);
    while(t--)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        printf("Case #%d: ",++cnt);
        if(x<=c)
        {
            printf("%.6lf\n",x/2);
            continue;
        }
        double ans=x/2;
        double sum=0;
        for(int i=0;;i++)
        {
            sum+=(c/(i*f+2));
            double temp=x/(i*f+f+2);
            if(sum+temp<ans)
                ans=sum+temp;
            else
                break;

            //printf("%.6lf\n",c/(i*f+2));
        }
        //ans+=(x/(k*f+f+2));
        printf("%.6lf\n",ans);
    }
    return 0;
}
