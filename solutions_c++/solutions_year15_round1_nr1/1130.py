#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#define ll long long int
#define mk make_pair
#define pb push_back
using namespace std;


int main()
{
    int t,w=1;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        ll i,j,k,l,ans=0,n,arr[100100],ans1=0,ma=0;
        cin>>n;
        for(i=1;i<=n;i++)
            cin>>arr[i];
        for(i=2;i<=n;i++)
        {
            if(arr[i]<arr[i-1])
                ans+=arr[i-1]-arr[i];
        }
        for(i=2;i<=n;i++)
            ma=max(ma,arr[i-1]-arr[i]);
        for(i=1;i<n;i++)
            ans1+=min(ma,arr[i]);
        cout<<"Case #"<<w<<": "<<ans<<" "<<ans1<<"\n";
        w++;
    }
    return 0;
}
