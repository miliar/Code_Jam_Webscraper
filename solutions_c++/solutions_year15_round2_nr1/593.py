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
		freopen( "A-large.in", "r", stdin );
		freopen( "A-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

ll a[1111111];
ll b[1111111];

ll revers( ll x ) {
    ll res = 0;
    while( x ) {
        res = res * 10 + x % 10;
        x /= 10;
    }
    return res;
}

ll solve( ll n ) {
    ll ans = 1;
    ll x = 1;
    ll y = 10;
    ll z = 10;
    while( y <= n ) {
        ans += z - 1 - x % z;
        x += z - 1 - x % z;
        if( x < revers( x ) ) {
            ans ++;
            x = revers( x );
            ans += z - 1 - x % z;
            x += z - 1 - x % z;
        }
        ans ++;
        x ++;
        y *= 10;
        if( z * z < y )
            z *= 10;
    }
    if( x == n )
        return ans;
    if( x / z != n / z ) {
        ll a;
        if( n % z == 0 )
            a = revers( n / z - 1 );
        else
            a = revers( n / z );
        ans += a - x % z;
        x += a - x % z;
        if( x < revers( x ) ) {
            ans ++;
            x = revers( x );
        }
    }
    ans += n - x;
    x += n - x;
    return ans;
}

int main( void ) {
    ll T;
    cin >> T;
    queue< ll > q;
    q.push( 1 );
    a[1] = 1;
    while( q.size() ) {
        ll x = q.front();
        q.pop();
        ll y = x + 1;
        ll z = revers( x );
        if( y <= 1000000 ) {
            if( a[y] == 0 ) {
                a[y] = a[x] + 1;
                q.push( y );
                b[y] = x;
            }
            if( a[y] > a[x] + 1 )
                a[y] = a[x] + 1, b[y] = x;
        }
        if( z <= 1000000 ) {
            if( a[z] == 0 ) {
                a[z] = a[x] + 1;
                q.push( z );
                b[z] = x;
            }
            if( a[z] > a[x] + 1 )
                a[z] = a[x] + 1, b[z] = x;
        }
    }

    forn( t, T ) {
        ll n;
        cin >> n;
        cout << "Case #" << t + 1 << ": " << solve( n ) << endl;
    }
	return 0;
}
