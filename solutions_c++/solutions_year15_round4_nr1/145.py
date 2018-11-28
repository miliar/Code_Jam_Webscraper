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

const int INF=5e8;

int h,w;
char buf[105][105];

int dx[]={0,1,0,-1},dy[]={1,0,-1,0};

int conv[305];

bool safe(int i,int j,int d){
  int cx=j+dx[d],cy=i+dy[d];
  while(cx>=0 && cy>=0 && cx<w && cy<h){
    if(buf[cy][cx]!='.'){
      return true;
    }
    cx+=dx[d];cy+=dy[d];
  }
  return false;
}

int main(){
  int t;cin>>t;
  conv['v']=0;
  conv['>']=1;
  conv['^']=2;
  conv['<']=3;

  REP(setn,t){
    printf("Case #%d: ",setn+1);

    cin>>h>>w;
    REP(i,h) scanf("%s",buf[i]);

    int res=0;
    REP(i,h) REP(j,w) if(buf[i][j]!='.'){
      int d=conv[buf[i][j]];
      if(safe(i,j,d)) ;
      else{
        ++res;
        int fail=1;
        REP(d2,4) if(safe(i,j,d2)) fail=0;
        if(fail) res=INF;
      }
    }
    if(res>=INF) puts("IMPOSSIBLE");
    else printf("%d\n",res);
  }

  return 0;

}



