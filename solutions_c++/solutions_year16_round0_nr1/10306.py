#include<bits/stdc++.h>
//#define yamin
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vii;

#define PB push_back
#define F first
#define S second
#define MP make_pair

#define PI acos(-1)
#define EPS 1e-9
#define inf 100000000
#define MOD 1000000007
//#define harmonic(n) 0.57721566490153286l+log(n)

#define mem(a,b) memset(a, b, sizeof(a) )
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a) * (a))

typedef vector<int>::iterator vit;
typedef set<int>::iterator sit;

inline bool checkBit(ll n, int i) { return n&(1LL<<i); }
inline ll setBit(ll n, int i) { return n|(1LL<<i);; }
inline ll resetBit(ll n, int i) { return n&(~(1LL<<i)); }

//int dx[] = {0, 0, +1, -1};
//int dy[] = {+1, -1, 0, 0};
//int dx[] = {+1, 0, -1, 0, +1, +1, -1, -1};
//int dy[] = {0, +1, 0, -1, +1, -1, +1, -1};

inline bool EQ(double a, double b) { return fabs(a-b) < EPS; }

//
//debug
#ifdef yamin
template < typename F, typename S >
ostream& operator << ( ostream& os, const pair< F, S > & p ) {
            return os << "(" << p.first << ", " << p.second << ")";
}

template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) {
            os << "{";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << *it;
                                            }
                    return os << "}";
}

template < typename T >
ostream &operator << ( ostream & os, const set< T > &v ) {
            os << "[";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << *it;
                                            }
                    return os << "]";
}

template < typename F, typename S >
ostream &operator << ( ostream & os, const map< F, S > &v ) {
            os << "[";
                for(auto it = v.begin(); it != v.end(); ++it) {
                                if( it != v.begin() ) os << ", ";
                                        os << it -> first << " = " << it -> second ;
                                            }
                    return os << "]";
}

#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)

void faltu () {
            cerr << endl;
}

template <typename T>
void faltu( T a[], int n ) {
            for(int i = 0; i < n; ++i) cerr << a[i] << ' ';
                cerr << endl;
}

template <typename T, typename ... hello>
void faltu( T arg, const hello &... rest) {
            cerr << arg << ' ';
                faltu(rest...);
}
#else
#define dbg(args...)
#endif

bool avail[10];

bool digit () {

    for ( int i = 0; i < 10; ++i ) {

            if ( !avail[i] ) return false;

    }

    return true;

}

void process ( ll n ) {//dbg ( n );

    while ( n ) {

            avail[n%10LL] = true;
            n/=10LL;

    }

}

int main () {

    ios_base::sync_with_stdio(0);

    freopen ( "A-large.in", "r", stdin );
    freopen ( "A-large.out", "w", stdout );

    int tc, cs = 0; cin >> tc;

    while ( tc-- ) {

            ll i = 0LL, n; cin >> n;

            cout << "Case #" << ++cs << ": ";

            if ( n == 0 ) {
                    cout << "INSOMNIA" << '\n';
                    continue;
            }

            mem ( avail, 0 );

            while ( !digit() ) {

                    ++i;
                    process ( n * i );

            }

            cout << n*i << '\n';

    }

    return 0;

}
