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
LD A[N],B[N];
LD dp[N][N];
LD calc() {
    mst(dp);
    dp[1][1] = A[1];
    dp[1][0] = 1-A[1];
    for(int k=2;k<=K;k++) {
        dp[k][0] = dp[k-1][0] * (1-A[k]);
        for(int y=1;y<=k;y++) {
            LD a=0;
            if(k-1 >= y)
                a = dp[k-1][y]*(1-A[k]);
            dp[k][y] = a+dp[k-1][y-1]*A[k];
            //printf("dp[%d][%d][%d]=%lf\n",i,k,y,dp[i][k][y]);
        }
    }
    return dp[K][K/2];
}
LD solve1() {
    sort(B+1,B+n+1);
    for(int j=1;j<=K/2;j++)
        A[j] = B[j];
    for(int j=K/2+1;j<=K;j++){
        A[j] = B[n-K+j];
    }
    return calc();
}
LD solve2() {
    sort(B+1,B+n+1);
    for(int j=1;j<=K;j++)
        A[j] = B[j];
    return calc();
}
LD solve3() {
    sort(B+1,B+n+1);
    for(int j=1;j<=K;j++)
        A[j] = B[n-j+1];
    return calc();
}
LD solve4() {
    FOR1(i,n)A[i]=B[i];
    int tmt=514;
    LD ans=0;
    while(tmt--){
        random_shuffle(A+1,A+n+1);
        maz(ans, calc());
    }
    return ans;
}
LD solve5() {
    LD ans=0;
    for(int i=0;i<(1<<n);i++)
        if(__count(i) == K) {
            int top=1;
            FOR(j,n) if(i&(1<<j)) A[top++]=B[j+1];
            LD a=calc();
            if(ans<a) {
                FOR1(z,K)printf("%lf ",A[z]);
                puts("");
                ans=a;
            }
            //maz(ans,calc());
        }
    return ans;
}
LD solve6() {
    sort(B+1,B+n+1);
    LD ans=0;
    for(int c=0;c<=K;c++) {
        int top=1;
        for(int j=1;j<=c;j++)
            A[top++] = B[j];
        for(int j=1;j<=K-c;j++)
            A[top++] = B[n-j+1];
        maz(ans,calc());
    }
    return ans;
}
int main() {
    RID(T);
    FOR1(w,T) {
        R(n,K);
        printf("Case #%d: ",w);
        FOR1(i,n) scanf("%lf",&B[i]);
        LD ans = solve1();
        maz(ans, solve2());
        maz(ans, solve3());
        //maz(ans, solve4());
        //maz(ans, solve5());
        maz(ans, solve6());
        printf("%.10lf\n",ans);
    }
    return 0;
}
/*
16 10
0.18 0.47 0.27 0.61 0.36 0.29 0.41 0.52 0.51 0.55 0.58 0.22 0.21 0.46 0.61 0.45
*/