#include<bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define pb push_back
#define mem(a,p) memset(a,p,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define bitcount __builtin_popcount
#define gcd __gcd
#define rep(i,a,b) for(int i=a;i<b;++i)
#define all(a) a.begin(),a.end()
#define sz(a) ((int)(a.size()))
#define DREP(a) sort(all(a));a.erase(unique(all(a)),a.end())
#define debug(x,y) cerr<<x<<" "<<y<<" "<<endl;
#define ns ios_base::sync_with_stdio(false);cin.tie(0)
using namespace std;
#define VI vector<int>
#define PII pair<int,int>

int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,a,b,k;
    cin>>t;
    rep(i,1,t+1) {
        cin>>a>>b>>k;
        int ans=0;
        rep(i,0,a) {
            rep(j,0,b) {
                int tmp=i&j;
                if(tmp<k)
                    ans++;
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<"\n";
    }
    return 0;
}
