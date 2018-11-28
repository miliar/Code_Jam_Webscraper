#include<bits/stdc++.h>
using namespace std;

#define int long long

#define rep(i,n) for(int i=0;i<(n);i++)
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define fi first
#define se second
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;

template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

void solve(){
    string S;
    int K;

    cin>>S>>K;

    bool f[1111]={};
    rep(i,S.size())f[i]=(S[i]=='-');

    int ans=0;
    for(int i=0;i+K<=S.size();i++){
        if(f[i]){
            rep(j,K)f[i+j]^=1;
            ans++;
        }
    }

    if(accumulate(f,f+S.size(),0ll))cout<<"IMPOSSIBLE"<<endl;
    else cout<<ans<<endl;
}

signed main(){
    int T;
    cin>>T;
    rep(i,T){
        cout<<"Case #"<<i+1<<": ";
        solve();
    }
    return 0;
}
