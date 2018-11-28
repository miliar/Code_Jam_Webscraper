#include <bits/stdc++.h>
using namespace std;

#define sc( x ) scanf( "%d" , &x )
#define REP( i , n ) for( int i = 0 ; i < n ; i++ )
#define FOR( it , A ) for( typeof A.begin() it = A.begin() ; it != A.end() ; it++ )
#define clr( t , val ) memset( t , val , sizeof(t) )

#define all(v)  v.begin() , v.end()
#define rall(v)  v.rbegin() , v.rend()
#define pb push_back

#define mp make_pair
#define fi first
#define se second

#define ones(x) __builtin_popcount(x)
#define test puts("************test************");
#define sync ios_base::sync_with_stdio(false);

#define N 100005
#define MOD 1000000007
#define INF (1<<30)
#define EPS (1e-5)

typedef long long ll;
typedef unsigned long long ull;
typedef pair< int , int > pii;
typedef pair< ll , ll > pll;
typedef vector< int > vi;
typedef vector< vi > vvi;
typedef vector< ll > vll;
typedef vector< ull > vull;

int n = 4;
int a[ 20 ] , T[ 20 ];
int main(){
	int cases , r1 , r2 , x;
	sc( cases );
	REP( tc , cases ){
		clr( T , 0 );
		sc( r1 ) ; 
		r1 --;
		REP( i , n ) {
			REP( j , n ) sc( a[ j ] ) , a[ j ] --;
			if( i == r1 ){
				REP( j , n ) T[ a[ j ] ]++;
			}
		}
		sc( r2 );
		r2 --;
		REP( i , n ) {
			REP( j , n ) sc( a[ j ] ) , a[ j ] --;
			if( i == r2 ){
				REP( j , n ) T[ a[ j ] ]++;
			}
		}
		int cnt = 0 , ind;
		REP( i , 16 ) if( T[ i ] == 2 ) cnt ++ , ind = i;
		if( cnt == 1 ) printf( "Case #%d: %d\n" , tc + 1 , ind + 1 );
		else{
			if( cnt >= 2 ) printf( "Case #%d: Bad magician!\n" , tc + 1 );
			else printf( "Case #%d: Volunteer cheated!\n" , tc + 1 );
		}
	}
}


