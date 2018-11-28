//Done by Ferran Alet

#include<bits/stdc++.h>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-5
#define debug(x) cerr << #x << " = " << x << endl
#define Debug(v) cerr << #v << " = "; for(int wow=0;wow<v.size();++wow) cerr<<v[wow]<<' '; cerr<<endl
#define DEBUG(M) cerr << #M <<":"<<endl; for(int iM=0;iM<M.size();++iM) { for(int jM=0;jM<M[iM].size();++jM) cerr<<M[iM][jM]<<' '; cerr<<endl;} cerr<<endl
#define FOR(x,y) for(int x=0;x<y;x++)
#define FORS(x,y) for(int x=0;x<int(y.size());++x)
#define FORU(x,y) for(int x=1;x<=y;x++)
#define RFOR(x,y) for(int x=y-1;x>=0;--x)
#define DRI(x) int x; cin>>x
#define DRII(x,y) int x,y; cin>>x>>y
#define DRIII(x,y,z) int x,y,z; cin>>x>>y>>z
#define PB push_back
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<ld,ld> PDD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ld> VD;
typedef vector<VD> VVD;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;
typedef vector<PII > VP;
typedef vector<VP> VVP;


inline bool igual(ld a,ld b){
    return abs(a-b)<EPS;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("Bsmall.out","w",stdout);
    freopen("Bsmall.in","r",stdin);
    DRI(casos);
    FORU(cas,casos){
        int n;
        cin>>n;
        ld V,T;
        cin>>V>>T;
        vector<PDD> v(n); //rates,temp
        FOR(i,n) cin>>v[i].first>>v[i].second;
        sort(v.begin(),v.end());
        reverse(v.begin(),v.end());
        cout.precision(9);
        cout<<"Case #"<<cas<<": ";
        /*if(igual(T,v[0].second)){
            cout<<fixed<<V/v[0].first<<endl;
        }
        else if(igual(T,v[1].second)){
            cout<<fixed<<V/v[1].first<<endl;
        }
        else */
        if(n==1){
            if(igual(T,v[0].second)) cout<<fixed<<V/v[0].first<<endl;
            else cout<<"IMPOSSIBLE"<<endl;
        }
        else if(igual(v[0].second,v[1].second)){
            if(igual(T,v[0].second)) cout<<fixed<<V/(v[0].first+v[1].first)<<endl;
            else cout<<"IMPOSSIBLE"<<endl;
        }
        else if(T<v[0].second+EPS && T>v[1].second-EPS){
            ld x=V*ld(T-v[1].second)/ld(v[0].second-v[1].second);
            cout<<fixed<<max(x/v[0].first,(V-x)/v[1].first)<<endl;
        }
        else if(T<v[1].second+EPS && T>v[0].second-EPS){
            ld x=V*ld(T-v[1].second)/ld(v[0].second-v[1].second);
            cout<<fixed<<max(x/v[0].first,(V-x)/v[1].first)<<endl;
        }
        else cout<<"IMPOSSIBLE"<<endl;
    }
}
