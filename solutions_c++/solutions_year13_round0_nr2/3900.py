#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
#include<memory.h>
using namespace std;
#define pb push_back
#define ins insert
#define front(i) ((1<<(i))-1)
// 13C

#define rep(n)  for(int               repp = 0; repp <    (n); ++repp)
#define repc(n) for(int repp_b = (n), repp = 0; repp < repp_b; ++repp)
#define rst(a, v) memset(a, v, sizeof a)
#define cpy(a, b) memcpy(a, b, sizeof a)
#define rstn(a, v, n) memset(a, v, (n)*sizeof((a)[0]))
#define cpyn(a, b, n) memcpy(a, b, (n)*sizeof((a)[0]))
#define ast(b) if(DBG && !(b)) { printf("!! %d\n", __LINE__); while(1) getchar(); }
#define dout DBG && cout << ">>| "
#define pr(x) #x"=" << (x) << " | "
#define mk(x) DBG && cout << "**| "#x << endl
#define pra(arr, a, b) if(DBG) { \
    dout<<#arr"[] | "; \
    forlec(i, a, b) cout<<"["<<i<<"]="<<arr[i]<<" |"<<((i-(a)+1)%13?" ":"\n"); \
    if(((b)-(a)+1)%13) puts(""); \
  }
#define rd(type, x) type x; cin >> x
inline int     rdi() { int d; scanf("%d", &d); return d; }
inline char    rdc() { scanf(" "); return getchar(); }
inline string  rds() { rd(string, s); return s; }
inline double rddb() { double d; scanf("%lf", &d); return d; }
template<class T> inline bool updateMin(T& a, T b) { return a>b? a=b, true: false; }
template<class T> inline bool updateMax(T& a, T b) { return a<b? a=b, true: false; }

int i,j;
int map[102][102];
int n,m;
bool check(int x, int y){
  int high=map[x][y];
  bool judgex=true;
  bool judgey=true;
  for(int i=0;i<m;i++){
    if(map[x][i]>high){judgex=false;break;}
  }
  for(int i=0;i<n;i++){
    if(map[i][y]>high){judgey=false;break;}
  }
  return judgex||judgey;
}
bool cc(){
  int i,j;
  for(i=0;i<n;i++){
    for(j=0;j<m;j++){
      if(!check(i,j)){
        //cout<<(i)<<(j)<<endl;
        //getchar();
        return false;
      }
    }
  }
  return true;
}


int main(){
  int test;
  int cas=0;
  //FILE *fp=fopen("B-small-attempt0.in","r");
  //FILE *fp1=fopen("ou.txt","w");
  //freopen("B-large.in","r",stdin);
  //freopen("ou.txt","w",stdout);
  scanf("%d",&test);
  while(test--){
     scanf("%d%d",&n,&m);
     for(int i=0;i<n;i++){
       for(int j=0;j<m;j++){
         scanf("%d",&map[i][j]);
       }
     }
     printf("Case #%d: ",++cas);
     if(cc())printf("YES\n");
     else printf("NO\n");
  }
  return 0;
}
