#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    freopen("largemushroom.in", "rt", stdin);
    freopen("round1large.out", "wt", stdout);
    int t,i,j,n,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n;
        int a[n],mx=0,ans1=0,ans2=0;
        for(i=0;i<n;i++)
            cin>>a[i];

        for(i=1;i<n;i++)
        {
            if((a[i]-a[i-1])<0)
                ans1+=(a[i-1]-a[i]);
            mx=max(mx, (a[i-1]-a[i]) );
        }
        for(i=0;i<n-1;i++)
        {
            if(a[i]>=mx)
                ans2+=mx;
            else
                ans2+=a[i];
        }
        cout<<"Case #"<<k<<": "<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
