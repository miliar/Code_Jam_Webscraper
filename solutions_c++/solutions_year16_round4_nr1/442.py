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
#ifndef DAVID
#include <bits/stdc++.h>
#endif
#define openfile(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout)
#define mpr std::make_pair
#define lg(x) (31-__builtin_clz(x))
#define lgll(x) (63-__builtin_clzll(x))
#define __count __builtin_popcount
#define __countll __builtin_popcountll
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
template<typename T>
void _R( T &x ) { cin>>x; }
void _R( int &x ) { scanf("%d",&x); }
#ifdef PRId64
void _R( long long &x ) { scanf("%" PRId64,&x); }
#else
void _R( long long &x) {cin >> x;}
#endif
void _R( double &x ) { scanf("%lf",&x); }
void _R( char &x ) { scanf(" %c",&x); }
void _R( char *x ) { scanf("%s",x); }

void R() {}
template<typename T, typename... U>
void R( T& head, U&... tail ) {
    _R(head);
    R(tail...);
}

template<typename T>
void _W( const T &x ) { cout<<x; }
void _W( const int &x ) { printf("%d",x); }
template<typename T>
void _W( const vector<T> &x ) {
    for ( auto i=x.cbegin(); i!=x.cend(); i++ ) {
        if ( i!=x.cbegin() ) putchar(' ');
        _W(*i);
    }
}

void W() {}
template<typename T, typename... U>
void W( const T& head, const U&... tail ) {
    _W(head);
    putchar(sizeof...(tail)?' ':'\n');
    W(tail...);
}
#ifdef DAVID
#define debug(format, ...) fprintf(stderr, format, ##__VA_ARGS__)
#else
#define debug(...)
#endif
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}

const int N=100;
const int INF=1e9+7;
int n,r,p,s;
VI ans;
void gen(int s,int n,int &p,int &q,int &r) {
    if(n==0) {
        ans.pb(s);
        return;
    }
    if(s==0) {
        q++;
        gen(1,n-1,p,q,r);
        gen(0,n-1,p,q,r);
    }
    else if(s==1) {
        r++;
        gen(1,n-1,p,q,r);
        gen(2,n-1,p,q,r);
    }
    else if(s==2) {
        p++;
        gen(2,n-1,p,q,r);
        gen(0,n-1,p,q,r);
    }
}
void sort(int l,int n) {
    if(n==1) {
        if(ans[l]>ans[l+1]) swap(ans[l],ans[l+1]);
        return;
    }
    sort(l,n-1);
    sort(l+(1<<n-1),n-1);
    int r = l+(1<<n-1);
    bool e=false;
    FOR(i,(1<<n-1)) e =e|| (ans[l+i] > ans[r+i]);
    if(e) {
        FOR(i,(1<<n-1)) swap(ans[l+i],ans[r+i]);
    }
}
int main() {
    RID(T);
    FOR1(w,T) {
        R(n,r,p,s);
        printf("Case #%d: ",w);
        bool ok= false;
        FOR(i,3) {
            int A[3]={};
            ans.clear();
            A[i]=1;
            gen(i, n, A[0],A[1],A[2]);
            if(A[0]==p && A[1]==r && A[2]==s) {
                ok=true;
                //W(ans);
                sort(0,n);
                //W(ans);
                for(auto c:ans) if(c==0)putchar('P');
                    else if(c==1)putchar('R');
                    else putchar('S');
                puts("");
                break;
            }
        }
        if(!ok) puts("IMPOSSIBLE");
    }
    return 0;
}
/*

*/