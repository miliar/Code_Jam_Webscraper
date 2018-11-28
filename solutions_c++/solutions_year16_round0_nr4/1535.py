#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("outD.txt", "w", stdout);
    ll t, k, c, s;
    cin>>t;
    for(int r=1; r<=t; r++){
        cin>>k>>c>>s;
        ll n=1;
        for(int i=1; i<=c; i++){
            n=n*k;
        }
        ll d=n/k, m=1;
        cout<<"Case #"<<r<<": ";
        for(int i=1; i<=k; i++){
            cout<<m<<" ";
            m+=d;
        }
        cout<<"\n";
    }
    return 0;
}
