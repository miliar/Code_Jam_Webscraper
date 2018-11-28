//Done by Ferran Alet

#include<bits/stdc++.h>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) //cerr << #x << " = " << x << endl
#define Debug(v) //cerr << #v << " = "; for(int wow=0;wow<v.size();++wow) //cerr<<v[wow]<<' '; //cerr<<endl
#define DEBUG(M) //cerr << #M <<":"<<endl; for(int iM=0;iM<M.size();++iM) { for(int jM=0;jM<M[iM].size();++jM) //cerr<<M[iM][jM]<<' '; //cerr<<endl;} //cerr<<endl
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

typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<double> VD;
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

int main(){
    ios_base::sync_with_stdio(false);
    //cin.tie(0);
    freopen("A-large.out","w",stdout);
    freopen("A-large.in","r",stdin);
    int casos;
    cin>>casos;
    int n,m;
    FORU(cas,casos){
        cin>>n>>m;
        debug(cas);
        VS t(n);
        FOR(i,n) cin>>t[i];
        Debug(t);
        int res=0;
        VVI col(n,VI(m));
        VVI fil(n,VI(m));
        FOR(i,n){
            FOR(j,m){
                fil[i][j]=(j ? fil[i][j-1] : 0);
                col[i][j]=(i ? col[i-1][j] : 0);
                if(t[i][j]!='.'){
                    fil[i][j]++;
                    col[i][j]++;
                }
            }
        }
        DEBUG(col);
        DEBUG(fil);
        FOR(i,n){
            FOR(j,m){
                //cerr<<i<<','<<j<<endl;
                //0
                if(t[i][j]=='.') continue;
                if(t[i][j]=='<' && j>0 && fil[i][j-1]>0) continue;
                if(t[i][j]=='>' && j<m-1 && fil[i][m-1]-fil[i][j]>0) continue;
                if(t[i][j]=='v' && i<n-1 && col[n-1][j]-col[i][j]>0) continue;
                if(t[i][j]=='^' && i>0 && col[i-1][j]>0) continue;
                //1
                ++res;
                //cerr<<"BAD: "<<i<<','<<j<<endl;
                if(j>0 && fil[i][j-1]>0) continue;
                if(j<m-1 && fil[i][m-1]-fil[i][j]>0) continue;
                if(i<n-1 && col[n-1][j]-col[i][j]>0) continue;
                if(i>0 && col[i-1][j]>0) continue;
                res=2*n*m;
            }
        }
        cout<<"Case #"<<cas<<": ";
        if(res>=2*n*m) cout<<"IMPOSSIBLE"<<endl;
        else cout<<res<<endl;
    }
}
