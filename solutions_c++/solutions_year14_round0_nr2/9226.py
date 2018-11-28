#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdio>
#include<vector>
#include<set>
#include<map>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        double C,F,X,d=2.0,k,p=0.0,ans;

        scanf("%lf%lf%lf",&C,&F,&X);

        ans=X/d;
        while(true)
        {
            k=p+C/d; if(k>ans) break;
            p=k; k+=(X-C)/d;
            d+=F; ans=min(ans,k);
        }
        printf("Case #%d: %.7lf\n",t,ans);
    }
    return 0;
}
