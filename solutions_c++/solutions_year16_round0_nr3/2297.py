#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll n,j;
ll getd(ll v)
{
    for(int i=2;i<sqrt(v)+5;i++)
    {
        if(v%i==0)
            return i;
    }
    return 0;
}
inline int tbase(ll v,int b)
{
    ll val=0;
    while(v>0)
    {
        val*=b;
        val+=v&1;
        v/=2;
    }
    return getd(val);
}
string to_bin(ll w)
{
    string s;
    while(w>0)
    {
        s+=(w&1)+48;
        w/=2;
    }
    return s;
}
int main()
{
    cin >> n >> n >> j;
    cout << "Case #1:\n";
    int f=0;
    for(ll v=1<<(n-1);v<(1<<n);v++)
    {
        if(v%2==0)
            continue;
        vector<ll> w;
        bool flag=1;
        for(int i=2;i<=10;i++)
        {
            ll k=tbase(v,i);
            if(k==0)
            {
                flag=0;
                break;
            }
            w.push_back(k);
        }
        if(flag)
        {
            cout << to_bin(v);
            for(auto &i:w)
                cout << " " << i;
            cout << "\n";
            f++;
            if(f==j)break;
        }
    }
    return 0;
}
