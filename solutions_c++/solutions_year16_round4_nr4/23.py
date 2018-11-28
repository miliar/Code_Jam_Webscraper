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

const int INF=5e8;


char buf[5][5];

int able[5][5];
int n;

bool check(){
  int perm[4],perm2[4];
  REP(i,n) perm[i]=i;//arrival
  do{
    REP(i,n) perm2[i]=i;//operate machine
    do{
      bool mark[4]={0};
      REP(i,n){
        if(!able[perm[i]][perm2[i]]){
          bool suc=false;
          REP(j,n) if(able[perm[i]][j] && !mark[j]) suc=true;
          if(!suc){
            return false;
          }else{
            break;
          }
        }else{
          mark[perm2[i]]=true;
        }
      }
    }while(next_permutation(perm2,perm2+n));
  }while(next_permutation(perm,perm+n));
  return true;
}

int main(){
  int T;cin>>T;
  for(int setn=1;setn<=T;++setn){
    printf("Case #%d: ",setn);
    cin>>n;
    REP(i,n) scanf("%s",buf[i]);

    CLR(able);

    int res=INF;
    REP(bit,(1<<(n*n))){
      REP(i,n) REP(j,n) able[i][j]=(buf[i][j]-'0')|(bit>>(i*n+j)&1);

      if(check()) chmin(res,__builtin_popcount(bit));
    }
    cout<<res<<endl;
  }
  return 0;
}



