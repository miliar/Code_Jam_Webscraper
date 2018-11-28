#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define f first
#define s second
#define ll long long
#define mod 1000000007
#define rep(i,n) for(ll i=0;i<n;i++)
int main(){
    freopen("output.txt","w",stdout);

    cout<<"Case #"<<1<<": ";
    ll N=6;
    ll J=3;
    vector<vector<ll> >p;

    rep(mask,(1<<N)){
        if((mask&1)==0) continue;
        if((mask& (1<<(N-1)))==0 ) continue;
        if(mask>50) break;
        vector<ll>v(11,0);
        rep(j,N){
            for(ll k=2;k<=10;k++){
                v[k]*=k;
                v[k]+=(ll) ( (mask>>j)&1 ) ;
            }
        }

        vector<ll>ans(11,-1);

        for(int k=2;k<=10;k++){
            cerr<<v[k]<<" ";
            for(int p=2;p<=1000;p++){
                if(v[k]>=p) break;
                if(v[k]%p==0){
                    ans[k]=p;
                    break;
                }
            }

        }
        cerr<<"\n";
        bool ok=1;
        for(int k=2;k<=10;k++){
            if(ans[k]==-1) ok=0;
        }

        if(ok) p.pb(ans);
        if(p.size()==J) break;

    }
    for(auto x:p){
        for(int k=2;k<x.size();k++){
            cout<<x[k]<<" ";
        }
        cout<<"\n";
    }
}
