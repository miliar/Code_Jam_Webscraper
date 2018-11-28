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

const int N=210;
const int INF=1e9+7;
int n,K;
char s[N][N];
int st;
VI v[30];
int p[N];
bool check(int t,int m) {
    if(t==n) return true;
    int id = p[t],cnt=0;
    for(auto c:v[id]) {
        if(m&(1<<c)) continue;
        cnt++;
    }
    if(cnt==0) return false;
    for(auto c:v[id]) {
        if(m&(1<<c));
        else {
            if(!check(t+1,m|(1<<c))) return false;
        }
    }
    return true;
}
bool ok(int s) {
    FOR(i,n)v[i].clear();
    FOR(i,n) FOR(j,n) if(s&(1<<(i*n+j))) v[i].pb(j);
    FOR(i,n) if(v[i].size()==0) return false;
    FOR(i,n)p[i]=i;
    do {
        if(!check(0,0)) return false;
    }while(next_permutation(p,p+n));
    return true;
}
int solve() {
    int ans=100000;
    FOR(i,(1<<(n*n))) {
        if((st & i) != st) continue;
        if(ans <= __count(st^i)) continue;
        if(ok(i)) ans = __count(st^i);
    }
    return ans;
}
int main() {
    RID(T);
    FOR1(w,T) {
        R(n);
        FOR(i,n) scanf("%s",s[i]);
        st = 0;
        FOR(i,n)FOR(j,n)if(s[i][j]=='1') st |= 1<<(i*n+j);
        printf("Case #%d: ",w);
        int ans=solve();
        printf("%d\n",ans);
    }
    return 0;
}
/*
16 10
0.18 0.47 0.27 0.61 0.36 0.29 0.41 0.52 0.51 0.55 0.58 0.22 0.21 0.46 0.61 0.45
*/