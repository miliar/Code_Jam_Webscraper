// @author 1rw6
// #includes {{{
//#include <bits/stdc++.h>
#include <cstdio>
#include <algorithm>
//using namespace std;
using std::pair;
using std::make_pair;
using std::min;
using std::max;
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
// }}}

#define MAXN 1050

const int inf=1000000000;

int cn,rn,vn;
int px1[MAXN],py1[MAXN],px2[MAXN],py2[MAXN];
int dist[MAXN];
bool vis[MAXN];

inline int between(int x1,int x2,int c) {
    return x1<=c&&c<=x2;
}

inline int p2p(int x1,int y1,int x2,int y2) {
    return max(abs(x1-x2),abs(y1-y2));
}

inline int p2r(int x,int y,int x1,int y1,int x2,int y2) {
    if(between(x1,x2,x)) {
        if(y<y1) return y1-y;
        else return y-y2;
    }
    if(between(y1,y2,y)) {
        if(x<x1) return x1-x;
        else return x-x2;
    }
    return min(min(p2p(x,y,x1,y1),p2p(x,y,x1,y2)),min(p2p(x,y,x2,y1),p2p(x,y,x2,y2)));
}

int go(int ax1,int ay1,int ax2,int ay2,int bx1,int by1,int bx2,int by2) {
    int sol=inf;
    sol=min(sol,p2r(ax1,ay1,bx1,by1,bx2,by2));
    sol=min(sol,p2r(ax1,ay2,bx1,by1,bx2,by2));
    sol=min(sol,p2r(ax2,ay1,bx1,by1,bx2,by2));
    sol=min(sol,p2r(ax2,ay2,bx1,by1,bx2,by2));
    sol=min(sol,p2r(bx1,by1,ax1,ay1,ax2,ay2));
    sol=min(sol,p2r(bx1,by2,ax1,ay1,ax2,ay2));
    sol=min(sol,p2r(bx2,by1,ax1,ay1,ax2,ay2));
    sol=min(sol,p2r(bx2,by2,ax1,ay1,ax2,ay2));
    return sol;
}
inline int go(int i,int j) {
    return go(px1[i],py1[i],px2[i],py2[i],px1[j],py1[j],px2[j],py2[j]);
}

int solve() {
    for(int i=0;i<vn;i++) {
        dist[i]=px1[i];
        vis[i]=0;
    }
    for(int t=0;t<vn;t++) {
        int v=-1;
        for(int i=0;i<vn;i++)
            if(!vis[i]&&(v==-1||dist[i]<dist[v])) v=i;
        vis[v]=1;
        //DPRII(v,dist[v]);
        for(int u=0;u<vn;u++) {
            if(vis[u]) continue;
            dist[u]=min(dist[u],dist[v]+go(v,u)-1);
        }
    }
    int sol=cn;
    for(int i=0;i<vn;i++)
        sol=min(sol,dist[i]+(cn-1)-px2[i]);
    return sol;
}

int main(void)
{
    int t,cas;
    RI(t);
    for(cas=1;cas<=t;cas++) {
        RI(cn,rn,vn);
        for(int i=0;i<vn;i++) {
            RI(px1[i],py1[i],px2[i],py2[i]);
        }
        int sol=solve();
        printf("Case #%d: %d\n",cas,sol);
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread

