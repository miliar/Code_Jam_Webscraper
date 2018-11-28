#include <bits/stdc++.h>
using namespace std ;

struct Node {
	int x , y ;
	bool operator < ( const Node& a ) const {
		return x < a.x ;
	}
} ;

Node a[16 * 2] ;
int G[16] ;
int p[16 * 4] ;
int vis[16 * 4] ;
int n , m ;

int F ( int x ) {
	return p[x] == x ? x : ( p[x] = F ( p[x] ) ) ;
}

void solve () {
	scanf ( "%d%d" , &n , &m ) ;
	for ( int i = 0 ; i < n + m ; ++ i ) {
		scanf ( "%d%d" , &a[i].x , &a[i].y ) ;
		if ( a[i].x > a[i].y ) swap ( a[i].x , a[i].y ) ;
	}
	sort ( a , a + n + m ) ;
	int S = n * m ;
	for ( int s = 0 ; s < 1 << S ; ++ s ) {
		for ( int i = 0 ; i < S * 4 ; ++ i ) {
			p[i] = i ;
		}
		for ( int i = 0 ; i < n ; ++ i ) {
			for ( int j = 0 ; j < m ; ++ j ) {
				int idx = i * m + j ;
				if ( s & ( 1 << idx ) ) {
					p[F ( idx )] = F ( S + idx ) ;
					p[F ( 2 * S + idx )] = F ( 3 * S + idx ) ;
				} else {
					p[F ( idx )] = F ( 3 * S + idx ) ;
					p[F ( 2 * S + idx )] = F ( S + idx ) ;
				}
				if ( i < n - 1 ) p[F ( 2 * S + idx )] = F ( idx + m ) ;
				if ( j < m - 1 ) p[F ( S + idx )] = F ( 3 * S + idx + 1 ) ;
			}
		}
		for ( int i = 0 ; i < S * 4 ; ++ i ) {
			F ( i ) ;
		}
		vector < int > G[S * 4] ;
		vector < pair < int , int > > tmp ;
		for ( int i = 0 ; i < m ; ++ i ) {
			G[F ( i )].push_back ( i + 1 ) ;
		}
		for ( int i = 0 ; i < n ; ++ i ) {
			G[F ( S + i * m + m - 1 )].push_back ( m + i + 1 ) ;
		}
		for ( int i = m - 1 ; ~i ; -- i ) {
			G[F ( 2 * S + ( n - 1 ) * m + i )].push_back ( n + m + ( m - i ) ) ;
		}
		for ( int i = n - 1 ; ~i ; -- i ) {
			G[F ( 3 * S + i * m )].push_back ( n + m + m + ( n - i ) ) ;
		}
		for ( int i = 0 ; i < S * 4 ; ++ i ) {
			if ( G[i].size () >= 2 ) {
				int x = G[i][0] , y = G[i][1] ;
				if ( x > y ) swap ( x , y ) ;
				tmp.push_back ( make_pair ( x , y ) ) ;
			}
		}
		sort ( tmp.begin () , tmp.end () ) ;
		int ok = 1 ;
		for ( int i = 0 ; i < tmp.size () ; ++ i ) {
			if ( tmp[i].first != a[i].x || tmp[i].second != a[i].y ) {
				ok = 0 ;
				break ;
			}
		}
		if ( ok ) {
			for ( int i = 0 ; i < n ; ++ i ) {
				for ( int j = 0 ; j < m ; ++ j ) {
					int idx = i * m + j ;
					if ( s & ( 1 << idx ) ) {
						printf ( "\\" ) ;
					} else printf ( "/" ) ;
				}
				puts ( "" ) ;
			}
			return ;
		}
	}
	printf ( "IMPOSSIBLE\n" ) ;
}

int main () {
	int T ;
	freopen ( "C-small-attempt0.in" , "r" , stdin ) ;
	freopen ( "C-small-attempt0.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; ++ i ) {
		printf ( "Case #%d:\n" , i ) ;
		solve () ;
	}
	return 0 ;
}