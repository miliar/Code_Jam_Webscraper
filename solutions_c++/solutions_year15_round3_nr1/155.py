#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#define ll long long int
#define mk make_pair
#define pb push_back
#define mod 1000000007
using namespace std;

struct comp
{
    bool operator() (const pair<int ,int > &p1 , const pair<int , int > &p2) const
    {
        if(p1.first<p2.first)
            return true;
        if(p1.first==p2.first&&p1.second<p2.second)
            return true;
        return false;
    }
};

ll visited[1000100],dist[1000100];

ll rev(ll n)
{
    ll r=0,d=0;
    while(n!=0)
    {
        r=n%10;
        d=d*10+r;
        n/=10;
    }
    return d;
}

int main()
{
    int t,w=1,n;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        ll i,j,k,l,ans=0,r,c;
        cin>>r>>c>>k;
        for(i=1;i<r;i++)
            ans+=(c/k);
        if(c%k==0)
            ans+=(c/k)-1+k;
        else
            ans+=c/k+k;
        cout<<"Case #"<<w<<": "<<ans<<"\n";
        w++;
        n++;
    }
    return 0;
}
