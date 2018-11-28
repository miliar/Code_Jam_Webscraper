#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stack>
#include <string>
#include <math.h>
using namespace std;
double c,f,x;
const double eps = 1e-8;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int i,j,k,m,n;
    int ca;
    scanf("%d",&ca);
    int t=1;
    while(scanf("%lf%lf%lf",&c,&f,&x)!=EOF)
    {
        double ans = x/2;
        for(i=1;;i++)
        {
            double tmp=0;
            for(j=0;j<i;j++)
                tmp+=(c/(j*f+2));
            tmp+=(x/(i*f+2));
            if(ans-tmp>eps)
                ans=tmp;
            else
                break;

        }
        printf("Case #%d: %.7lf\n",t++,ans);
    }







    return 0;
}
