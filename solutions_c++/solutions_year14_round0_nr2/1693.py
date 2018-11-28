#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include<iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
double C,c,F,X;
int n;
double ans;
double TC[110110];
double check(int i)
{
    return TC[i]+X/(c+(double)(i)*F);
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=0;
    while(T--)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        c=2.0;
        int n=(int)(X+1.0);
        ans=X/c;
        TC[0]=0.0;
        //printf("%.6f\n",ans);
        for(int i=0;i<=n+10;i++)
        {
            if(i) TC[i]=TC[i-1]+C/(c+(double)(i-1)*F);
            ans=min(ans,check(i));
        }
        printf("Case #%d: %.7f\n",++cas,ans);
    }

    return 0;
}
