#include <iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
#define ll long long
int getPow(ll q)
{
    int re=0;
    ll t=1;
    while(t<q)
    {
        re++;
        t*=2;
    }
    if(t!=q)
        return -1;
    return re;
}
int main()
{
    ll i,j,t,m,n;
    freopen("E:\\in","r",stdin);
    freopen("out","w",stdout);
    cin>>t;
    for(int tt=1;tt<=t;++tt)
    {
        ll p,q;
        char c;
        cin>>p>>c>>q;
        int re=0;
        int mu=getPow(q);
        if(mu==-1||mu>40)
        {
            cout<<"Case #"<<tt<<": impossible\n";
            continue;
        }
        while(p*2<q)
           {
               re++;
               q/=2;
           }
        cout<<"Case #"<<tt<<": "<<re+1<<"\n";
    }
    return 0;
}
