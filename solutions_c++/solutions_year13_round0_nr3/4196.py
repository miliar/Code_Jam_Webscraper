#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef long double ld;
const int N=1e7;
vector <ll> v;
inline bool pal(ll x)
{
    static int f[18];
    int p=0;
    while (x)
    {
        f[p++]=x%10;
        x/=10;
    }
    for(int i=0;i<=p/2;i++)
        if (f[i]!=f[p-i-1])
            return false;
    return true;
}
inline int f(ll n)
{
    int i=0;
    for(i=0;i<v.size() && v[i]<=n;i++);
    return i;
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("output.txt","w",stdout);
    v.reserve(40);
    for(int i=1;i<=N;i++)
        if (pal(i) && pal(i*1ll*i))
            v.push_back(i*1ll*i);
    int t;
    ll a,b;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        cin>>a>>b;
        cout<<"Case #"<<q<<": "<<f(b)-f(a-1)<<"\n";
    }
    return 0;
}
