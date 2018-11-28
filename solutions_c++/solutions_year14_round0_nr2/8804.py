#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
 //   freopen("B-large.in","r",stdin);
 //   freopen("b.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int dex=1;dex<=T;dex++)
    {
        double c,f,x;  // 农场价格，增量，目标钱数
        double ans=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        int p=0; // 当前农场数
        // x/(2+f*p)>c/(2+f*p)+x/(2+f*(p+1))
        while (x/(2+f*p)>c/(2+f*p)+x/(2+f*(p+1)))
        {
            ans+=c/(2+f*p);
            p++;
        }
        ans+=x/(2+f*p);
        printf("Case #%d: %.7lf\n",dex,ans);
    }
 //   system("pause");
    return 0;
}
