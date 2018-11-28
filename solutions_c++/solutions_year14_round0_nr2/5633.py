#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
#define LL long long
double p[100001];
int main()
{
    int t,cas = 1,i,n;
    double c,f,x,temp,ans;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        n = (int)x;
        p[1] = c/2.0;
        temp = f + 2.0;
        for(i = 2;i <= n;i ++)
        {
            p[i] = p[i-1] + c/temp;
            temp += f;
        }
        ans = x/2.0;
        temp = f + 2.0;
        for(i = 1;i <= n;i ++)
        {
            ans = min(ans,p[i]+x/temp);
            temp += f;
        }
        printf("Case #%d: %7lf\n",cas++,ans);
    }
    return 0;
}
