#include <iostream>
using namespace std;
#include <stdio.h>
#include <string.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    double C,F,X;
    for(int cnt = 1;cnt<=T;cnt++)
    {
        cin>>C>>F>>X;
        double ans=0x7ffffff,now=X/2,cookie=2;
        while(ans>now)
        {
            ans = now;
            double bak = now;
            bak -= X/cookie;
            bak += X/(cookie+F) +C/(cookie);
            cookie += F;
            now = bak;
        }
        printf("Case #%d: ",cnt);
        printf("%.7lf\n",ans);
    }
}
