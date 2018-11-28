//Done by Ferran Alet

#include<bits/stdc++.h>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
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

int busca(int pos, VVI &v, VI &E, VI &F){
    //debug(pos);
    if(pos==v.size()){
        int act=0;
        FOR(i,E.size()) if(E[i]>0 && F[i]>0) ++act;
        return act;
    }
    //Debug(v[pos]);
    FOR(i,v[pos].size()) E[v[pos][i]]++;
    int primer = busca(pos+1,v,E,F);
    FOR(i,v[pos].size()) E[v[pos][i]]--;
    FOR(i,v[pos].size()) F[v[pos][i]]++;
    int segon = busca(pos+1,v,E,F);
    FOR(i,v[pos].size()) F[v[pos][i]]--;
    return min(primer,segon);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("Csmall2.out","w",stdout);
    freopen("Csmall2.in","r",stdin);
    DRI(casos);
    FORU(cas,casos){
    debug(cas);
        int n;
        cin>>n;
        VI IE,IF;
        string s;
        getline(cin,s);
        getline(cin,s);
        stringstream ss;
        ss<<s;
        string st;
        map<string,int> M;
        int cont=0;
        while(ss>>st) {
            if(M.find(st)==M.end()) M[st]=cont++;
            IE.push_back(M[st]);
        }
        getline(cin,s);
        stringstream sss;
        sss<<s;
        while(sss>>st) {
            if(M.find(st)==M.end()) M[st]=cont++;
            IF.push_back(M[st]);
        }
        n-=2;
        vector<vector<int> > v(n);
        FOR(i,n){
            getline(cin,s);
            stringstream stst;
            stst<<s;
            while(stst>>st) {
                if(M.find(st)==M.end()) M[st]=cont++;
                v[i].push_back(M[st]);
            }
        }
        VI E(cont),F(cont);
        FOR(i,IE.size()) E[IE[i]]++;
        FOR(i,IF.size()) F[IF[i]]++;
        //Debug(E);
        //Debug(F);
        cout<<"Case #"<<cas<<": "<<busca(0,v,E,F)<<endl;
        /*int res=INF;
        FOR(S,(1<<n)){
            //if(S%1000==0) debug(S);
            set<int> E=IE;
            set<int> F=IF;
            FOR(i,n){
                if((S&(1<<i))!=0){
                    FOR(j,v[i].size()) E.insert(v[i][j]);
                }
                else FOR(j,v[i].size()) F.insert(v[i][j]);
            }
            int act=0;
            for(auto it=E.begin();it!=E.end();++it){
                if(F.find(*it)!=F.end()) ++act;
            }
            res=min(res,act);
        }
        cout<<"Case #"<<cas<<": "<<res<<endl;*/
    }
}
