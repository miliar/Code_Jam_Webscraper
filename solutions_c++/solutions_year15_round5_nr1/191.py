//by david942j
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <ctime>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <cstdlib>
#define openfile(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout)
#define mpr std::make_pair
#define lg(x) (31-__builtin_clz(x))
#define __count __builtin_popcount
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define FORit(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define pb push_back
#define RI(x) scanf("%d",&x)
#define RID(x) int x;RI(x)
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
inline int max(int a,int  b){return a>b?a:b;}
/*void RI() {}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}*/
const int N=2000010,INF=1e9;
const LD EPS=1e-6;

int m,n,D;
VI G[N];
LL S0,As,Cs,Rs;
LL M0, Am, Cm, Rm;
int S[N],M[N];
void make(int s[],LL s0,LL A,LL C, LL R) {
    s[0]=s0;
    FOR1(i,n-1)s[i]=(A*s[i-1]+C) % R;
}
bool dead[N];
int p[N],size[N];
int find(int x){return x==p[x]?x:p[x]=find(p[x]);}
void uni(int x,int y) {
    if(x==-1 || y==-1)return;
    x=find(x);y=find(y);
    if(x==y)return;
    p[x]=y;
    size[y]+=size[x];
    size[x]=0;
}
PII A[N];
void DFS(int x) {
    if(dead[x])return;
    dead[x]=true;
    size[find(x)]--;
    for(auto c:G[x]) {
        DFS(c);
    }
}
void cut(int x) {
    DFS(x);
}
int main() {
    int ww=1;
    RID(T);
    while(T--) {
        RI(n);
        RI(D);
        scanf("%lld%lld%lld%lld",&S0,&As,&Cs,&Rs);
        scanf("%lld%lld%lld%lld",&M0,&Am,&Cm,&Rm);
        make(S,S0,As,Cs,Rs);
        make(M,M0,Am,Cm,Rm);
        FOR1(i,n-1)M[i] %= i;
        M[0]=-1;
        FOR(i,n)G[i].clear();
        for(int i=1;i<n;i++) G[M[i]].pb(i);
        //FOR(i,n)printf("i=%d S=%d M=%d\n",i,S[i],M[i]);
        FOR(i,n)p[i]=i,size[i]=1;
        FOR(i,n)dead[i]=false;
        FOR(i,n)A[i] = mpr(S[i],i);
        sort(A,A+n);
        int ans=1;
        int w=n-1;
        FOR(i,n) if(S[i] > S[0]+D || S[i] < S[0]-D)cut(i);
        for(int i=n-1;i>=0;i--) {
            int now = A[i].Y;
            //printf("now=%d\n",now);
            while(w>=0  && A[w].X >= A[i].X-D) {
                if(dead[A[w].Y]){w--;continue;}
                uni(A[w].Y,M[A[w].Y]);
                //printf("merge %d to %d\n",A[w].Y,find(A[w].Y));
                w--;
            }
            maz(ans,size[0]);
            cut(now);
        }
        printf("Case #%d: %d\n",ww++,ans);
    }

    return 0;
}
/*
6 2
10 1 3 17
5 2 7 19
6 4
10 1 3 17
5 2 7 19
6 10
10 1 3 17
5 2 7 19
6 11
10 1 3 17
5 2 7 19
6 14
10 1 3 17
5 2 7 19
6 100
10 1 3 17
5 2 7 19
*/
