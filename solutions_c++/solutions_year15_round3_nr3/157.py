#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<queue>
#include <iomanip>
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


int main()
{
    int t,w=1;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        ll i,j,k,l=0,r,c,n,m,o,v,arr[1111],ans=0;
        cin>>n>>m>>v;
        for(i=0;i<m;i++)
            cin>>arr[i];
        ll res=1;
        for(i=0;i<m;i++)
        {
            if(arr[i]<=res)
            {
                res+=arr[i]*n;
            }
            else
            {
                ans++;
                res+=res*n;
                i--;
            }
        }
        while(1)
        {
            if(res>v)
                break;
            ll temp=res;
            res=temp*n+res;
            ans++;
        }
        cout<<"Case #"<<w<<": "<<ans<<"\n";
        w++;
    }
    return 0;
}
