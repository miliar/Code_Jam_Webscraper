#include<bits/stdc++.h>

#define ll long long

using namespace std;

int hs[10];

bool ch(ll n)
{
    ll i,num=n;
    while(num)
    {
        ll rem=num%10;
        hs[rem]=1;
        num/=10;
    }
    for(i=0;i<=9;i++)
        if(hs[i]==0)
        return 1;
    return 0;
}

int main()
{
    ll t;
    cin>>t;
    ll n,i,j;
    for(i=1;i<=t;i++)
    {
        memset(hs,0,sizeof(hs));
        cin>>n;
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",i);
        }
        else
        {
            ll ct=1;
            while(ch(n*ct))
            {
                ct++;
            }
            printf("Case #%lld: %lld\n",i,n*(ct));
        }
    }
    return 0;
}
