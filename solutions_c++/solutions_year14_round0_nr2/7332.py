#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int c=1,t;
    double C,F,X;
    cin>>t;
    while(t--)
    {
        cin>>C>>F>>X;
        double totalTime=0.0,cookiesPerSecond=2;
        while((C/cookiesPerSecond) + (X/(F+cookiesPerSecond)) < (X/cookiesPerSecond))
        {
            totalTime+= C/cookiesPerSecond;
            cookiesPerSecond+=F;
        }
        totalTime+=X/cookiesPerSecond;
        printf("Case #%d: %lf\n",c++,totalTime);
    }
    return 0;
}
