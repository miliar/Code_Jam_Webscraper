#include<bits/stdc++.h>
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
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }
const char noAns[]="IMPOSSIBLE";
void process(int tc) {
    printf("Case #%d: ",tc);
    int n,len; cin>>n>>len;
    bool ok=true;
    REP(love,n) {
        string s; cin>>s;
        if (s==string(len,'1')) ok=false;
    }
    string s; cin>>s;
    if (!ok) {
        printf("%s\n",noAns);
        return;
    }
    if (len==1) {
        printf("? 0\n");
        return;
    }
    REP(love,len-1) printf("?");
    printf(" 10?");
    REP(love,70) printf("10"); printf("\n");
}
int main(void) {
    int t; cin>>t;
    FOR(i,1,t) process(i);
    return 0;
}
