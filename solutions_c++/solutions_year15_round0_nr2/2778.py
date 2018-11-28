#include <bits/stdc++.h>

using namespace std;

#define rep(i,n)    for(int (i)=0; (i)<(int)(n); ++(i))
#define each(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); ++itr)
#define all(a)      a.begin(), a.end()
#define mp          make_pair
#define pb          push_back
#define F           first
#define S           second
#define mod         1000000009
typedef long long               ll;
typedef unsigned int            uint;
typedef unsigned long long      ull;

ll solve(vector<ll> & s){
    ll best=LLONG_MAX;
    for(ll i=1; i<1005; ++i){
        ll cur=0;
        rep(j,s.size()){
            cur+=(s[j]-1)/i;
        }
        best=min(best,cur+i);
    }
    return best;
}

int main(){
    vector<ll> qcase;
    int cases;
    ll res;
    cin>>cases;
    rep(i,cases){
        int smax;
        cin>>smax;
        rep(j,smax){
            ll d;
            cin>>d;
            qcase.pb(d);
        }
        res=solve(qcase);
        qcase.clear();
        cout<<"Case #"<<i+1<<": "<<res<<"\n";
    }
    return 0;
}
