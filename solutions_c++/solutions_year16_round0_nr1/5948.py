#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

map<ll,ll>mp;
ll n,x;

bool mod()
{
    x+=n;
    ll y=x;

    while(y)    {
        mp[y%10]=1;
        y/=10;
    }
    ll i;
    for(i=0;i<10;i++)    {
        if(!mp[i])    break;
    }
    return i==10;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    ll t;
    cin>>t;
    ll i=1;

    while(i<=t)    {
        cin>>n;
        cout<<"Case #"<<i<<": ";
        if(!n)    {
            cout<<"INSOMNIA"<<endl;
            i++;
            continue;
        }

        x=0;
        while(!mod()){}
        cout<<x<<endl;
        mp.clear();
        i++;
    }



    return 0;






}
