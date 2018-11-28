#include <iostream>
#include <cstdio>
#define eps 1e-9
using namespace std;
int main()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int ii=0;ii<t;ii++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=0;
        double res=2.0;
        while(1)
        {
            //cout<<x/(res+f)<<" "<<(x-c)/res<<endl;
            if(c-x>eps||x/(res+f)-(x-c)/res>eps)
            break;
            ans+=c/res;
            //cout<<ans<<endl;
            res+=f;
        }
        ans+=x/res;
        printf("Case #%d: ",ii+1);
        printf("%.7lf\n",ans);
    }
}
