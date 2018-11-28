#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out","w",stdout);
    int csnum;
    cin>>csnum;
    for(int cs=1;cs<=csnum;cs++)
    {
        double c,f,x,ans;
        cin>>c>>f>>x;
        double v=2.0;
        ans=x/v;
        double t=0;
        while (t<ans)
        {
            t+=c/v; v+=f;
            ans=min(ans,t+x/v);
        }
        printf("Case #%d: ",cs);
        printf("%.7lf\n",ans);
    }
    return 0;
}
