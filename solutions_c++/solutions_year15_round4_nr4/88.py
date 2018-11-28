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

#define N 110

int n,m;
void input() {
    RI(n,m);
}

int b[N][N];

const int dx[]={1,0,-1,0};
const int dy[]={0,1,0,-1};
bool _chk( int x, int y ) {
    if ( !b[x][y] ) return 1;
    int c=0;
    REP(i,4) {
        int xx=(x+dx[i]);
        int yy=(y+dy[i]+m)%m;
        if ( xx<0 || xx>=n ) continue;
        if ( b[xx][yy]==0 ) return 1;
        if ( b[xx][yy]==b[x][y] ) c++;
    }
    return c==b[x][y];
}

bool chk( int x, int y ) {
    if ( !_chk(x,y) ) return 0;
    REP(i,4) {
        int xx=(x+dx[i]);
        int yy=(y+dy[i]+m)%m;
        if ( xx<0 || xx>=n ) continue;
        if ( !_chk(xx,yy) ) return 0;
    }
    return 1;
}

set<vector<VI>> sol;
void dfs( int x, int y ) {
    if ( y==m ) {
        dfs(x+1,0);
        return;
    }
    if ( x==n ) {
        vector<VI> v;
        REP(i,m) {
            VI col;
            REP(j,n) col.PB(b[j][i]);
            v.PB(col);
        }
        vector<VI> mi=v;
        REP(i,m) {
            v.push_back(v[0]);
            v=vector<VI>{v.begin()+1,v.end()};
            if ( v<mi ) mi=v;
        }
        sol.insert(mi);
        return;
    }
    REP1(i,1,3) {
        b[x][y]=i;
        if ( !chk(x,y) ) continue;
        dfs(x,y+1);
    }
    b[x][y]=0;
}

void slow() {
    sol.clear();
    dfs(0,0);
    printf("%d\n",SZ(sol));
    //dump(sol);
}

void solve() {
    if ( n<=6 && m<=6 ) {
        slow();
    } else {
        assert(0);
    }
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

