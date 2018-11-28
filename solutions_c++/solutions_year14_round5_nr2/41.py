// @author peter50216
// #includes {{{
#include <bits/stdc++.h>
using namespace std;
// }}}
// #defines {{{
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)
#define REPL(i,x) for(int i=0;x[i];i++)
#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define DRIII(x,y,z) int x,y,z;RIII(x,y,z)
#define RS(x) scanf("%s",x)
#define PI(x) printf("%d\n",x)
#define PIS(x) printf("%d ",x)
#define CASET int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define MP make_pair
#define PB push_back
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,-1,sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define F first
#define S second
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
// }}}
int hi[110],gi[110];
int dp[110][1100];
inline int divup(int a,int b){return (a+b-1)/b;}
inline void relax(int& a,int b){a=max(a,b);}
int p,q;
int numshot(int v){
  if(p<q){
    if(v%q==0||v%q>p)return -1;
    return v/q;
  }else{
    return (v-1)/q;
  }
}
int main(){
  CASET{
    int n;
    RIII(p,q,n);
    REP(i,n)RII(hi[i],gi[i]);
    int ans=0;
    int mxf=n*10;
    MS1(dp);
    dp[0][1]=0;
    REP(i,n){
      REP1(jj,0,mxf+1){
        int d=dp[i][jj];
        if(d==-1)continue;
        int j=jj-1;
        //printf("%d %d: %d\n",i,j,d);
        relax(dp[i+1][1+j+divup(hi[i],q)],d);
        int xx=j,h=hi[i];
        if(xx==-1){
          xx++;h-=q;
          if(h<=0)continue;
        }
        while(xx>0&&h>0&&numshot(h)==-1){
          xx--;h-=p;
        }
        if(h<=0)relax(dp[i+1][1+xx],d+gi[i]);
        else if(numshot(h)!=-1)relax(dp[i+1][1+xx+numshot(h)-1],d+gi[i]);
        else {
          while(h>0&&numshot(h)==-1){
            h-=p;
            h-=q;
          }
          if(h>0){
            relax(dp[i+1][1+xx+numshot(h)-1],d+gi[i]);
          }
        }
      }
    }
    ans=0;
    REP1(j,0,mxf+1)if(dp[n][j]!=-1)relax(ans,dp[n][j]);
    printf("Case #%d: %d\n",cas++,ans);
  }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

