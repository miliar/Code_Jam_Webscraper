#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        ll n;
        scanf("%lld",&n);
        set<int> s;
        ll m=1;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",i);
        else{
        while(1)
        {
            ll x=n*m;
            ll a=n*m;
            while(x>0)
            {
                s.insert(x%10);
                x/=10;
            }
            m++;
            if(s.size()==10)
               {
                   printf("Case #%d: %lld\n",i,a);
                   break;
               }
        }
        }
    }
    return 0;
}

