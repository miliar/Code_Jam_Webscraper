#include "bits/stdc++.h"
#pragma comment(linker, "/STACK:102400000,102400000")
#define debug(a) cout<<a<<endl
#define PB push_back
#define PF push_front
#define LB lower_bound
#define fr(x) freopen(x,"r",stdin)
#define fw(x) freopen(x,"w",stdout)
#define in(x) (read(x))
#define iout(x) printf("%d\n",x)
#define lout(x) printf("%lld\n",x)
#define UB upper_bound
#define REP(x,l,u) for(ll x = l;x<u;x++)
#define RREP(x,l,u) for(ll x = l;x>=u;x--)
#define complete_unique(a) a.erase(unique(a.begin(),a.end()),a.end())
#define mst(x,a) memset(x,a,sizeof(x))
#define PII pair<int,int>
#define CI  const int&
#define CD  const double&
#define CL  const ll&
#define CC  const char&
#define MP make_pair
#define lowbit(x) (x&(-x))
#define lson (ind<<1)
#define rson (ind<<1|1)
#define se second
#define fi first
#define sz(x) ((int)x.size())
typedef  long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ld;
using namespace std;
const int block_size = 320;
typedef complex<ll> point;
const ll mod = 1e9+7;
const ld eps = 1e-9;
const int inf = mod;
template<typename T>
int sign(const T&a){if(a<0)return -1;if(a>0)return 1;return 0;}


template<typename T> inline void read(T &x){
    x = 0; T f = 1; char ch = getchar();
    while (!isdigit(ch)) {if (ch == '-') f = -1; ch = getchar();}
    while (isdigit(ch))  {x = x * 10 + ch - '0'; ch = getchar();}
    x *= f;
}

int t;

int s;
bitset<10>vis;
bool check(){
    REP(i,0,10){
        if(!vis[i])return false;
    }
    return true;
}
void add(int a){
    while (a) {
        vis[a%10] = 1;
        a/=10;
    }
}
void solve(){
    vis.reset();
    if(s == 0){
        cout<<"INSOMNIA"<<endl;
    }else{
        for(int i = s;;i+=s){
            add(i);
            if(check()){
                cout<<i<<endl;
                return;
            }
        }
    }
}

int main(){
    cin>>t;
    REP(i,1,t+1){
        cin>>s;
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}