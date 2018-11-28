#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll arr[10000];
int main()
{
    ll t;
    cin>>t;
    for(int t1=1;t1<=t;t1++){
    ll n;
    cin>>n;
    ll case1=0;
    ll case2=0;
    for(int i=0;i<n;i++)
        cin>>arr[i];
    for(int i=0;i<n-1;i++)
    {
        if(arr[i]>arr[i+1])
            case1+=(arr[i]-arr[i+1]);
    }
    ll max=0;
    for(int i=0;i<n-1;i++)
    {
        if(arr[i]-arr[i+1]>max)
            max=(arr[i]-arr[i+1]);
    }
    for(int i=0;i<n-1;i++)
    {
        case2+=(min(arr[i],max));
    }
    cout<<"Case #"<<t1<<": "<<case1<<" "<<case2<<endl;}

}
