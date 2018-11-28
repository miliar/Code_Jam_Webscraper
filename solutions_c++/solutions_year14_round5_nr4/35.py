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

int ci[100];
int n;
vector<int> ed[100];
PII alle[110];
int vis[110],visid;
int vise[110];
const int INF=1000000000;
inline int run(int ap,int bp){
  int mv=-INF;
  int gv=0,ch=0;
  if(vis[ap]!=visid){
    vis[ap]=visid;
    ch=1;
    gv+=ci[ap];
  }
  bool used=0;
  REP(i,SZ(ed[ap])){
    int ii=ed[ap][i];
    if(vise[ii]==visid)continue;
    used=1;
    vise[ii]=visid;
    int r=run(bp,alle[ii].F+alle[ii].S-ap);
    mv=max(mv,gv-r);
    vise[ii]=visid-1;
  }
  if(!used){
    bool alld=1;
    REP(i,SZ(ed[bp])){
      int ii=ed[bp][i];
      if(vise[ii]!=visid){alld=0;break;}
    }
    if(alld){
      mv=gv-((vis[bp]==visid)?0:ci[bp]);
    }else mv=gv-run(bp,ap);
  }
  if(ch){
    vis[ap]=visid-1;
  }
  //printf("run ap=%d bp=%d %d\n",ap,bp,mv);
  return mv;
}
int main(){
  CASET{
    fprintf(stderr,"Case %d\n",cas);
    RI(n);
    REP(i,n){
      RI(ci[i]);
      ed[i].clear();
    }
    REP(i,n-1){
      DRI(b);
      int a=i;
      b--;
      alle[i]=MP(a,b);
      ed[a].PB(i);ed[b].PB(i);
    }
    MS0(vis);visid=0;
    MS0(vise);
    int maxa=-INF;
    REP(as,n){
      int maxb=-INF;
      REP(bs,n){
        visid++;
        int r=run(as,bs);
        //printf("%d %d: %d\n",as,bs,r);
        maxb=max(maxb,-r);
      }
      //printf("as=%d: %d\n",as,maxb);
      maxa=max(maxa,-maxb);
    }
    printf("Case #%d: %d\n",cas++,maxa);
  }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

