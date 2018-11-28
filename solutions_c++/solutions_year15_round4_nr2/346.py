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
const int N=110,INF=1e9;
const LD EPS=1e-6;

int m,n;
int A[N];
char s[N][N];
int dx[]={1,0,-1,0},dy[]={0,1,0,-1};
LD V,C;
LD r[N],c[N];
bool same(LD a, LD b){return abs(a-b)<EPS;}
LD solve() {
    if(n==1) {
        if(same(c[0],C))return V/r[0];
        else return -1;
    }
    if(n==2) {
        if(same(c[0],c[1])) {
            if(!same(c[0],C))return -1;
            return V/(r[0]+r[1]);
        }
        LD d=r[0]*r[1]*(c[1]-c[0]);
        LD t0 = (r[1]*c[1]*V-V*C*r[1]) / d;
        LD t1 = (-r[0]*c[0]*V+V*C*r[0]) / d;
        if(t0 < -EPS || t1 < -EPS)return -1;
        return max(t0,t1);
    }
    assert(false);
}
int main() {
    int w=1;
    RID(T);
    while(T--) {
        RI(n);
        scanf("%lf%lf",&V,&C);
        FOR(i,n)scanf("%lf%lf",&r[i],&c[i]);
        LD ans=solve();
        if(ans<-0.5)printf("Case #%d: IMPOSSIBLE\n",w++);
        else printf("Case #%d: %.10lf\n",w++,ans);
    }

    return 0;
}
/*
3 3
..<
<^v
>v^
*/
