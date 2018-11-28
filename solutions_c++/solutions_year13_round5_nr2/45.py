// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
typedef long long LL;
int sgn( LL x ) { return (x>0)-(x<0); }
struct P {
    LL x,y;
    P(){}
    P( LL _x, LL _y ):x(_x),y(_y){}
    void read() { scanf("%lld%lld",&x,&y); }
};
bool operator ==( P a, P b ) { return a.x==b.x && a.y==b.y; }
P operator -( P a, P b ) { return P(a.x-b.x,a.y-b.y); }
LL operator *( P a, P b ) { return a.x*b.y-a.y*b.x; }
LL X( P o, P a, P b ) { return (a-o)*(b-o); }
int dir( P o, P a, P b ) { return sgn(X(o,a,b)); }
bool is_jiao( LL a, LL b, LL c, LL d ) { return max(a,b)>=min(c,d) && max(c,d)>=min(a,b); }
bool is_on( P a, P c, P d ) {
    P b = a;
    if ( !is_jiao(a.x,b.x,c.x,d.x) ) return 0;
    if ( !is_jiao(a.y,b.y,c.y,d.y) ) return 0;
    if ( dir(a,b,c)*dir(a,b,d)>0 ) return 0;
    if ( dir(c,d,a)*dir(c,d,b)>0 ) return 0;
    return 1;
}
bool is_jiao( P a, P b, P c, P d ) {
    if ( !is_jiao(a.x,b.x,c.x,d.x) ) return 0;
    if ( !is_jiao(a.y,b.y,c.y,d.y) ) return 0;
    if ( dir(a,b,c)*dir(a,b,d)>0 ) return 0;
    if ( dir(c,d,a)*dir(c,d,b)>0 ) return 0;
    if ( a==c && !is_on(b,c,d) && !is_on(d,a,b) ) return 0;
    if ( a==d && !is_on(b,c,d) && !is_on(c,a,b) ) return 0;
    if ( b==c && !is_on(a,c,d) && !is_on(d,a,b) ) return 0;
    if ( b==d && !is_on(a,c,d) && !is_on(c,a,b) ) return 0;
    return 1;
}
#define N 1010
int n;
P p[N];
bool vis[N];
int path[N],sol[N];
LL ans;
bool chk( int lv, P a, P b ) {
    for ( int i=1; i<lv; i++ ) if ( is_jiao(p[path[i-1]],p[path[i]],a,b) ) return 0;
    return 1;
}
void go( int lv, LL area ) {
    if ( lv==n ) {
        if ( !chk(lv,p[path[n-1]],p[path[0]]) ) return;
        area+=p[path[n-1]]*p[path[0]];
        if ( area<0 ) area*=-1;
        if ( area>ans ) {
            ans=area;
            for ( int i=0; i<n; i++ ) sol[i]=path[i];
        }
        return;
    }
    for ( int i=1; i<n; i++ ) if ( !vis[i] ) {
        if ( !chk(lv,p[path[lv-1]],p[i]) ) continue;
        path[lv]=i;
        vis[i]=1;
        go(lv+1,area+p[path[lv-1]]*p[i]);
        vis[i]=0;
    }
}
void solve() {
    scanf("%d",&n);
    for ( int i=0; i<n; i++ ) p[i].read();
    ans=-1;
    go(1,0);
    //printf("ans = %lld\n",ans);
    for ( int i=0; i<n; i++ ) printf("%d%c",sol[i],i==n-1?'\n':' ');
}
int main()
{
    int num_case;
    scanf("%d",&num_case);
    for ( int i=1; i<=num_case; i++ ) {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
