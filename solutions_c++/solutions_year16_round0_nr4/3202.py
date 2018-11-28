#include<bits/stdc++.h>
#include<algorithm>
#define ll long long int
using namespace std;
ll cost[100005];
int main()
{
    ll i,j,t,s,c,k;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<j<<": ";
        for(i=1;i<=k;i++)
            cout<<i<<" ";
        cout<<endl;
    }
    return 0;
}
