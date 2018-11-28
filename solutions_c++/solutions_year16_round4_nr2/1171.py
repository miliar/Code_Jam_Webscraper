// There is nothing in a caterpillar that tells you its going to be a butterfly --------------------- !
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define f first
#define s second
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
ll x[2011],y[2011];
int main(){
    int n;
    cin >> n;
    map<pair<long double,long double>,ll>M;
    map<long double ,long double >M1;
    rep(i,n) cin >> x[i] >> y[i];
    rep(i,n){
        for(int j=i+1;j<n;j++){
            if(x[i]!=x[j]){
               long double m=y[j]-y[i];
                m/=(x[j]-x[i]);
               long double dis=(y[j]-y[i])*(y[j]-y[i])+(x[j]-x[i])*(x[j]-x[i]);
                M[{m,dis}]++;
            }
            else{
                long double dis=(y[j]-y[i])*(y[j]-y[i])+(x[j]-x[i])*(x[j]-x[i]);
                    M1[dis]++;
            }
        }
    }
    ll ans=0;
    for(auto x:M){
        ans+=(x.s*(x.s-1))/2;
    }
    for(auto x:M1){
        ans+=(x.s*(x.s-1))/2;
    }
    ans/=2;
    cout<<ans;
}
