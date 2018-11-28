/********************************/
/***  Coded By Ankush Sharma  ***/
/********************************/

#include<bits/stdc++.h>
using namespace std;

int main()
{
   // std::ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, c=0; cin>>t;
    c=t;
    while(t--)
    {
        int n; cin>>n;
        int diff=0, ans1=0, ans2=0, arr[n]; cin>>arr[0];
        for(int i=1; i<n; i++)
        {
            cin>>arr[i];
            diff=max(diff, arr[i-1]-arr[i]);
        }
        ans2+=min(arr[0], diff);
        for(int i=1; i<n; i++)
        {
            if(arr[i]<arr[i-1]) ans1+=(arr[i-1]-arr[i]);
            if(i<n-1) ans2+=min(arr[i], diff);
        }
        cout<<"Case #"<<c-t<<": ";
        cout<<ans1<<" "<<ans2<<"\n";
    }
    return 0;
}

