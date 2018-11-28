#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>
#include<cmath>
#include<cstdlib>
#include<vector>
using namespace std;
int brr,brp,brs;
void get(int t,int n)
{
    if(n==0)
    {
        if(t==1)brr++;
        if(t==2)brp++;
        if(t==3)brs++;
        return;
    }
    if(t==1)
    {
        get(1,n-1);
        get(3,n-1);
    }
    if(t==2)
    {
        get(2,n-1);
        get(1,n-1);
    }
    if(t==3)
    {
        get(3,n-1);
        get(2,n-1);
    }
}
string ou(int t,int n)
{
    string ll,rr;
    if(n==0)
    {
        if(t==1)return "R";
        if(t==2)return "P";
        if(t==3)return "S";
    }
    if(t==1)
    {
        ll=ou(3,n-1);
        rr=ou(1,n-1);
    }
    if(t==2)
    {
        ll=ou(2,n-1);
        rr=ou(1,n-1);
    }
    if(t==3)
    {
        ll=ou(2,n-1);
        rr=ou(3,n-1);
    }
    if(ll<rr)ll+=rr;
    else ll=rr+ll;
    return ll;
}
void solve()
{
    int l=0,n,r,p,s;
    cin>>n>>r>>p>>s;
    brr=brp=brs=0;
    get(2,n);
    if(brr==r && brp==p && brs==s)
    {
        cout<<ou(2,n)<<'\n';
        return;
    }
    brr=brp=brs=0;
    get(1,n);
    if(brr==r && brp==p && brs==s)
    {
        cout<<ou(1,n)<<'\n';
        return;
    }
    brr=brp=brs=0;
    get(3,n);
    if(brr==r && brp==p && brs==s)
    {
        cout<<ou(3,n)<<'\n';
        return;
    }
    cout<<"IMPOSSIBLE\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,i;
    cin>>t;
    for(i=1;i<=t;++i)
    {
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
