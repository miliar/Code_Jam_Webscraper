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
char ch[]="CJ";
int solve(string s) {
    int res=0;
    int numPush=0;
    string cur;
    REP(i,s.size()) {
        if (cur.empty()) {
            cur.push_back(s[i]);
            res++;
            numPush++;
            continue;
        }
        if (numPush>=s.size()/2) {
            if (cur.back()==s[i]) res++;
            cur.pop_back();
            continue;
        }
        if (cur.back()==s[i]) {
            res++;
            cur.pop_back();
        } else {
            res++;
            numPush++;
            cur.push_back(s[i]);
        }
    }
    return (5*res);
}
int main(void) {
    int t; cin>>t;
    FOR(i,1,t) {
        string s; cin>>s;
        printf("Case #%d: %d\n",i,solve(s));
    }
    return 0;
}
