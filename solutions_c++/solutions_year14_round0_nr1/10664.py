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
#define PI acos( -1.0 )
#define EPS 1E-9
#define TAM 17
 
 using namespace std;
  
typedef pair<int,int> ii ;
typedef long long ll ;
typedef long double ld ;
typedef pair<int,ii> pii ;

int mc[ TAM ] ;

void init(){
	clr( mc , 0 ) ;
}

void read(){
	int row , x ;
	scanf("%d" , &row ) ;
	f( i , 0 , 4 ) f( j , 0 , 4 ){
		scanf("%d" , &x ) ;
		if( i + 1 == row ) mc[ x ]++ ;
	}
}

int main(){

	int test , first , second , x , mx ;
	scanf("%d" , &test ) ;
	f( k , 1 , test+1 ){
		init() ;
		read() ;
		read() ;
		mx = 0 ;
//		f( i , 0 , TAM ) cout << mc[ i ] << ' ' ; cout << endl ;
		f( i , 0 , TAM ) mx = max( mx , mc[ i ] ) ;
		vector<int> g ;
		f( i , 1 , TAM ) if( mc[ i ] == mx ) g.push_back( i ) ;

		printf("Case #%d: " , k ) ;
		if( g.size() == 1 ){
			printf("%d\n" , g[ 0 ] ) ;
			continue ;
		}
		if( mx == 1 ){
			printf("Volunteer cheated!\n" ) ;
			continue ;
		}
		printf("Bad magician!\n" ) ;
	}
	return 0 ;
}
