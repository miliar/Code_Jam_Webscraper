#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define inf 10000000000000
int main()
{   
    ll t,n,i,y;
    scanf("%lld",&t);
    y=t;
    while(t--)
    {
        scanf("%lld",&n);
        ll mark[15];
        for(i=0;i<12;i++)
        mark[i]=0;
        ll count=0;
        ll w=0;
        while(1)
        {
            w++;
            ll m=n*w,d;
            //printf("%lld %lld\n",n,w);
            while(m!=0)
            {
                d=m%10;
                mark[d]=1;
                m=m/10;
            }

            for(i=0;i<=9;i++)
            {
                if(mark[i]==0)
                break;
            }
            if(i==10)
            break;
            count++;
            if(count==10000)
            break;
        }
        if(count==10000)
        printf("Case #%lld: INSOMNIA\n",y-t);
        else
        {
            printf("Case #%lld: %lld\n",y-t,n*w);
        }
    }
    return 0;
}