// {{{ by shik
#include <bits/stdc++.h>
#include <unistd.h>
#define SZ(x) ((int)(x).size())
#define ALL(x) begin(x),end(x)
#define REP(i,n) for ( int i=0; i<int(n); i++ )
#define REP1(i,a,b) for ( int i=(a); i<=int(b); i++ )
#define FOR(it,c) for ( auto it=(c).begin(); it!=(c).end(); it++ )
#define MP make_pair
#define PB push_back
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#ifdef SHIK
template<typename T>
void _dump( const char* s, T&& head ) { cerr<<s<<"="<<head<<endl; }

template<typename T, typename... Args>
void _dump( const char* s, T&& head, Args&&... tail ) {
    int c=0;
    while ( *s!=',' || c!=0 ) {
        if ( *s=='(' || *s=='[' || *s=='{' ) c++;
        if ( *s==')' || *s==']' || *s=='}' ) c--;
        cerr<<*s++;
    }
    cerr<<"="<<head<<", ";
    _dump(s+1,tail...);
}

#define dump(...) do { \
    fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
    _dump(#__VA_ARGS__, __VA_ARGS__); \
} while (0)

template<typename Iter>
ostream& _out( ostream &s, Iter b, Iter e ) {
    s<<"[";
    for ( auto it=b; it!=e; it++ ) s<<(it==b?"":" ")<<*it;
    s<<"]";
    return s;
}

template<typename A, typename B>
ostream& operator <<( ostream &s, const pair<A,B> &p ) { return s<<"("<<p.first<<","<<p.second<<")"; }
template<typename T>
ostream& operator <<( ostream &s, const vector<T> &c ) { return _out(s,ALL(c)); }
template<typename T, size_t N>
ostream& operator <<( ostream &s, const array<T,N> &c ) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator <<( ostream &s, const set<T> &c ) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<( ostream &s, const map<A,B> &c ) { return _out(s,ALL(c)); }
#else
#define dump(...)
#endif

template<typename T>
void _R( T &x ) { cin>>x; }
void _R( int &x ) { scanf("%d",&x); }
void _R( long long &x ) { scanf("%" PRId64,&x); }
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

#ifdef SHIK
#define FILEIO(...)
#else
#define FILEIO(name) do {\
    freopen(name ".in","r",stdin); \
    freopen(name ".out","w",stdout); \
} while (0)
#endif

// }}}

const int N=110;
const int M=5;
const int L=22;
typedef double Double;

Double fac[N];
void predo() {
    fac[0]=1;
    REP1(i,1,N-1) fac[i]=fac[i-1]*i;
}

int n,fa[N],m;
char st[N],ww[M][L];
void input() {
    R(n);
    REP1(i,1,n) R(fa[i]);
    scanf("%s",st+1);
    R(m);
    REP(i,m) R(ww[i]);
}

VI e[N];
int sz[N];
Double dp[N];
void go( int p ) {
    sz[p]=1;
    dp[p]=1;
    double r=1;
    for ( int i:e[p] ) {
        go(i);
        sz[p]+=sz[i];
        dp[p]*=dp[i];
        r*=fac[sz[i]];
    }
    dp[p]*=fac[sz[p]-1]/r;
    // dump(p,dp[p],r);
}

int sample( vector<Double> v ) {
    Double s=0;
    int nv=SZ(v);
    REP(i,nv) s+=v[i];
    REP(i,nv) v[i]/=s;
    Double x=(rand()+0.5)/RAND_MAX;
    s=0;
    for ( int i=0; i<nv; i++ ) {
        s+=v[i];
        if ( s>=x ) return i;
    }
    assert(0);
}

VI poke( const VI &v, int x ) {
    VI nv;
    for ( int i:v ) {
        if ( i==x ) {
            for ( int j:e[i] ) nv.PB(j);
        } else {
            nv.PB(i);
        }
    }
    return nv;
}

Double calc( const VI &v ) {
    Double ans=1;
    Double r=1;
    int cnt=0;
    for ( int i:v ) {
        ans*=dp[i];
        cnt+=sz[i];
        r*=fac[sz[i]];
    }
    ans*=fac[cnt]/r;
    return ans;
}

bool sim( char w[L] ) {
    char t[N];
    VI v{0};
    REP(i,n+1) {
        vector<Double> f;
        for ( int j:v ) {
            auto nv=poke(v,j);
            f.PB(calc(nv));
        }
        int idx=sample(f);
        t[i]=st[v[idx]];
        v=poke(v,v[idx]);
    }
    t[n+1]=0;
    return strstr(t+1,w);
}

Double solve( char w[L] ) {
    const int T=2000;
    Double cnt=0;
    REP(i,T) if ( sim(w) ) cnt++;
    return cnt/T;
}

void solve() {
    REP1(i,0,n) e[i].clear();
    REP1(i,1,n) e[fa[i]].PB(i);
    go(0);
    // dump(dp[0]);
    vector<Double> ans;
    REP(i,m) {
        auto now=solve(ww[i]);
        ans.PB(now);
    }
    W(ans);
}

int main( int argc, char *argv[] ) {
    predo();
    int n_case;
    R(n_case);
    REP1(i,1,n_case) {
        input();
        if ( argc==2 && atoi(argv[1])!=i ) continue;
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
