#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define PB pop_back
#define fs first
#define se second
#define eps (1e-8)
#define INF (0x3f3f3f3f)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

ll T,k,c,s;
int cas=0;
ll qpow(ll a,ll p){
    ll ans=1;
    while(p>0){
        if(p&1) ans=(ans*a);
        a*=a;p>>=1;
    }
    return ans;
}
int main(){
    freopen("/home/cwind/CppFiles/in","r",stdin);
    freopen("/home/cwind/CppFiles/out","w",stdout);
    cin>>T;
    while(T--){
        cin>>k>>c>>s;
        printf("Case #%d:",++cas);
        ll x=1;
        ll inc=qpow(k,c-1);
        for(int i=0;i<k;i++){
            cout<<" "<<x;
            x+=inc;
        }
        puts("");
    }
    return 0;
}