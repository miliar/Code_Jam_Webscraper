#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
#include<sstream>
using namespace std;
typedef long long ll;
int main()
{
    vector<ll>x;
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    int c=1;
    for(ll i=1;i<=10000000;i++)
    {
stringstream ss;
        ss<<i;
        string a;
        ss>>a;
        ss.clear();
        ss<<string(a.rbegin(),a.rend());
        ll aux;
        ss>>aux;
        if(i!=aux) continue;
        ss.clear();
        ss<<i*i;
        string s;
        ss>>s;
        ss.clear();
        ss<<string(s.rbegin(),s.rend());

        ss>>aux;
        if(i*i==aux) x.push_back(aux);
    }
    int n;
    ll a,b;
    scanf("%d",&n);
    while(n-- && scanf("%lld %lld",&a,&b))
    {

        printf("Case #%d: %d\n",c++,upper_bound(x.begin(),x.end(),b)-lower_bound(x.begin(),x.end(),a));
    }
    return 0;
}
