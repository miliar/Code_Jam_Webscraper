#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0;i<(n);++i)
#define lfo(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define rfo(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define lfoe(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define st first
#define nd second
#define sz(s) int(s.size())
#define pb push_back

template<class F, class T> T convert(F a, int p = -1) { stringstream ss; if (p >= 0) ss << fixed << setprecision(p); ss << a; T r; ss >> r; return r; }
template<class T> T gcd(T a, T b) { T r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
typedef long long ll;
typedef pair<int,int> II;
const int oo=int(1e9)+7;
const int dx[]={1,0,0,-1};
const int dy[]={0,-1,1,0};
const int N=int(1e6)+10;

int tc,x,n,ans;
multiset<int> s;

int main(){
    freopen("a.inp","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tc);
    //cin>>tc;
    lfo(tt,1,tc){
        scanf("%d%d",&n,&x);
        if (!s.empty()) s.clear();
        rep(i,n){
            int u;
            scanf("%d",&u);
            s.insert(u);
        }
        //lfoe(it,s) printf("%d ",*it);puts("");
        ans=0;
        while (!s.empty()){
            if (sz(s)==1){s.clear();ans++;break;}
            __typeof(s.begin()) it=s.end();
            --it;ans++;
            int here=*it;
            s.erase(it);
            __typeof(s.begin()) ti=s.lower_bound(x-here+1);
            if (ti!=s.begin()){
                --ti;
                s.erase(ti);
            }
        }
        printf("Case #%d: %d\n",tt,ans);
        //cout<<"Case #"<<tt<<": "<<'\n';
    }
    return 0;
}
