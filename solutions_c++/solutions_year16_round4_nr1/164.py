#include<bits/stdc++.h>
#define MAX   13
#define LIM   20
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
const string fake="Z";
const string noAns="IMPOSSIBLE";
const string ch="PRS";
string best[MAX+3][3][2*LIM+3][2*LIM+3];
int winner(int x,int y) {
    assert(x!=y);
    if ((x+1)%3==y) return (x); else return (y);
}
string getBest(int n,int w,int p,int r) {
    int tmp=MASK(n)/3;
    p=p-tmp;
    r=r-tmp;
    if (p<-LIM || p>LIM || r<-LIM || r>LIM) return (fake);
    return (best[n][w][p+LIM][r+LIM]);
}
void prepare(void) {
    REP(i,MAX+1) REP(j,3) FOR(k,-LIM,LIM) FOR(l,-LIM,LIM)
        best[i][j][k+LIM][l+LIM]=fake;
    best[0][0][1+LIM][LIM]="P";
    best[0][1][LIM][1+LIM]="R";
    best[0][2][LIM][LIM]="S";
    REP(i,MAX) REP(w1,3) FOR(p1,max(0LL,MASK(i)/3-LIM),min(MASK(i),MASK(i)/3+LIM))
        FOR(r1,max(0LL,MASK(i)/3-LIM),min(MASK(i),MASK(i)/3+LIM))
            if (getBest(i,w1,p1,r1)!=fake)
                REP(w2,3) FOR(p2,max(0LL,MASK(i)/3-LIM),min(MASK(i),MASK(i)/3+LIM))
                    FOR(r2,max(0LL,MASK(i)/3-LIM),min(MASK(i),MASK(i)/3+LIM)) if (w1!=w2)
                        if (getBest(i,w2,p2,r2)!=fake) {
                            int sumP=p1+p2-MASK(i+1)/3;
                            int sumR=r1+r2-MASK(i+1)/3;
                            if (sumP<-LIM || sumP>LIM || sumR<-LIM || sumR>LIM) continue;
                            minimize(best[i+1][winner(w1,w2)][sumP+LIM][sumR+LIM],
                                getBest(i,w1,p1,r1)+getBest(i,w2,p2,r2));
                        }
}
string solve(int n,int r,int p) {
    string res=fake;
    REP(i,3) minimize(res,getBest(n,i,p,r));
    return (res==fake?noAns:res);
}
int main(void) {
    prepare();
    cerr<<"DONE"<<endl;
    int t; cin>>t;
    FOR(i,1,t) {
        int n,p,r,s; cin>>n>>r>>p>>s;
        printf("Case #%d: %s\n",i,solve(n,r,p).c_str());
    }
    return 0;
}
