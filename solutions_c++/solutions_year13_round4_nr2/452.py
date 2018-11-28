#include<iostream>
#include<sstream>
#include<cstdio>
#include<cctype>
#include<string>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<vector>
#include<cstring>
#include<algorithm>

#define ll long long
#define inf 1000000009
#define mod 1000000007

using namespace std;

typedef pair<int,int> II;

ll Max(int n,ll x)
{
    if(x==0) return 1;
    if(n==1) return 2;
    return (1ll<<(n-1))+Max(n-1,(x-1)/2);
}
ll Min(int n,ll x)
{
    ll tot=(1ll<<n);
    return tot-Max(n,tot-x-1)+1;
}
void go(int cas)
{
    int n;
    ll p;
    cin>>n;
    cin>>p;
    ll s=0,e=(1ll<<n)-1,y=0,z=0;
    while(s<=e)
    {
        ll mid=(s+e)/2;
        if(Max(n,mid)<=p) y=mid,s=mid+1;
        else e=mid-1;
    }
    s=0;
    e=(1ll<<n)-1;
    while(s<=e)
    {
        ll mid=(s+e)/2;
        if(Min(n,mid)<=p) z=mid,s=mid+1;
        else e=mid-1;
    }
    cout<<"Case #"<<cas<<": "<<y<<" "<<z<<endl;
}

int main()
{
    //freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int T;
    cin>>T;
    for(int run=1;run<=T;run++) go(run);
    //fclose(stdout);
}
