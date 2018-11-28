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

inline ll transforma(ll num, int b){
    ll res = 0;
    ll d = 1;
    while(num){
        res +=d * (num%2);
        num/=2;
        d*=b;
    }

    return res;
}
inline ll check_prime(ll num){
    for(ll i=2;i*i<=num;++i){
        if(num%i==0) return i;
    }
    return -1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("solC.out","w",stdout);
//  freopen(".in","r",stdin);
    int cont = 0;
    ll N = (1<<16);
    cout <<"Case #1:"<<endl;
    for(int S=N/2+1;S<N;S+=2){
        debug(S);
        VI div(9);
        bool ok=true;
        for(int b=2;b<=10;++b){
            ll num = transforma(S,b);
            div[b-2] = check_prime(num);
            if(div[b-2]==-1) {ok=false; break;}
        }
        if(ok){
            VI w;
            ll SS = S;
            while(SS) {w.push_back(SS%2); SS/=2;}
            reverse(w.begin(),w.end());
            FOR(i,w.size()) cout<<w[i];
            FOR(i,9) cout <<' '<< div[i];
            cout<<endl;
            cont++;
            if(cont==50) break;
        }
    }
    cout << cont <<endl;
}
