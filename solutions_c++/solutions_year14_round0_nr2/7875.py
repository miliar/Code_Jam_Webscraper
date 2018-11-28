#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("of.out","w",stdout);
    int T,t;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double ans = 0.0;
        double per = 2.0;
        if(x<=c)
        {
            printf("Case #%d: %.7lf\n",t,x/2.0);
        }
        else
        {
            while( x/per > c/per + x/(per + f))
            {
                ans += c/per;
                per += f;
            }
            ans += x/per;
            printf("Case #%d: %.7lf\n",t,ans);
        }
    }
    return 0;
}
