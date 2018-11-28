#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,tt,i,d;
    long double c,x,f,k,ans;
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
        ans =0.0 ;
        scanf("%Lf%Lf%Lf",&c,&f,&x);
        k = x/c - 1 - 2/f;
        k = k+0.000001;
        d = floor(k);
        if(x >= c+0.000001)
        {
            for(i=0;i<=d;i++)
                ans += c/(2.0+i*f);
            ans = ans + x/(2.0 + (d+1)*f);
        }
        else
        {
            ans = x/(2.0);
        }
        if(ans >= x/(2.0))
            ans = x/(2.0);
        printf("Case #%d: %Lf\n",tt,ans);


    }
    return 0;
}
