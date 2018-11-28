#include <iostream>
#include <sstream>
#include <bitset>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <numeric>
#include <list>
#define FOR(i,A) for(typeof (A).begin() i = (A).begin() ; i != (A).end() ; i++)
#define mp make_pair
#define debug( x ) cout << #x << " = " << x << endl
#define clr(v,x) memset( v, x , sizeof v )
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define f(i,a,b) for(int i = a ; i < b ; i++)
#define fd(i,a,b) for(int i = a ; i >= b ; i--)
#define TAM 10000001

using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef long double ld ;
typedef pair<int,ii> pii ;

int v[ TAM ] ;
int p = 0 , r = 0 ;

bool pal( ll x ){
	char a[ 10 ] ;
	sprintf( a , "%lld" , x ) ;
	int n = strlen( a ) ;
	f( i , 0 , n>>1 ) if( a[ i ] != a[ n - i - 1 ] ) return false ;
	return true ;
}

void pre(){
	p = 0 ;
	f( i , 1 , TAM ) if( pal( i ) ) v[ p++ ] = i ;
	r = 0 ;
	f( i , 0 , p ) if( pal( v[ i ] * v[ i ] ) ) v[ r++ ] = v[ i ] * v[ i ] ;
}

int main(){

	pre() ;
	int test , a , b ;
	scanf("%d" , &test ) ;
	f( k , 1 , test + 1 ){
		scanf("%d%d" , &a , &b ) ;
		int ini = lower_bound( v , v + r , a ) - v ;
		int fin = upper_bound( v , v + r , b ) - v ;
		printf("Case #%d: %d\n" , k , fin - ini ) ;
	}

    return 0 ;
}

