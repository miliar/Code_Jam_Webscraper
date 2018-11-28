#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int t,co=0;
    double t1,t2,to,ans,c,f,x,cs;
    cin>>t;
    while(t--)
    {
        co++;
        cs=2;
        cin>>c>>f>>x;
        c=c*1.0000000;
        f*=1.0000000;
        x*=1.0000000;
        ans=0.0;
        if(x<c)
        {
            to=x/(2*1.0000000);
            printf("Case #%d: %.7lf\n",co,to);
            continue;
        }
        t2=0.0000000;
        while(1)
        {
            t1=x/cs;
            t2+=c/cs;
            t2+=x/(f+cs);
            if(t2<=t1)
            {
                ans+=c/cs;
                cs+=f;
                t2=0.0000000;
            }
            else
            {
                ans+=x/cs;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",co,ans);
    }
    return 0;
}
