#include<bits/stdc++.h>
using namespace std;

#define l long long
#define pb(x) push_back(x)

int main()
{
    int t;
    cin>>t;
    for(int ix=1;ix<=t;ix++)
    {
         int n;
         cin>>n;int m[n+2];
         int ans1=0;
         for(int i=0;i<n;i++)cin>>m[i];
         for(int i=0;i<n-1;i++)
         {
             if(m[i]>m[i+1])
             {
                 ans1+=(m[i]-m[i+1]);
             }
         }
         cout<<"Case #"<<ix<<": ";
         int temp=0,ans2=0;
         for(int i=0;i<n-1;i++)
         {
             if(m[i]>m[i+1])
             {
                 temp=max(temp,m[i]-m[i+1]);
             }
         }
         for(int i=0;i<n-1;i++)
         {
             ans2+=min(m[i],temp);
         }
         cout<<ans1<<" "<<ans2<<endl;
    }
}
