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
const long double eps=0;
int n;
long double gv,gx;
long double r[N],c[N];
void input() {
    cin>>n>>gv>>gx;
    REP(i,n) cin>>r[i]>>c[i];
}

bool cmp( int a, int b ) {
    return c[a]<c[b];
}
int srt[N];

long double ub[N];
bool chk( long double m ) {
    REP(i,n) ub[i]=m*r[i];
    long double lt=0,rem=gv;
    REP(ii,n) {
        int i=srt[ii];
        long double v=min(rem,ub[i]);
        lt+=v*c[i];
        rem-=v;
    }
    if ( rem>0 ) return 0;
    long double rt=0;
    rem=gv;
    for ( int ii=n-1; ii>=0; ii-- ) {
        int i=srt[ii];
        long double v=min(rem,ub[i]);
        rt+=v*c[i];
        rem-=v;
    }
    return lt-eps<=gx*gv && gx*gv<=rt+eps;
}

void lasai() {
    if ( n==1 ) {
        if ( c[0]==gx ) printf("%.9Lf\n",gv/r[0]);
        else puts("IMPOSSIBLE");
    } else if ( n==2 ) {
        if ( c[0]>c[1] ) {
            swap(r[0],r[1]);
            swap(c[0],c[1]);
        }
        if ( c[0]>gx || c[1]<gx ) puts("IMPOSSIBLE");
        else if ( c[0]==c[1] ) {
            long double ans=gv/(r[0]+r[1]);
            printf("%.9Lf\n",ans);
        } else {
            long double v0=gv*(c[1]-gx)/(c[1]-c[0]);
            long double v1=gv*(gx-c[0])/(c[1]-c[0]);
            long double ans=max(v0/r[0],v1/r[1]);
            printf("%.9Lf\n",ans);
        }
    } else assert(0);
}

void solve() {
    REP(i,n) srt[i]=i;
    sort(srt,srt+n,cmp);
    if ( c[srt[0]]==c[srt[n-1]] ) {
        if ( c[srt[0]]==gx ) {
            long double sr=0;
            REP(i,n) sr+=r[i];
            long double ans=gv/sr;
            printf("%.9Lf\n",ans);
        } else {
            puts("IMPOSSIBLE");
        }
        return;
    }
    long double ll=0,rr=2e7;
    REP(i,100) {
        long double m=(ll+rr)/2;
        if ( chk(m) ) rr=m;
        else ll=m;
    }
    //lasai();
    if ( !chk(rr) ) puts("IMPOSSIBLE");
    else printf("%.9Lf\n",rr);
}

int main( int argc, char *argv[] ) {
    int n_case;
    RI(n_case);
    REP1(i,1,n_case) {
        input();
        if ( argc==2 && atoi(argv[1])!=i ) continue;
        dump(n,gx,gv,r[0],c[0],r[1],c[1]);
        printf("Case #%d: ",i);
        solve();
        fflush(stdout);
    }
    return 0;
}

