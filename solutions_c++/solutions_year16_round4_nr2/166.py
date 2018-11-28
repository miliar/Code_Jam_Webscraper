#include<bits/stdc++.h>
#define MAX   227
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
int n,m;
double prob[MAX],f[MAX][MAX];
void init(void) {
    scanf("%d%d",&n,&m);
    FOR(i,1,n) scanf("%lf",&prob[i]);
    sort(prob+1,prob+n+1);
}
double probTie(const vector<double> &prob) {
    assert(prob.size()==m);
    REP(i,m+1) REP(j,m/2+1) f[i][j]=0;
    f[0][0]=1.0;
    REP(i,m) REP(j,m/2+1) if (f[i][j]>0) {
        if (j<m/2) f[i+1][j+1]+=f[i][j]*prob[i];
        f[i+1][j]+=f[i][j]*(1.0-prob[i]);
    }
    return (f[m][m/2]);
}
double process(void) {
    double res=0.0;
    FOR(i,1,n-m+1) maximize(res,probTie(vector<double>(prob+i,prob+i+m)));
    FOR(i,0,m) {
        vector<double> tmp;
        FOR(j,1,i) tmp.push_back(prob[j]);
        REP(j,m-i) tmp.push_back(prob[n-j]);
        sort(ALL(tmp));
        maximize(res,probTie(tmp));
    }
    return (res);
}
int main(void) {
    int t; scanf("%d",&t);
    FOR(i,1,t) {
        init();
        printf("Case #%d: %.9lf\n",i,process());
    }
    return 0;
}
