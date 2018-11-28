#include "bits/stdc++.h"
#define MAXRATE 111111
using namespace std;
int test(int id)
{
    double C,F,X;
    cin>>C>>F>>X;
    cout<<"Case #"<<id<<": ";
    double basetime=0.0,rate=2.0,cur,future;
    double ans=99999999.0;
    bool flag = true;

    cur = X/rate;
    future = C/rate + X/(rate+F);
    while (cur>future){
            basetime+=(C/rate);
            rate+=F;
            cur = X/rate;
            future = C/rate + X/(rate+F);
            double temp = basetime + cur;
            if (temp<ans){ans = temp;}
        }
    //cout<<ans<<"\n\n\n\n";
    ans = basetime + (X/rate);
    printf("%.9lf\n",ans);
    return 0;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outBl.txt","w",stdout);
    int T; scanf("%d",&T);
    for (int i=1; i<=T; i++)
    {
        test(i);
    }
}
