#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
//    freopen("in.in","r",stdin);
//    freopen("ans.in","w",stdout);
    int T,Case=1;
    double c,f,x;
    cin>>T;
    while(T--)
    {
        cin>>c>>f>>x;
        double ans;
        double p=2.0;
        printf("Case #%d: ",Case++);
        if(x<c)
        {
            ans=x/p;
            printf("%lf\n",ans);
            continue;
        }
        double t=c/p;
        ans=x/p;
        double tmp=t+x/(p+f);
        for(double i=2.0;i<=500000;i+=1.0)
        {
            if(tmp<ans)
                ans=tmp;
            t+=c/(p+f*(i-1.0));
            tmp=t+x/(p+f*i);

        }
        printf("%lf\n",ans);
    }
    return 0;
}
