#include <bits/stdc++.h>

using namespace std;

#ifdef ONLINE_JUDGE
#define OJ 1
#else
#define OJ 0
#endif

#define dd				double
#define ll 				long long
#define pb 				push_back
#define mp 				make_pair
#define X				first
#define Y				second
#define forn( i, n ) 	for( ll i = 0; i < (ll) (n); i ++ )
#define endl 			'\n'

#define TIMESTAMP fprintf(stderr, "Execution time: %.3lf s.\n", (double)clock()/CLOCKS_PER_SEC)

struct __s { __s() {
		//srand( time( NULL ) );
		freopen( "C-small-attempt0.in", "r", stdin );
		freopen( "C-small-attempt0.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

ll f( string s ) {
    ll res = 0;
    forn( i, s.size() ) {
        res *= 27LL;
        ll c = s[i] - 'a' + 1LL;
        res += c;
    }
    return res % 1000000;
}

ll b[2][1111111];

int main( void ) {
    ll T;
    cin >> T;
    forn( t, T ) {
        ll n;
        cin >> n;
        string s;
        vector< ll > a[211];
        forn( i, 1111111 ) {
            b[0][i] = b[1][i] = 0;
        }
        getline( cin, s );
        getline( cin, s );
        ll j = 0;
        while( j < s.size() ) {
            string ss;
            while( j < s.size() && s[j] != ' ' ) {
                ss += s[j];
                j ++;
            }
            b[0][f( ss )] ++;
            j ++;
        }
        getline( cin, s );
        j = 0;
        ll ans0 = 0;
        while( j < s.size() ) {
            string ss;
            while( j < s.size() && s[j] != ' ' ) {
                ss += s[j];
                j ++;
            }
            ll k = f( ss );
            if( b[0][k] != 0 && b[1][k] == 0 )
                ans0 ++;
            b[1][k] ++;
            j ++;
        }
        n -= 2;
        forn( i, n ) {
            getline( cin, s );
            j = 0;
            while( j < s.size() ) {
                string ss;
                while( j < s.size() && s[j] != ' ' ) {
                    ss += s[j];
                    j ++;
                }
                a[i].pb( f( ss ) );
                j ++;
            }
        }

        ll ans = 1000000000LL;
        forn( i, 1 << n ) {
            ll res = 0;
            forn( j, n ) {
                bool k = i & ( 1 << j );
                forn( l, a[j].size() ) {
                    if( b[!k][a[j][l]] != 0 && b[k][a[j][l]] == 0 )
                        res ++;
                    b[k][a[j][l]] ++;
                }
            }
            forn( j, n ) {
                bool k = i & ( 1 << j );
                forn( l, a[j].size() ) {
                    b[k][a[j][l]] --;
                }
            }
            ans = min( ans, res );
        }
        cout << "Case #" << t + 1 << ": " << ans0 + ans << endl;

    }
	return 0;
}

