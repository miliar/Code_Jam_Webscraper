#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    double c,f,x,t=2,sum=0,min,TC;
    cin>>TC;
    for(int i=1;i<=TC;i++)
    {
        cin>>c>>f>>x;
        sum=0,min=x/2,t=2;
        while (1)
        {
            if(sum>min)
            {
                printf("Case #%d: %.7lf\n",i,min);
                break;
            }
            else
            {
                sum+=(c/t)+x/(t+f);
                if(sum<min)
                {
                    min=sum;
                    sum-=(x/(t+f));
                    t+=f;
                }
            }
        }
    }
    return 0;
}
