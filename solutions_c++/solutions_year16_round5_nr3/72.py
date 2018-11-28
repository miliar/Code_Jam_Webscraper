#define DEB
#include<bits/stdc++.h>
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

int n,s;
pair<pi,int> ps[1005];

bool vis[1005];
double len;
double sqr(double a){
  return a*a;
}
void dfs(int v){
  vis[v]=1;
  REP(i,n){
    double len2=sqr(ps[i].fr.fr-ps[v].fr.fr)+sqr(ps[i].fr.sc-ps[v].fr.sc)+sqr(ps[i].sc-ps[v].sc);
    len2=sqrt(len2);
    if(len2<=len && !vis[i]){
      dfs(i);
    }
  }
}
bool check(double len){
  ::len=len;
  CLR(vis);
  dfs(0);
  if(vis[1]) return true;
  return false;
}
int main(){
  int T;
  cin>>T;
  for(int setn=1;setn<=T;++setn){
    cin>>n>>s;
    REP(i,n){
      cin>>ps[i].fr.fr>>ps[i].fr.sc>>ps[i].sc;
      int a,b,c;cin>>a>>b>>c;
    }
    double lb=0,ub=10000;
    REP(hoge,60){
      double md=(lb+ub)/2;
      if(check(md)) ub=md;
      else lb=md;
    }

    printf("Case #%d: %.10f\n",setn,ub);
  }
  return 0;
}



