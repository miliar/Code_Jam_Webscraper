#include<iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int t;
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>t;
    for (int tt=1;tt<=t;tt++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double ans=0;
        double cur_r=2;
        double t1=x/cur_r, t2=c/cur_r+x/(cur_r+f);
        while (t1>t2)
        {
            ans+=c/cur_r;
            cur_r+=f;
            t1=x/cur_r;
            t2=c/cur_r+x/(cur_r+f);
        }
        ans+=t1;
        cout<<"Case #"<<tt<<": ";
        printf("%.7lf\n",ans);
    }
    return 0;
}
