#include<bits/stdc++.h>
using namespace std;
#define inf 123456789

int makeit( int a, int x )
{
    if( a<=x ) return 0;
    if(a%x==0) return (a/x) -1;
    return a/x;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;  cin>>t;
    for( int tt=1; tt<=t; ++tt ) {
        int n;  cin>>n;
        int a[n],minutes=0;
        multiset<int> s;
        for( int i=0; i<n; ++i )
            cin>>a[i];
        int ans=inf;
        for( int x=1; x<=1000; ++x ) {
            int sum=0;
            for( int i=0; i<n; ++i ) {
                sum+=makeit(a[i],x);
            }
            ans=min(ans,sum+x);
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
