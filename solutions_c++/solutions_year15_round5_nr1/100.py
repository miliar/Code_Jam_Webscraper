#define DEB

#include<bits/stdc++.h>
#include<unistd.h>
#define REP(i,m) for(int i=0;i<(m);++i)
#define REPN(i,m,in) for(int i=(in);i<(m);++i)
#define ALL(t) (t).begin(),(t).end()
#define CLR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define fr first
#define sc second

using namespace std;


#ifdef DEB
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
#else
#define dump(x) ;
#define prl ;
template<class T> void debug(T a,T b){ ;}
#endif

template<class T> void chmin(T& a,const T& b) { if(a>b) a=b; }
template<class T> void chmax(T& a,const T& b) { if(a<b) a=b; }

typedef long long int lint;
typedef pair<int,int> pi;

namespace std{
  template<class S,class T>
  ostream &operator <<(ostream& out,const pair<S,T>& a){
    out<<'('<<a.fr<<','<<a.sc<<')';
    return out;
  }
}

//const int INF=5e8;


int n,d;
int S[1000005],M[1000005];
void gen(int* ar){
  int s0,as,cs,rs;
  cin>>s0>>as>>cs>>rs;
  ar[0]=s0;

  REP(i,n-1){
    ar[i+1]=(ar[i]*as+cs)%rs;
  }
}

pi sal[1000005];

vector<int> g[1000005];
int par[1000005];
int cnt=0;

int mark[1000005],valid[1000005];

void dfs(int v){
  valid[v]=1;
  ++cnt;
  for(auto to:g[v]){
    if(mark[to] && !valid[to]) dfs(to);
  }
}

void sett(int id){
  mark[id]=1;
  if(par[id]==-1 || valid[par[id]]){
    dfs(id);
  }
}


void dfs2(int v){
  valid[v]=0;
  --cnt;
  for(auto to:g[v]){
    if(valid[to]) dfs2(to);
  }
}

void del(int id){
  mark[id]=0;
  if(valid[id]) dfs2(id);
}

int main(){
  int T;cin>>T;
  REP(setn,T){
    cnt=0;
    CLR(mark);CLR(valid);
    printf("Case #%d: ",setn+1);
    cin>>n>>d;

    REP(i,n) g[i].clear();

    gen(S);
    gen(M);

    par[0]=-1;
    REP(i,n-1){
      int a=i+1,b=M[i+1]%(i+1);
      g[b].pb(a);
      par[a]=b;
    }

    REP(i,n) sal[i]=mp(S[i],i);

    sort(sal,sal+n);

    int j=0;
    int res=0;
    REP(i,n){
      while(j<n && sal[j].fr<=sal[i].fr+d){
        sett(sal[j].sc);
        ++j;
      }
      chmax(res,cnt);


      del(sal[i].sc);
    }
    printf("%d\n",res);
  }

  return 0;

}



