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

inline int bit( int x, int i ) {
    return (x>>i)&1;
}

const int N=514;
int r,c,n,a[N];
void input() {
    R(r,c);
    n=2*(r+c);
    assert(n<N);
    REP(i,n) R(a[i]);
}

int go( int p, bool m[] ) {
    int x,y,d;
    if ( p<c ) x=0,y=p,d=0; // down
    else if ( p<c+r ) x=p-c,y=c-1,d=1; // left
    else if ( p<c+r+c ) x=r-1,y=c-1-(p-c-r),d=2; // up
    else if ( p<c+r+c+r ) x=r-1-(p-c-r-c),y=0,d=3; // right
    else assert(0);
    while ( x>=0 && x<r && y>=0 && y<c ) {
        if ( m[x*c+y] ) { // [/]
            if ( d==0 ) y--,d=1;
            else if ( d==1 ) x++,d=0;
            else if ( d==2 ) y++,d=3;
            else if ( d==3 ) x--,d=2;
            else assert(0);
        } else { // [\]
            if ( d==0 ) y++,d=3;
            else if ( d==1 ) x--,d=2;
            else if ( d==2 ) y--,d=1;
            else if ( d==3 ) x++,d=0;
            else assert(0);
        }
    }
    if ( x<0 ) return y;
    if ( y>=c ) return c+x;
    if ( x>=r ) return c+r+(c-y-1);
    if ( y<0 ) return c+r+c+(r-x-1);
    assert(0);
}

bool check( bool m[] ) {
    REP(i,n) {
        if ( go(a[i],m)!=a[i^1] ) return 0;
    }
    return 1;
}

void output( bool m[] ) {
    REP(i,r) {
        REP(j,c) putchar(m[i*c+j]?'/':'\\');
        W("");
    }
}

bool sol1[N];
bool solve_small() {
    assert(r*c<=16);
    bool m[N];
    REP(i,1<<(r*c)) {
        REP(j,r*c) m[j]=bit(i,j);
        if ( check(m) ) {
            memcpy(sol1,m,sizeof(m));
            return 1;
        }
    }
    return 0;
}

void solve() {
    W("");
    REP(i,n) a[i]--;
    bool ans1=solve_small();
    if ( !ans1 ) W("IMPOSSIBLE");
    else output(sol1);
}

int main( int argc, char *argv[] ) {
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
