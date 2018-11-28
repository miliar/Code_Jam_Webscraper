// @author peter50216
// #includes {{{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<functional>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<vector>
#include<iostream>
#include<sstream>
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

int ai[2010],bi[2010];
vector<int> ed[2010];
int dp[2010];
int vis[2010];
int out[2010];
inline void dfs(int np,set<int>& vis,set<int>& all){
    if(vis.count(np))return;
    if(!all.count(np))return;
    vis.insert(np);
    REP(i,ed[np].size())dfs(ed[np][i],vis,all);
}
inline void solve(int sm,set<int>& v){
    if(v.empty())return;
    int r=*v.begin();
    set<int> v1,v2;
    dfs(r,v1,v);
    v.erase(r);
    v1.erase(r);
    FOR(it,v)if(!v1.count(*it))v2.insert(*it);
    out[r]=sm+1+v1.size();
    solve(sm,v1);
    solve(out[r],v2);
}
int main(){
    CASET{
        DRI(n);
        REP(i,n)RI(ai[i]);
        REP(i,n)RI(bi[i]);
        REP(i,n)ed[i].clear();
        int lm=1;
        dp[1]=0;
        REP1(i,1,n-1){
            if(ai[i]==lm+1){
                ed[i].PB(dp[lm]);
                lm++;
            }else{
                if(ai[i]>1)ed[i].PB(dp[ai[i]-1]);
                ed[dp[ai[i]]].PB(i);
            }
            dp[ai[i]]=i;
        }
        dp[1]=n-1;
        lm=1;
        PER1(i,n-2,0){
            if(bi[i]==lm+1){
                ed[i].PB(dp[lm]);
                lm++;
            }else{
                if(bi[i]>1)ed[i].PB(dp[bi[i]-1]);
                ed[dp[bi[i]]].PB(i);
            }
            dp[bi[i]]=i;
        }
        set<int> all;
        REP(i,n)all.insert(i);
        solve(0,all);
        fprintf(stderr,"Case #%d:\n",cas);
        printf("Case #%d:",cas++);
        REP(i,n)printf(" %d",out[i]);puts("");
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

