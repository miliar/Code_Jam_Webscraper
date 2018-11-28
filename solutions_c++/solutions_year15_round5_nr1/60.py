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

const int N=2e6+10;

struct DJS {
    int fa[N];
    void init( int n ) {
        REP(i,n) {
            fa[i]=i;
        }
    }
    int Find( int x ) {
        return x==fa[x]?x:fa[x]=Find(fa[x]);
    }
    void Union( int a, int b ) {
        a=Find(a);
        b=Find(b);
        assert(a!=b);
        fa[a]=b;
    }
} djs;

int n,d,s[N],m[N];
VI e[N];
void input() {
    int as,cs,rs;
    int am,cm,rm;
    RI(n,d);
    RI(s[0],as,cs,rs);
    RI(m[0],am,cm,rm);
    REP(i,n-1) s[i+1]=(1LL*s[i]*as+cs)%rs;
    REP(i,n-1) m[i+1]=(1LL*m[i]*am+cm)%rm;
    REP1(i,1,n-1) m[i]%=i;
    // dump(VI(s,s+n));
    // dump(VI(m,m+n));
    REP(i,n) e[i].clear();
    REP1(i,1,n-1) e[m[i]].PB(i);
}

int ss[N],iss[N];
bool cmp( int a, int b ) {
    return s[a]<s[b];
}

int sz[N];
bool bye[N];

void cut( int p, int l, int r ) {
    if ( bye[p] ) return;
    queue<int> q;
    int cnt=0,root=djs.Find(p);
    bye[p]=1;
    q.push(p);
    while ( !q.empty() ) {
        p=q.front(); q.pop();
        cnt++;
        djs.fa[p]=p;
        for ( int i:e[p] ) if ( !bye[i] && l<=iss[i] && iss[i]<=r ) {
            bye[i]=1;
            q.push(i);
        }
    }
    sz[root]-=cnt;
}

void solve() {
    REP(i,n) ss[i]=i;
    sort(ss,ss+n,cmp);
    REP(i,n) iss[ss[i]]=i;
    djs.init(n);
    REP(i,n) sz[i]=1;
    REP(i,n) bye[i]=0;
    int ans=0;
    for ( int i=0,j=0; i<n; i++ ) {
        while ( j<n && s[ss[j]]-s[ss[i]]<=d ) {
            if ( ss[j]!=0 ) {
                assert(djs.Find(ss[j])==ss[j]);
                djs.Union(ss[j],m[ss[j]]);
                sz[djs.Find(ss[j])]+=sz[ss[j]];
            }
            j++;
        }
        // dump(i,j,ss[i],ss[j-1],s[ss[i]],s[ss[j-1]],sz[0]);
        if ( s[ss[i]]<=s[0] && s[0]<=s[ss[j-1]] ) {
            ans=max(ans,sz[0]);
        }
        if ( ss[i]==0 ) break;
        cut(ss[i],i,j-1);
        djs.Find(rand()%n);
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

