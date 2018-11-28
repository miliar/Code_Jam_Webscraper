#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
ll t;
set<ll> bol;
void fcia(int C)
{
    while(C>0LL)
    {
        bol.erase(C%10LL);
        C/=10LL;
    }
}
int main()
{
    scanf("%lld",&t);
    for(int xyz=1;xyz<=t;xyz++)
    {
        for(int i=0;i<10;i++)bol.insert(i);
        int n;scanf("%d",&n);
        if(n==0LL){printf("Case #%d: INSOMNIA\n",xyz);continue;}
        ll nn=n;
        while(true)
        {
            fcia(n);
            if(bol.empty())break;
            n+=nn;
        }
        printf("Case #%lld: %lld\n",xyz,n);
    }
    return 0;
}
