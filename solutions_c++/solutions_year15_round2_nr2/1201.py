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
        ll i,j,k,l,ans=0,b,p=0,n,m,x,mi=10e9;
        memset(visited,0,sizeof(visited));
        memset(dist,0,sizeof(dist));
        cin>>n>>m>>x;
        k=n*m;
        l=pow(2,k);
        for(i=0;i<l;i++)
        {
            ll co=0;
            ll arr[100][100]={0};
            for(j=0;j<k;j++)
            {
                if((i&(1<<j)))
                {
                    co++;
                    arr[j/m][j%m]=1;
                }
                else
                    arr[j/m][j%m]=(i&(1<<j));
            }
            if(co==x)
            {
                ll val=0;
                /*for(p=0;p<n;p++)
                {
                    for(j=0;j<m;j++)
                        cout<<arr[p][j]<<" ";
                    cout<<"\n";
                }*/
                for(p=0;p<n;p++)
                {
                    for(j=0;j<m;j++)
                    {
                        if(p>=1&&arr[p][j]*arr[p-1][j]==1)
                            val++;
                        if(p<n-1&&arr[p][j]*arr[p+1][j]==1)
                            val++;
                        if(j>=1&&arr[p][j]*arr[p][j-1]==1)
                            val++;
                        if(j<m-1&&arr[p][j]*arr[p][j+1]==1)
                            val++;
                    }
                }
                mi=min(mi,val/2);
            }
        }
        cout<<"Case #"<<w<<": "<<" "<<mi<<"\n";
        w++;
        n++;
    }
    return 0;
}
