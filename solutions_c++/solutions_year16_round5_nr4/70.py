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
int n,L;
char good[105][55];
char bad[55];
int main(){
  int T;
  cin>>T;
  for(int setn=1;setn<=T;++setn){
    cin>>n>>L;
    bool fail=false;
    REP(i,n){
      scanf("%s",good[i]);
      bool zero=false;
      REP(j,L) if(good[i][j]=='0') zero=true;
      if(!zero){
        fail=true;
      }
    }
    scanf("%s",bad);
    printf("Case #%d: ",setn);
    if(fail){
      puts("IMPOSSIBLE");
    }else{
      if(L==1){
        puts("? 0");
      }else{
        REP(i,L-1) putchar('?');
        printf(" 10?");
        REP(i,L+5) printf("01");
        puts("");
      }
    }
  }
  return 0;
}



