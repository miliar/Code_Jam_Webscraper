#include<bits/stdc++.h>
#define MAX   1111
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define div   ___div
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define ignore   ___ignore
#define __builtin_popcount __builtin_popcountll
#define SQR(x) ((x)*(x))
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }
const int INF=(int)1e9+7;
int x[MAX],y[MAX],z[MAX],n;
bool vst[MAX];
int dis(int u,int v) {
    return (SQR(x[u]-x[v])+SQR(y[u]-y[v])+SQR(z[u]-z[v]));
}
void ignore(void) {
    int x; scanf("%d",&x);
}
void init(void) {
    scanf("%d",&n); ignore();
    FOR(i,1,n) {
        scanf("%d%d%d",&x[i],&y[i],&z[i]);
        REP(love,3) ignore();
    }
}
bool ok(int x) {
    memset(vst,false,sizeof vst);
    queue<int> q;
    vst[1]=true;
    q.push(1);
    while (!q.empty()) {
        int u=q.front();q.pop();
        if (u==2) return (true);
        FOR(v,1,n) if (!vst[v] && dis(u,v)<=x) {
            vst[v]=true;
            q.push(v);
        }
    }
    return (false);
}
int process(void) {
    int L=0;
    int R=INF;
    while (true) {
        if (L==R) return (L);
        if (R-L==1) return (ok(L)?L:R);
        int M=(L+R)>>1;
        if (ok(M)) R=M; else L=M+1;
    }
}
int main(void) {
    int t; scanf("%d",&t);
    FOR(i,1,t) {
        init();
        printf("Case #%d: %.7lf\n",i,sqrt(process()));
    }
    return 0;
}
