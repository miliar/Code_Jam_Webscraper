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
    int t,w=1;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        ll i,j,k,l,ans=0,n,arr[10010],b,p=0;
        memset(visited,0,sizeof(visited));
        memset(dist,0,sizeof(dist));
        cin>>n;
        queue<ll> q;
        visited[1]=1;
        dist[1]=1;
        q.push(1);
        while(!q.empty())
        {
            ll u=q.front(); q.pop();
            if(u>n)
                continue;
            ll v=rev(u);
            if(visited[u+1]==0)
            {
                dist[u+1]=1+dist[u];
                visited[u+1]=1;
                q.push(u+1);
            }
            if(v!=u&&v>u+1&&visited[v]==0)
            {
                dist[v]=1+dist[u];
                visited[v]=1;
                q.push(v);
            }

        }
        cout<<"Case #"<<w<<": "<<dist[n]<<"\n";
        w++;
    }
    return 0;
}
