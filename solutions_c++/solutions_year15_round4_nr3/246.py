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

#define N 220

int n;
vector<string> vs[N];
void input() {
    RI(n);
    while ( getchar()!='\n' );
    REP(i,n) vs[i].clear();
    REP(i,n) {
        char line[8080];
        gets(line);
        for ( char *p=strtok(line," "); p; p=strtok(NULL," ") ) vs[i].PB(p);
    }
}

inline int bit( int x, int i ) {
    return (x>>i)&1;
}

map<string,int> wid;
VI vid[N];
void solve() {
    assert(n<=20);
    wid.clear();
    REP(i,n) vid[i].clear();
    REP(i,n) for ( auto s:vs[i] ) {
        if ( wid.count(s) ) continue;
        int id=SZ(wid)+1;
        wid[s]=id;
    }
    REP(i,n) for ( auto s:vs[i] ) vid[i].PB(wid[s]);
    int ans=1e9;
    REP(i,1<<n) {
        if ( bit(i,0)!=0 || bit(i,1)!=1 ) continue;
        vector<int> z(SZ(wid)+1);
        REP(j,n) for ( int k:vid[j] ) z[k]|=1<<bit(i,j);
        int now=0;
        for ( int j:z ) if ( j==3 ) now++;
        ans=min(ans,now);
    }
    printf("%d\n",ans);
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

