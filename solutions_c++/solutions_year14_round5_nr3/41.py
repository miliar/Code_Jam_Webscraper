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

char s[20][3];
int id[20];
int n;
int ans;
const int INF=1000000000;
void dfs(int np,int inc,int outc,const set<int>& in,const set<int>& out){
  if(np==n){
    ans=min(ans,SZ(in)+inc);
    return;
  }
  int ii=id[np];
  if(s[np][0]=='E'){//in
    if(ii==0){
      if(outc>0)dfs(np+1,inc+1,outc-1,in,out);
      FOR(it,out){
        set<int> nin=in,nout=out;
        nin.insert(*it);nout.erase(*it);
        dfs(np+1,inc,outc,nin,nout);
      }
    }else{
      if(in.count(ii)){
        return;
      }else if(out.count(ii)){
        set<int> nin=in,nout=out;
        nin.insert(ii);nout.erase(ii);
        dfs(np+1,inc,outc,nin,nout);
      }else if(outc>0){
        set<int> nin=in;
        nin.insert(ii);
        dfs(np+1,inc,outc-1,nin,out);
      }
    }
  }else{
    if(ii==0){
      if(inc>0)dfs(np+1,inc-1,outc+1,in,out);
      FOR(it,in){
        set<int> nin=in,nout=out;
        nin.erase(*it);nout.insert(*it);
        dfs(np+1,inc,outc,nin,nout);
      }
    }else{
      if(out.count(ii)){
        return;
      }else if(in.count(ii)){
        set<int> nin=in,nout=out;
        nin.erase(ii);nout.insert(ii);
        dfs(np+1,inc,outc,nin,nout);
      }else if(inc>0){
        set<int> nout=out;
        nout.insert(ii);
        dfs(np+1,inc-1,outc,in,nout);
      }
    }
  }
}
int main(){
  CASET{
    RI(n);
    REP(i,n){
      scanf("%s%d",s[i],&id[i]);
    }
    ans=INF;
    printf("Case #%d: ",cas++);
    REP(inc,n+1){
      dfs(0,inc,10000,set<int>(),set<int>());
      if(ans!=INF)break;
    }
    if(ans==INF)puts("CRIME TIME");
    else printf("%d\n",ans);
  }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

