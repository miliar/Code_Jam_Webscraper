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
char s[N][N];
void input() {
    RI(n,m);
    REP1(i,1,n) scanf("%s",s[i]+1);
}

const char sd[5]="<>^v";
int flg[N][N];
void solve() {
    memset(flg,0,sizeof(flg));
    REP1(i,1,n) {
        int l=-1,r=-1;
        REP1(j,1,m) if ( s[i][j]!='.' ) {
            if ( l==-1 ) l=j;
            r=j;
        }
        if ( l!=-1 ) flg[i][l]|=1;
        if ( r!=-1 ) flg[i][r]|=2;
    }
    REP1(i,1,m) {
        int l=-1,r=-1;
        REP1(j,1,n) if ( s[j][i]!='.' ) {
            if ( l==-1 ) l=j;
            r=j;
        }
        if ( l!=-1 ) flg[l][i]|=4;
        if ( r!=-1 ) flg[r][i]|=8;
    }
    int ans=0;
    REP1(i,1,n) REP1(j,1,m) {
        int x=flg[i][j];
        if ( x==15 ) {
            puts("IMPOSSIBLE");
            return;
        }
        int d=strchr(sd,s[i][j])-sd;
        if ( (x>>d)&1 ) ans++;
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

