#include<iostream>
#include<vector>
#include<cstdio>
#include<queue>
#include<cstring>
using namespace std;
void solve()
{
    string s;
    cin>>s;
    int o=0,co=0,i,n=s.size();
    if(s[0]=='-')o=1;
    for(i=1;i<n;++i)
    {
        if(s[i]!=s[i-1])++co;
        if(s[i]=='-')o=max(o,co+1);
    }
    cout<<o<<'\n';
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int i,n;
    cin>>n;
    for(i=1;i<=n;++i)
    {
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
