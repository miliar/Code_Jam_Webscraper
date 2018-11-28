#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;
ll n; 
ll getb(ll x,ll y,ll z)
{
    int ip=0;
    ll re=1;
    ll cot=0;
    while(x)
    {
        if(x%2)
        {
            re=1;
            for(int i=0;i<ip;i++)
            {
                re*=(y%z);
                re%=z;
            }
            cot+=re;
            cot%=z;
        }
        x/=2;
        ip++;
    }
    return cot;
}
ll g(ll x,ll y)
{
    for(ll i=2;i<=10000;i++)
    {
        if(getb(x,y,i)==0)
        {
            return i;
        }
    }
    return 0;
}
void out(ll x)
{
    if(x==0)return;
    out(x/2);
    cout<<x%2;
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt", "w",stdout);
#endif
    int T;
    cin>>T;int j;
    for(int ca=1;ca<=T;ca++)
    {
        ll cot[10];
        cin>>n>>j;
        ll now=1;
        for(int i=1;i<n;i++)now*=2LL;
        now+=1;
        printf("Case #%d:\n",ca);
        while(true)
        {
            memset(cot,0,sizeof(cot));
            if(j==0)break;
            int i;
            for(i=2;i<=10;i++)
            {
                ll re=g(now,i);
                cot[i]=re;
                if(re==0)break;
            }
            now+=2;
            if(i<=10)continue;
            out(now-2);
            for(int i=2;i<=10;i++)
            {
                printf(" %lld",cot[i]);
            }
            printf("\n");
            j--;
        }
    }
    return 0;
}
