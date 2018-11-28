#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<memory.h>
#include<cstdlib>
using namespace std;
const int N=1000001;
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
int tot;
long long sum[N];
bool pallo(long long x){
    long long sum1=0;
    for(i=x;i;i/=10){
        sum1=sum1*10+i%10;
    }
    return sum1==x;
}
void init(){
    for(long long i=0;i<N;i++){
        long long cc=i*i;
        if(pallo(i)&&pallo(cc))sum[tot++]=cc;
    }
}
int main(){
  int test;
  int cas=0;
  int l,r;
  //freopen("C-small-attempt0.in","r",stdin);
  //freopen("ou.txt","w",stdout);
  init();
  scanf("%d ",&test);
  while(test--){
      int anssum=0;
      scanf("%d%d",&l,&r);
      for(int i=0;i<tot;i++){
          if(l<=sum[i]&&sum[i]<=r)anssum++;
      }
      printf("Case #%d: ",++cas);
      printf("%d\n",anssum);
  }
  //system("pause");
  return 0;
}
