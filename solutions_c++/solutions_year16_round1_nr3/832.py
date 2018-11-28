// @author kelvin
// #includes {{{
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;
// }}}
// #defines {{{
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define POP() pop_back()
#define F first
#define S second
#define PR printf
void RI() {}
template<typename... T>
void RI(int& head,T&... tail) {
    scanf("%d",&head);
    RI(tail...);
}
void PRI(int x) {
    printf("%d\n",x);
}
template<typename... Args>
void PRI(int head,Args... tail) {
    printf("%d ",head);
    PRI(tail...);
}
#define RF(x) scanf("%lf",&(x))
#define RS(x) scanf("%s",x)
#define DPRI(x) fprintf(stderr,"<"#x"=%d>\n",x)
#define DPRII(x,y) fprintf(stderr,"<"#x"=%d, "#y"=%d>\n",x,y)
#define DPRIII(x,y,z) fprintf(stderr,"<"#x"=%d, "#y"=%d, "#z"=%d>\n",x,y,z)
#define DPRIIII(x,y,z,w) fprintf(stderr,"<"#x"=%d, "#y"=%d, "#z"=%d "#w"=%d>\n",x,y,z,w)
#define DPRF(x) fprintf(stderr,"<"#x"=%lf>\n",x)
#define DPRS(x) fprintf(stderr,"<"#x"=%s>\n",x)
#define DPRMSG(x) fprintf(stderr,#x"\n")
#define DPRPII(x) fprintf(stderr,"<"#x"=(%d,%d)>\n",x.F,x.S)
typedef pair<int,int> pii;
// }}}
// #functions {{{
pii operator+(const pii &a,const pii &b) { return MP(a.F+b.F,a.S+b.S); }
pii operator-(const pii &a,const pii &b) { return MP(a.F-b.F,a.S-b.S); }
pii& operator+=(pii &a,const pii &b) { a.F+=b.F; a.S+=b.S; return a; }
pii& operator-=(pii &a,const pii &b) { a.F-=b.F; a.S-=b.S; return a; }
template <class T,class U>
bool cmp_second(const pair<T,U> &a,const pair<T,U> &b) { return a.second<b.second; }
template <class T>
T gcd(T a,T b) { a=abs(a); b=abs(b); while(b) { T t=b; b=a%b; a=t; } return a; }
template <class T>
pair<T,T> ext_gcd(T a,T b) {
   T a0=1,a1=0,b0=0,b1=1;
   if(a<0) { a=-a; a0=-1; }
   if(b<0) { b=-b; b1=-1; }
   while(b) {
      T t,q=a/b;
      t=b; b=a-b*q; a=t;
      t=b0; b0=a0-b0*q; a0=t;
      t=b1; b1=a1-b1*q; a1=t;
   }
   return MP(a0,a1);
}
inline int sg(int x) { return x?(x>0?1:-1):0; }
inline string concatenate_strings(vector<string> ss) {
   string s;
   for(int i=0;i<ss.size();i++)
      s+=ss[i];
   return s;
}
template <class T>
inline vector<T> read_from_string(string s) {
   vector<T> ret; stringstream ss(s,stringstream::in);
   while(1) { T x; ss>>x; ret.push_back(x); if(ss.eof()) break; }
   return ret;
}
// }}}

const int MAXN = 1050;

int n;
int out[MAXN];
int visid=0;
int vis[MAXN];
int dfsid,order[MAXN];
int ncyc;
vector<int> cyc[MAXN];
int cycid[MAXN];
int dp[MAXN];
int opt[MAXN],opt2[MAXN];

void dfs(int v) {
    vis[v]=visid;
    int u=out[v];
    if(vis[u]<visid) dfs(u);
    order[dfsid++]=v;
}

void dfs2(int v) {
    vis[v]=visid;
    cyc[ncyc].PB(v);
    int u=out[v];
    if(vis[u]<visid) dfs2(u);
}

int solve() {
    int maxcyc=0;
    ++visid;
    dfsid=0;
    for(int v=0;v<n;v++)
        if(vis[v]<visid) dfs(v);
    //
    ++visid;
    ncyc=0;
    memset(cycid,-1,sizeof(cycid));
    for(int o=0;o<n;o++) {
        int v=order[o];
        if(vis[v]==visid) continue;
        cyc[ncyc].clear();
        dfs2(v);
        //printf("(%d)\n",(int)cyc[ncyc].size());
        if(cyc[ncyc].size()>1) {
            for(auto u: cyc[ncyc]) {
                cycid[u]=ncyc;
            }
            maxcyc=max(maxcyc,(int)cyc[ncyc].size());
            ncyc++;
        }
    }
    //
    memset(dp,0,sizeof(dp));
    memset(opt,0,sizeof(opt));
    memset(opt2,0,sizeof(opt));
    for(int o=n-1;o>=0;o--) {
        int v=order[o];
        int u=out[v];
        int x=cycid[v];
        if(x>=0) {
            if(dp[v]>opt[x]) {
                opt2[x]=opt[x];
                opt[x]=dp[v];
            } else if(dp[v]>opt2[x]) {
                opt2[x]=dp[v];
            }
        } else {
            dp[u]=max(dp[u],dp[v]+1);
        }
    }
    //
    //for(int i=0;i<n;i++)
        //printf("%d: %d %d\n",i,dp[i],cycid[i]); puts("--");
    //
    int sol=0;
    for(int i=0;i<ncyc;i++)
        if(cyc[i].size()==2) sol+=opt[i]+opt2[i]+cyc[i].size();
    sol=max(maxcyc,sol);
    return sol;
}

int main(void)
{
    int t;
    RI(t);
    for(int cas=1; cas<=t; cas++) {
        RI(n);
        for(int i=0;i<n;i++) {
            RI(out[i]);
            out[i]--;
        }
        printf("Case #%d: %d\n",cas,solve());
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread
