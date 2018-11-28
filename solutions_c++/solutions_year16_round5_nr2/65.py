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

int n,m;
int prevv[105];
vector<int> g[105];
char s[105];

char q[5][25];
int qlen[5];

int app[5];
const int M=10000;

int tmpar[105];
void shuffle(string& a,const string& b){
  int n=a.size()+b.size();
  REP(i,n){
    if(i<a.size()) tmpar[i]=0;
    else tmpar[i]=1;
  }
  random_shuffle(tmpar,tmpar+n);
  string tmp;tmp.resize(n);
  int c1=0,c2=0;
  REP(i,n){
    if(tmpar[i]==0) tmp[i]=a[c1++];
    else tmp[i]=b[c2++];
  }
  a=tmp;
}
string calc(int v){
  string res;
  for(auto to:g[v]){
    shuffle(res,calc(to));
  }
  string a;a+=s[v];
  res=a+res;
  return res;
}
void solve(){
  string t=calc(0);

  REP(i,m){
    REP(j,t.size()-qlen[i]+1){
      bool fail=0;
      REP(k,qlen[i]) if(t[j+k]!=q[i][k]){
        fail=1;break;
      }
      if(!fail){
        ++app[i];
        break;
      }
    }
  }
}

int main(){
  int T;
  cin>>T;
  for(int setn=1;setn<=T;++setn){
    dump(setn);
    CLR(app);
    cin>>n;
    ++n;
    REP(i,n) g[i].clear();
    REPN(i,n,1){
      cin>>prevv[i];
      if(~prevv[i]) g[prevv[i]].pb(i);
    }

    s[0]='z';
    scanf("%s",s+1);
    cin>>m;
    printf("Case #%d:",setn);
    REP(i,m){
      cin>>q[i];
      qlen[i]=strlen(q[i]);
    }
    REP(hoge,M) solve();
    REP(i,m){
      double res=app[i]/(double)M;
      printf(" %.5f",res);
    }
    puts("");
  }
  return 0;
}



