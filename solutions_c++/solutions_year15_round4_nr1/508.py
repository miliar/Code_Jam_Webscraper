#include <bits/stdc++.h>
using namespace std;
#define TR(i,v)       for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x)      cout<<#x<<" = "<<x<<endl
#define SIZE(p)       (int)(p).size()
#define MP(a,b)       make_pair((a),(b))
#define ALL(p)        (p).begin(),(p).end()
#define rep(i,n)      for(int i=0;i<(int)(n);++i)
#define REP(i,a,n)    for(int i=(a);i<(int)(n); ++i)
#define FOR(i,a,b)    for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,b,a)   for(int i=(int)(b);i>=(int)(a);--i)
#define CLR(x,y)      memset((x),(y),sizeof((x)))
#define fi first
#define se second
typedef long long LL;
typedef pair<int,int> pii;
char g[110][110];
int n,m;
vector<pii> L,R,U,D;
bool ok(int x,int y){
  FOR(j,y+1,m)if(g[x][j]!='.')return 1;
  FORD(j,y-1,1)if(g[x][j]!='.')return 1;
  FOR(i,x+1,n)if(g[i][y]!='.')return 1;
  FORD(i,x-1,1)if(g[i][y]!='.')return 1;
  return 0;
}
bool ck(){
  for(auto pp:L){
    int x=pp.fi,y=pp.se;    
    if(!ok(x,y))return 0;
  }
  for(auto pp:R){
    int x=pp.fi,y=pp.se;
    if(!ok(x,y))return 0;
  }
  for(auto pp:U){
    int x=pp.fi,y=pp.se;
    if(!ok(x,y))return 0;
  }
  for(auto pp:D){
    int x=pp.fi,y=pp.se;
    if(!ok(x,y))return 0;
  }
  return 1;
}
int main(){
  int T;scanf("%d",&T);
  FOR(cs,1,T){
    printf("Case #%d: ",cs);
    scanf("%d%d",&n,&m);
    FOR(i,1,n)scanf("%s",g[i]+1);    
    L.clear();R.clear();U.clear();D.clear();
    FOR(j,1,m){      
      FOR(i,1,n){
        if(g[i][j]!='.'){
          if(g[i][j]=='^'){
            U.push_back(MP(i,j));            
          }
          break;
        }
      }
      FORD(i,n,1){
        if(g[i][j]!='.'){
          if(g[i][j]=='v'){
            D.push_back(MP(i,j));
          }
          break;
        }
      }
    }
    FOR(i,1,n){
      FOR(j,1,m){
        if(g[i][j]!='.'){
          if(g[i][j]=='<'){
            L.push_back(MP(i,j));
          }
          break;
        }
      }
      FORD(j,m,1){
        if(g[i][j]!='.'){
          if(g[i][j]=='>'){
            R.push_back(MP(i,j));
          }
          break;
        }
      }
    }
    int res=0;
    if(!ck()){
      puts("IMPOSSIBLE");
      continue;
    }
    res=SIZE(L)+SIZE(R)+SIZE(U)+SIZE(D);
    printf("%d\n",res);
  }
  return 0;
}