#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main()
{
    freopen("inputB.txt","r",stdin);
    freopen("outputB.txt","w",stdout);
    int t=0;
    scanf("%d",&t);
    double a,b,c;
    for(int po=0;po<t;po++)
    {
        double ans=0.0;
        double rate=2.0;
        cin>>a>>b>>c;
        if(c<a) ans=c/rate;
        else
        {
            while(1)
            {
                ans += a / rate;
                if((c - a) / rate <= (c / (rate + b)))
                {
                    ans += (c-a) / rate;
                    break;
                }
                else rate += b;
            }
        }
        printf("Case #%d: %.7lf\n",po+1,ans);
    }
}
                    
            
            
