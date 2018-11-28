#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
double c,f,x;
int main()
{
    freopen("B1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas)
    {
        printf("Case #%d: ",cas);
        scanf("%lf%lf%lf",&c,&f,&x);
        double r=2;
        if(x<c){printf("%.7f\n",x/r);continue;}
        double ans=0;
        while(x/r>c/r+x/(r+f))
        {
            ans+=c/r;
            r+=f;
           // cout<<ans<<' '<<r<<endl;
        }
        ans+=x/r;
        printf("%.7f\n",ans);

    }



    return 0;
}
