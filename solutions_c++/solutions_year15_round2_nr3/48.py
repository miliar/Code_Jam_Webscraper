//Done by Ferran Alet

#include<bits/stdc++.h>
#include<queue>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define Debug(v) cerr << #v << " = "; for(ll wow=0;wow<v.size();++wow) cerr<<v[wow]<<' '; cerr<<endl
#define DEBUG(M) cerr << #M <<":"<<endl; for(ll iM=0;iM<M.size();++iM) { for(ll jM=0;jM<M[iM].size();++jM) cerr<<M[iM][jM]<<' '; cerr<<endl;} cerr<<endl
#define FOR(x,y) for(ll x=0;x<y;x++)
#define FORS(x,y) for(ll x=0;x<ll(y.size());++x)
#define FORU(x,y) for(ll x=1;x<=y;x++)
#define RFOR(x,y) for(ll x=y-1;x>=0;--x)
#define DRI(x) ll x; cin>>x
#define DRII(x,y) ll x,y; cin>>x>>y
#define DRIII(x,y,z) ll x,y,z; cin>>x>>y>>z
#define PB push_back
#define SZ(X) ((ll)(X).size())
#define ALL(X) (X).begin(), (X).end()

using namespace std;

typedef long long ll;
typedef pair<ll,ll> PII;
typedef vector<ll> VI;
typedef vector<VI> VVI;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<string> VS;
typedef map<ll,ll> MII;
typedef MII::iterator iMII;
typedef vector<PII > VP;
typedef vector<VP> VVP;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("C-large.out","w",stdout);
    freopen("C-large.in","r",stdin);
    DRI(casos);
    FORU(cas,casos){
        debug(cas);
        DRI(n);
        vector<ll> minim,maxim;
        vector<ll> M;
        vector<ll> X;
        FOR(i,n){
            DRIII(x,H,m);
            FOR(h,H){
                M.push_back(m+h);
                minim.push_back((360LL-x)*(m+h));
                maxim.push_back((360LL*(2LL)-x)*(m+h));
                X.push_back((360LL*(2LL)-x));
            }
        }
        priority_queue< PII > pq;
        ll H = minim.size();
        FOR(i,minim.size()) {
            pq.push(PII(-minim[i],-1));
            pq.push(PII(-maxim[i],i));
        }
        ll pos=0;
        bool primer = true;
        ll res = INF;
        ll cont= minim.size();
        ll queden = minim.size();
        ll ant=-1;
        while(cont-queden<res){
            while((primer or pq.top().first==ant)){
                ant = pq.top().first;
                ll tio = pq.top().second;
                pq.pop();
                if(tio==-1){
                    cont--;
                    --queden;
                }
                else{
                    cont++;
                    X[tio]+=360LL;
                    pq.push(PII(-X[tio]*M[tio],tio));
                }
                primer = false;
            }
            primer = true;
            res = min(res,cont);
        }
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
}
