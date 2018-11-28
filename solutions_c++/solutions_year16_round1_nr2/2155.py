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
		srand( time( NULL ) );
		freopen( "B-large.in", "r", stdin ); freopen( "B-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

ll n;
ll a[111][55];
ll I[111];
bool u[111];
ll w[55];
ll h[55];

bool comp( ll i, ll j ) {
	return a[i][0] < a[j][0];
}

ll check() {
	ll res = 0;
	forn( i, n ) {
		forn( j, n ) {
			if( h[i] == 2 * n - 1 || w[j] == 2 * n - 1 )
				continue;
			if( a[h[i]][j] != a[w[j]][i] ) {
				res ++;
			}
		}
	}
	return res;
}

int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		cin >> n;
		forn( i, 2 * n - 1 ) {
			forn( j, n ) {
				cin >> a[i][j];
			}
			I[i] = i;
			u[i] = false;
		}
		sort( I, I + 2 * n - 1, comp );
		h[0] = I[0];
		u[I[0]] = true;
		u[2 * n - 1] = false;
		forn( i, n ) {
			bool ok = true;
			forn( j, 2 * n - 1 ) {
				if( u[I[j]] )
					continue;
				if( a[h[0]][i] == a[I[j]][0] ) {
					w[i] = I[j];
					u[I[j]] = true;
					ok = false;
					break;
				}
			}
			if( ok ) {
				w[i] = 2 * n - 1;
				u[2 * n - 1] = true;
				a[2 * n - 1][0] = a[h[0]][i];
				for( ll i = 1; i < n; i ++ ) {
					a[2 * n - 1][i] = 0;
				}
			}
		}
		for( ll i = 1; i < n; i ++ ) {
			bool ok = true;
			forn( j, 2 * n - 1 ) {
				if( u[I[j]] )
					continue;
				if( u[2 * n - 1] || a[w[0]][i] == a[I[j]][0] ) {
					h[i] = I[j];
					u[I[j]] = true;
					ok = false;
					break;
				}
			}
			if( ok ) {
				h[i] = 2 * n - 1;
				u[2 * n - 1] = true;
				a[2 * n - 1][0] = a[w[0]][i];
				for( ll i = 1; i < n; i ++ ) {
					a[2 * n - 1][i] = 0;
				}
			}
		}
		vector< pair< ll, ll > > v;
		for( ll i = 1; i < n; i ++ ) {
			for( ll j = 1; j < n; j ++ ) {
				if( a[h[i]][0] == a[w[j]][0] ) {
					v.pb( mp( i, j ) );
				}
			}
		}
		/*if( t + 1 <= 9 )
			continue;
		forn( i, n ) {
			forn( j, n ) {
				cout << a[h[i]][j] << " ";
			}
			cout << endl;
		}
		forn( i, n ) {
			forn( j, n ) {
				cout << a[w[j]][i] << " ";
			}
			cout << endl;
		}
		cout << check() << endl;*/
		ll k = 0;
		while( check() ) {
			ll res = check();
			if( k == 0 ) {
				forn( i, v.size() ) {
					ll res1 = check();
					swap( h[v[i].X], w[v[i].Y] );
					ll res2 = check();
					if( res1 < res2 )
						swap( h[v[i].X], w[v[i].Y] );
				}
			} else if( k == 1 ) {
				forn( i, v.size() ) {
					ll res1 = check();
					swap( h[v[i].X], w[v[i].Y] );
					ll res2 = check();
					if( res1 <= res2 )
						swap( h[v[i].X], w[v[i].Y] );
				}
			} else if( k == 2 ) {
				ll res = 0;
				ll idx = -1;
				forn( i, v.size() ) {
					ll res1 = check();
					swap( h[v[i].X], w[v[i].Y] );
					ll res2 = check();
					if( res < res1 - res2 ) {
						res = res1 - res2;
						idx = i;
					}
					swap( h[v[i].X], w[v[i].Y] );
				}
				if( idx != -1 )
					swap( h[v[idx].X], w[v[idx].Y] );
			} else if( k == 3 ) {
				forn( i, v.size() ) {
					if( rand()%2 )
						swap( h[v[i].X], w[v[i].Y] );
				}
				k = 0;
			}
			if( res == check() ) {
				k = ( k + 1 ) % 4;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		forn( i, n ) {
			if( h[i] != n * 2 - 1 )
				continue;
			forn( j, n ) {
				cout << a[w[j]][i] << " ";
			}
		}
		forn( i, n ) {
			if( w[i] != n * 2 - 1 )
				continue;
			forn( j, n ) {
				cout << a[h[j]][i] << " ";
			}
		}
		cout << endl;
	}
	return 0;
}
