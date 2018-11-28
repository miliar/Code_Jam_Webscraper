#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;
int main()
{
    int T;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double cur=c;
        double ans=0;
        double v=2.0;
        cout<<"Case #"<<tt<<": ";
        if(cur>=x)
        {
            ans=x/2.0;
            printf("%.7lf\n",ans);
            continue;
        }

        while(cur<x)
        {
            ans+=c/v;
            cur=c;
            double t1=(x-cur)/v;
            double t2=x/(v+f);
            if(t1>t2)
            {
                v=v+f;
                cur=0;
            }
            else
            {
                ans+=t1;
                break;
            }
        }
        printf("%.7lf\n",ans);
    }
    return 0;
}
