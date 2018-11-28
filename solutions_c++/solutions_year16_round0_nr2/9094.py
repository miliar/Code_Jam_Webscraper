#include <bits/stdc++.h>
#define ll long long
using namespace std;
string s;
ll solve(ll a)
{
    ll i, l;
    l=s.length();
    for(i=1;i<l;i++)
    {
        if(s[i]!=s[i-1])
            a++;
    }
    return a;
}
int main()
{
    ll t, k, a, l;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        a=0;
        cin>>s;
        cout<<"Case #"<<k<<": ";
        l=s.length();
        if(s[l-1]=='-')
            a++;
        a=solve(a);
        cout<<a<<endl;
    }
    return 0;
}