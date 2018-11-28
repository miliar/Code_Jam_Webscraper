#include <bits/stdc++.h>
using namespace std;
int main()
{
        int T;
        cin>>T;
        int t;
        for(t=1;t<=T;t++)
        {
                double C,F,X;
                cin>>C>>F>>X;
                double ans=0.0;
                double rate=2.0;
                double curr=0.0;
                while( (X/rate) > (C/rate)+((X-curr)/(rate+F)))
                {
                        double t=C/rate;
                        ans+=t;
                        curr=(rate*(t))-C;
                        rate+=F;
                }
                printf("Case #%d: %0.7lf\n",t,ans+((X-curr)/rate));
        }
        
        return 0;
}

