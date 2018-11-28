#include <bits/stdc++.h>
using namespace std;
#define dprint(v) cerr << #v"=" << v << endl //;)
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define pb push_back
#define fst first
#define snd second
typedef long long ll;
typedef pair<int,int> ii;

int knt(ll x){
    int r=0;
    if(!x) return 1;
    while(x){
        r|=1<<(x%10);
        x/=10;
    }
    return r;
}

ll solve(ll n){
    int ap=0;
    for(ll ni=n; ; ni+=n){
        ap|=knt(ni);
        if(ni<=0) return -1;
        if(ap==(1<<10)-1) return ni;
    }
    return -1;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("asd.out", "w", stdout);
    ios::sync_with_stdio(0);
    ll n;
    int TC; cin >> TC;
    for(int TT=1; TT<=TC; TT++){
        cout << "Case #" << TT << ": ";
        cin >> n;
        ll ans=solve(n);
        if(ans==-1) cout << "INSOMNIA";
        else cout << ans;
        cout << endl;
    }
    return 0;
}
