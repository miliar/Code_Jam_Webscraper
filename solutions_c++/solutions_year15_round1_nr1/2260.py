#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a)    for(int i = 0;i < a;i++)
#define REP(i,a,b)  for(int i = a;i < b;i++)

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    REP(a,1,t+1)
    {
        int ar[1010],n;
        int ans1=0,ans2=0;
        int rate=-1;
        cin>>n;
        FOR(i,n)
        {
            cin>>ar[i];
        }
        for(int i=0;i<n-1;i++)
        {
            if(ar[i]>=ar[i+1])
            {
                ans1+=(ar[i]-ar[i+1]);
            }
        }
        for(int i=0;i<n-1;i++)
        {
            if(ar[i+1]<=ar[i])
            rate=max(rate,(ar[i]-ar[i+1]));
        }
        for(int i=0;i<n-1;i++)
        {
            ans2+=min(rate,ar[i]);
        }
        cout<<"Case #"<<a<<": "<<ans1<<" "<<ans2<<"\n";
    }
    return 0;
}
