#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <string>
#include <vector>
using namespace std;

const int MAXN = 200 + 10 ;
const int MAXPT = 200 + 5000 + 100 ;
const int MAXM = 2 * ( 200 + 5000 ) ;
const int Zy = 2000000000 ;

int first[ MAXPT ] , last[ MAXM ] , y[ MAXM ] , pow[ MAXM ] ;
int dist[ MAXPT ] , que[ MAXPT ] ;
int edg[ MAXM ] ;
int n , m , f , tot , test , ans , s , t , tt , word_len ;
map<string,int> word_map ;
vector<string> sentence[ MAXN ] ;

void Add( int a , int b , int c )
{
	y[ ++ tot ] = b ; pow[ tot ] = c ;
	last[ tot ] = first[ a ] ; first[ a ] = tot ;
}

void Updata( int a , int b , int c )
{
	// cout << "Updata: " << a << ' ' << b << endl;
	Add( a , b , c ) ;
	Add( b , a , c ) ;
}

void Init() {
	tot = -1 ; 
	memset( first , 255 , sizeof( first ) ) ; // 注意初值为 -1 // 各种读入各种连边
	word_len = 0 ;
	word_map.clear() ;

	cin >> n ;
	string line ; getline( cin , line ) ;
	for ( int x = 0 ; x < n ; x ++ ) {
		sentence[ x ].clear() ;
		getline( cin , line ) ;
		line = line + " " ;
		string ss ;
		for ( int i = 0 ; i < line.length() ; i ++ ) {
			if ( line[ i ] == ' ' ) {
				if ( word_map.count( ss ) == 0 )
					word_map[ ss ] = word_len ++ ;
				Updata( x , n + word_map[ ss ] , 1 ) ;
				sentence[ x ].push_back( ss ) ;
				ss = "" ;
			} else 
				ss = ss + line[ i ] ;
		}
	}
	// for ( int i = 0 ; i < n ; i ++ ) pow[ i ] = Zy ;
	// for ( int i = 0 ; i < word_len ; i ++ ) pow[ n + i ] = 1 ;
	s = 0 ; t = 1 ; // s 为源点 int Bfs() // 给所有点更新 dist 值
}

int BFS() {
	int l = 0 , r = 1 ; que[ 1 ] = s ;
	memset( dist , 255 , sizeof( dist ) ) ; dist[ s ] = 0 ;
	while ( r != l )
		for ( int p = first[ que[ ++ l ] ] ; p != -1 ; p = last[ p ] )
			if ( pow[ p ] > 0 && dist[ y[ p ] ] == -1 )
			{
				dist[ y[ p ] ] = dist[ que[ l ] ] + 1 ;
				que[ ++ r ] = y[ p ] ;
			}
	if ( dist[ t ] == -1 ) return 0 ;
	return 1 ;
}

int FindPath( int pt , int mi ) {
    if ( pt == t ) return mi ;
    int cici = 0 ;
    for ( int p = first[ pt ] ; p != -1 && mi > 0 ; p = last[ p ] )
        if ( pow[ p ] && dist[ y[ p ] ] == dist[ pt ] + 1 )
        {
            int tmp = FindPath( y[ p ] , min( mi , pow[ p ] ) ) ;
            cici += tmp ; mi -= tmp ;
            pow[ p ] -= tmp ; pow[ p ^ 1 ] += tmp ;
        }
    dist[ pt ] = -1 ;
    return cici ;
}

int cnt = 0 ;
int stk[ MAXN ] ;
void dfs( int deep ) {
	if ( deep >= n ) {
		word_map.clear() ;
		int sum = 0 ;
		for ( int i = 0 ; i < n ; i ++ )
			if ( stk[ i ] == 0 )
				for ( int j = 0 ; j < sentence[ i ].size() ; j ++ )
					word_map[ sentence[ i ] [ j ] ] = 1 ;
		for ( int i = 0 ; i < n ; i ++ )
			if ( stk[ i ] == 1 )
				for ( int j = 0 ; j < sentence[ i ].size() ; j ++ )
					if ( word_map[ sentence[ i ] [ j ] ] == 1 ) {
						sum ++ ;
						word_map[ sentence[ i ] [ j ] ] = 2 ;
					}
		if ( ans == -1 || sum < ans )
			ans = sum ;
		return ;
	}
	stk[ deep ] = 0 ; dfs( deep + 1 ) ;
	stk[ deep ] = 1 ; dfs( deep + 1 ) ;
}

int main() {
	freopen( "C-small-attempt1.in" , "r" , stdin ) ;
	// freopen( "c.in" , "r" , stdin ) ;
	freopen( "C-small-attempt1.out" , "w" , stdout ) ;
	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		Init() ;
		ans = 0 ;
		while ( BFS() ) ans += FindPath( s , Zy ) ;
		// stk[ 0 ] = 0 ;
		// stk[ 1 ] = 1 ;
		// dfs( 2 ) ;
		printf( "Case #%d: %d\n" , t , ans ) ;
	}
}
