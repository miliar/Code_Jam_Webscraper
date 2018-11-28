// by shik {{{
#include <bits/stdc++.h>
#include <unistd.h>
#define SZ(x) ((int)(x).size())
#define ALL(c) begin(c),end(c)
#define REP(i,n) for ( int i=0; i<(int)(n); i++ )
#define REP1(i,a,b) for ( int i=(int)(a); i<=(int)(b); i++ )
#define FOR(it,c) for ( auto it=(c).begin(); it!=(c).end(); it++ )
#define MP make_pair
#define PB push_back
using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;

void RI() {}

template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}

void WI( int x ) {
    printf("%d\n",x);
}

template<typename... Args>
void WI(int head, Args... tail) {
    printf("%d ",head);
    WI(tail...);
}
/// }}}

#define N 1010

struct Rec {
    int x1,y1,x2,y2;
    void read() {
        RI(x1,y1,x2,y2);
    }
} rec[N];

int get_dis( int l1, int r1, int l2, int r2 ) {
    if ( r1<l2 ) return l2-r1;
    if ( r2<l1 ) return l1-r2;
    return 0;
}

int get_dis( const Rec &a, const Rec &b ) {
    int dx=get_dis(a.x1,a.x2,b.x1,b.x2);
    int dy=get_dis(a.y1,a.y2,b.y1,b.y2);
    int d=max(dx,dy)-1;
    if ( d<0 ) d=0;
    return d;
}

int w,h,n;
void input() {
    RI(w,h,n);
    REP1(i,1,n) rec[i].read();
}

int e[N][N],dis[N];
bool vis[N];
void solve() {
    rec[0]=Rec{-1,0,-1,h-1};
    rec[n+1]=Rec{w,0,w,h-1};
    n+=2;
    REP(i,n) REP(j,n) e[i][j]=get_dis(rec[i],rec[j]);
    memset(vis,0,n*sizeof(bool));
    vis[0]=1;
    REP(i,n) dis[i]=e[0][i];
    while ( !vis[n-1] ) {
        int who=-1;
        REP(j,n) if ( !vis[j] && (who==-1 || dis[j]<dis[who]) ) who=j;
        vis[who]=1;
        REP(j,n) if ( !vis[j] ) dis[j]=min(dis[j],dis[who]+e[who][j]);
    }
    int ans=dis[n-1];
    printf("%d\n",ans);
}

int main( int argc, char *argv[] ) {
    int n_case;
    RI(n_case);
    //fprintf(stderr,"n_case = %d\n",n_case);
    REP1(i,1,n_case) {
        input();
        if ( argc==2 && atoi(argv[1])!=i ) continue;
        if ( argc==3 && (atoi(argv[1])<i || atoi(argv[2])>i) ) continue;
        if ( 1 || argc!=1 ) {
            fprintf(stderr,"Running #%d...\n",i);
            fflush(stderr);
        }
        printf("Case #%d: ",i);
        solve();
        fflush(stdout);
    }
    return 0;
}

