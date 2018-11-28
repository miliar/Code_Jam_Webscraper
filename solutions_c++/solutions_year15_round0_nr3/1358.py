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

char mul( char a, bool &b, char c ) {
    if( c == '1' )
        return a;
    else if( a == '1' )
        return c;
    else if( a == 'i' ) {
        if( c == 'i' ) {
            b = !b;
            return '1';
        } else if( c == 'j' )
            return 'k';
        else if( c == 'k' ) {
            b = !b;
            return 'j';
        }
    } else if( a == 'j' ) {
        if( c == 'i' ) {
            b = !b;
            return 'k';
        }
        else if( c == 'j' ) {
            b = !b;
            return '1';
        }
        else if( c == 'k' )
            return 'i';
    } else if( a == 'k' ) {
        if( c == 'i' )
            return 'j';
        else if( c == 'j' ) {
            b = !b;
            return 'i';
        }
        else if( c == 'k' ) {
            b = !b;
            return '1';
        }
    }
}

int main( void ) {
    ll T;
    cin >> T;
    forn( t, T ) {
        ll l, x;
        cin >> l >> x;
        string c, s;
        cin >> c;
        forn( i, x ) {
            s += c;
        }
        char a = '1';
        bool b = true;
        vector< ll > ii, kk;
        for( ll i = 0; i < s.size(); i ++ ) {
            a = mul( a, b, s[i] );
            if( a == 'i' && b ) {
                ii.pb( i + 1 );
            }
        }
        a = '1';
        b = true;
        for( ll i = s.size() - 1; i >= 0; i -- ) {
            a = mul( s[i], b, a );
            if( a == 'k' && b ) {
                kk.pb( i );
            }
        }
        bool ans = false;
        for( ll i = 0; i < ii.size(); i ++ ) {
            a = '1';
            b = true;
            ll j = ii[i];
            for( ll k = (ll) kk.size() - 1; k >= 0; k -- ) {
                if( kk[k] <= ii[i] )
                    continue;
                while( j < kk[k] ) {
                    a = mul( a, b, s[j] );
                    j ++;
                }
                if( a == 'j' && b ) {
                    ans = true;
                    break;
                }
            }
            if( ans )
                break;
        }

        cout << "Case #" << t + 1 << ": " << ( ans ? "YES" : "NO" ) << endl;
    }
	return 0;
}

