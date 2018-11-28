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

#define N 1000000
#define MOD 1000000007
#define INF (1<<30)
#define EPS (1e-5)

typedef long long ll;
typedef unsigned long long ull;
typedef pair< int , int > pii;
typedef vector< char > vc;
typedef vector< vc > vvc;
typedef vector< int > vi;
typedef vector< vi > vvi;

int R , C , M , spaces;
int dx[] = { 0 , 0 , 1 , -1 , 1 , 1 , -1 , -1 };
int dy[] = { 1 , -1 , 0 , 0 , 1 , -1 , 1 , -1 };
vvc MAT;
void impr(){
	REP( i , R ) {
		REP( j , C ) printf( "%c" , MAT[ i ][ j ] );
		puts( "" );
	}
}
bool valid( int x , int y ){ return x >= 0 && x < y ; }
bool isSolution(){
	vvi forb = vvi( R , vi( C , 0 ) );
	REP( i , R ) REP( j , C ){
		if( MAT[ i ][ j ] == '*' ){
			REP( k , 8 ){
				int ni = i + dx[ k ] , nj = j + dy[ k ];
				if( valid( ni , R ) && valid( nj , C ) && MAT[ ni ][ nj ] == '.' ) forb[ ni ][ nj ] = 1;
			}
		}
	}
	vvi vis = vvi( R , vi( C , 0 ) );
	int ncomp = 0;
	REP( i , R ) REP( j , C )
		if( !forb[ i ][ j ] && MAT[ i ][ j ] == '.' && !vis[ i ][ j ] ){
			ncomp ++;
			queue< pair< int , int > > Q;
			vis[ i ][ j ] = 1;
			Q.push( mp( i , j ) );
			while( !Q.empty() ){
				pii p = Q.front() ; Q.pop();
				int x = p.fi , y = p.se;
				REP( k , 8 ){
					int nx = x + dx[ k ] , ny = y + dy[ k ];
					if( valid( nx , R ) && valid( ny , C ) && !forb[ nx ][ ny ] && MAT[ nx ][ ny ] == '.'
						&& !vis[ nx ][ ny ] ){
						vis[ nx ][ ny ] = 1;
						Q.push( mp( nx , ny ) );
					}
				}
			}
		}
	
	
	int a , b;
	REP( i , R ) REP( j , C ) 
		if( MAT[ i ][ j ] == '.' && !forb[ i ][ j ] ){
			REP( k , 8 ){
				int ni = i + dx[ k ] , nj = j + dy[ k ];
				if( valid( ni , R ) && valid( nj , C ) && forb[ ni ][ nj ] ) forb[ ni ][ nj ] = 2;
			}
			a = i , b = j;
		}
	REP( i , R ) REP( j , C ) if( forb[ i ][ j ] == 2 ) forb[ i ][ j ] = 0;
	//MAT[ 0 ][ 0 ] = 'c'; when return 1
	
	int sum = 0;
	REP( i , R ) REP( j , C ) sum += forb[ i ][ j ];
	
	if( sum == 0 && ncomp == 1 ) {
		MAT[ a ][ b ] = 'c';
		return 1;
	}
	return 0;
}
void doit(){
	if( spaces == 1 ){
		MAT = vvc( R , vc( C , '*' ) );
		MAT[ 0 ][ 0 ] = 'c';
		impr();
		return;
	}
	MAT = vvc( R , vc( C , '*' ) );
	string cad = string( M , '*' ) + string( spaces , '.' );
	do{
		REP( i , R*C ) MAT[ i / C ][ i % C ] = cad[ i ];
		if( isSolution() ){
			impr();
			return;
		}
	}while( next_permutation( all( cad ) ) );
	puts( "Impossible" );
}
void solve(){
	spaces = R * C - M;
	doit();
}
int main(){
	int cases;
	sc( cases );
	REP( tc , cases ){
		sc( R ) , sc( C ) , sc( M );
		printf( "Case #%d:\n" , tc + 1 );
		solve();
	}
}

