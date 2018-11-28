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
        ll i,j,k,l,ans=0,n,arr[10010],b,p=0;
        cin>>b>>n;
        for(i=1;i<=b;i++)
            cin>>arr[i];
        ll lo=0;
        ll hi=10e15;
        while(lo<=hi)
        {
            ll mid=(lo+hi)/2;
            ll sum=0;
            for(i=1;i<=b;i++)
                sum+=mid/arr[i];
            if(sum+b>=n)
            {
                ans=mid;
                hi=mid-1;
            }
            else
                lo=mid+1;
        }
        vector<pair<ll,ll> > vec;
        for(i=b;i>=1;i--)
        {
            k=ans/arr[i];
            p+=k;
            k=k*arr[i];
            vec.pb(mk(k,i));
        }
        sort(vec.begin(),vec.end(),comp());
        ans=vec[n-p-1].first;
        cout<<"Case #"<<w<<": "<<ans<<"\n";
        w++;
    }
    return 0;
}
