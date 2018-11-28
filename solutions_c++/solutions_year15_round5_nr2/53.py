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

void RI() {}

template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}

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
} while (0);

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
template<typename T>
ostream& operator <<( ostream &s, const set<T> &c ) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<( ostream &s, const map<A,B> &c ) { return _out(s,ALL(c)); }

// }}}

#define N 1010
int n,k,s[N];
void input() {
    RI(n,k);
    REP1(i,1,n-k+1) RI(s[i]);
}

LL l[N],r[N];
void solve() {
    REP1(i,1,k) {
        l[i]=r[i]=0;
        LL x=0;
        for ( int j=i; j<=n-k; j+=k ) {
            x+=s[j+1]-s[j];
            l[i]=min(l[i],x);
            r[i]=max(r[i],x);
        }
    }
    int w=1;
    REP1(i,1,k) if ( r[i]-l[i]>r[w]-l[w] ) w=i;
    LL sl=0,sr=0;
    REP1(i,1,k) {
        LL lb=l[w]-l[i];
        LL rb=r[w]-r[i];
        assert(lb<=rb);
        sl+=lb;
        sr+=rb;
    }
    LL x=s[1];
    if ( x>sr ) x-=(x-sr)/k*k;
    if ( x<sl ) x+=(sl-x)/k*k;
    bool good=0;
    REP1(i,-100,+100) {
        LL xx=x+i*k;
        if ( sl<=xx && xx<=sr ) good=1;
    }
    if ( good ) printf("%lld\n",r[w]-l[w]);
    else printf("%lld\n",r[w]-l[w]+1);
}

int main( int argc, char *argv[] ) {
    int n_case;
    RI(n_case);
    REP1(i,1,n_case) {
        input();
        if ( argc==2 && atoi(argv[1])!=i ) continue;
        printf("Case #%d: ",i);
        solve();
        fflush(stdout);
    }
    return 0;
}

