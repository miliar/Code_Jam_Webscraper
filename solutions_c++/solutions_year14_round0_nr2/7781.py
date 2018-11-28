#include <iostream>
#include <cstdio>
using namespace std;
#define eps 1e-6
int main()
{
 //   freopen("B-large.in","r",stdin);
   // freopen("out.txt","w",stdout);
    double c,f,x,a,b;
    double ans;
    int T,cas=1;
    cin>>T;
    double now;
    while(T--)
    {
        ans=0;
        cin>>c>>f>>x;
        now=2.0;
        while(true)
        {
            a=x/now;
            b=c/now+x/(now+f);
            if(a<b)
            {
                ans=ans+a;
                break;
            }
            else
            {
                ans=ans+c/now;
                now=now+f;
            }
        }
            printf("Case #%d: %lf\n",cas,ans);

        cas++;
    }
    return 0;
}
