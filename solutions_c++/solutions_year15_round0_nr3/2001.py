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
    cin.tie(0);
    freopen("C.out","w",stdout);
    freopen("C-small-attempt0.in","r",stdin);
    DRI(casos);
    FORU(cas,casos){
        debug(cas);
        DRII(n,c);
        n*=c;
        string s,st;
        cin>>st;
        FOR(i,c) s+=st;
        int obj=0;
        VVI mult = {{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
        VVI signe = {{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
        int simbol_act=0,signe_act=0;
        debug(s);
        debug(n);
        FOR(i,n){
            signe_act = (signe_act+signe[simbol_act][s[i]-'i'+1])&1;
            simbol_act = mult[simbol_act][s[i]-'i'+1];
            //cerr<<simbol_act<<' '<<signe_act<<',';
            if(obj==0 && simbol_act==1 && signe_act==0) ++obj;
            else if(obj==1 && simbol_act==3 && signe_act==0) ++obj;
        }
        //cerr<<endl;
        debug(obj);
        bool yes = false;
        if(obj==2 && simbol_act==0 && signe_act==1) yes = true;
        cout<<"Case #"<<cas<<": "<<(yes ? "YES": "NO")<<endl;
    }
}
