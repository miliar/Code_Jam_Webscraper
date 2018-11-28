
/*-------------------------------------------*/
//Author      : Mir Riyanul Islam (Riyan)  
//University  : AIUB                       
//E-mail      : mir_riyan@yahoo.com        
//Problem ID  : C                     
//Problem Name: Fair and Square
//Algorithm   : 
/*-------------------------------------------*/
#pragma comment( linker , "/STACK:16777216" )
#pragma warning( disable : 4786 )
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

//#define deBug
#define inOut

#define MS 111
#define pnl puts( "" )
#define psp cout << " "
#define prnt( a ) cout << a
#define phl cout << "Hello World!!!"
#define prntln( a ) cout << a << endl
#define prntD( a ) printf( "%.3lf" , a )

using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-11;
const double PI = 2 * acos( 0.0 );

int MAX( int a , int b ) { return a > b ? a : b;  }
int MIN( int a , int b ) { return a < b ? a : b;  }
void SWAP( int &a , int &b ) { int t = a; a = b; b = t; }
int GCD( int a , int b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }

int n , m , l , r;
int linear[MS] , given[MS][MS] , upd[MS][MS] , lst[MS][MS] , check[MS][MS];

void init() {
	int i , j;
	memset( check , 0 , sizeof( check ) );
	for( i = 0 ; i < n ; i++ ) {
		for( j = 0 ; j < m ; j++ ) {
			upd[i][j] = linear[l-1];
			lst[i][j] = upd[i][j];
		}
	}
}

void updateCheck() {
	int i , j;
	r = 0;
	for( i = 0 ; i < n ; i++ ) {
		for( j = 0 ; j < m ; j++ ) {
			if( upd[i][j] == given[i][j] ) check[i][j] = 1 , r++;
		}
	}
}

bool cutGrass( int h ) {
	int i , j;
	//top2bottom
	for( i = 0 ; i < m ; i++ ) {
		for( j = 0 ; j < n ; j++ ) {
			if( h < given[j][i] ) {
				for( j-- ; j >= 0 ; j-- ) {
					upd[j][i] = lst[j][i];
				}
				break;
			}
			else {
				lst[j][i] = upd[j][i];
				upd[j][i] = h;
			}
		}
		if( j == n ) {
			for( j = 0 ; j < n ; j++ ) {
				lst[j][i] = upd[j][i];
				if( upd[j][i] == given[j][i] ) check[j][i] = 1;
			}
		}
	}
	updateCheck();
	if( r == n * m ) return true;
	//right2left
	for( i = 0 ; i < n ; i++ ) {
		for( j = m - 1 ; j >= 0 ; j-- ) {
			if( h < given[i][j] ) {
				for( j++ ; j < m ; j++ ) {
					upd[i][j] = lst[i][j];
				}
				break;
			}
			else {
				lst[i][j] = upd[i][j];
				upd[i][j] = h;
			}
		}
		if( j == -1 ) {
			for( j = m - 1 ; j >= 0 ; j-- ) {
				lst[i][j] = upd[i][j];
				if( upd[i][j] == given[i][j] ) check[i][j] = 1;
			}
		}
	}
	updateCheck();
	if( r == n * m ) return true;
	//bottom2up
	for( i = 0 ; i < m ; i++ ) {
		for( j = n - 1 ; j >= 0 ; j-- ) {
			if( h < given[j][i] ) {
				for( j++ ; j < n ; j++ ) {
					upd[j][i] = lst[j][i];
				}
				break;
			}
			else {
				lst[j][i] = upd[j][i];
				upd[j][i] = h;
			}
		}
		if( j == -1 ) {
			for( j = n - 1 ; j >= 0 ; j-- ) {
				lst[j][i] = upd[j][i];
				if( upd[j][i] == given[j][i] ) check[j][i] = 1;
			}
		}
	}
	updateCheck();
	if( r == n * m ) return true;
	//left2right
	for( i = 0 ; i < n ; i++ ) {
		for( j = 0 ; j < m ; j++ ) {
			if( h < given[i][j] ) {
				for( j-- ; j >= 0 ; j-- ) {
					upd[i][j] = lst[i][j];
				}
				break;
			}
			else {
				lst[i][j] = upd[i][j];
				upd[i][j] = h;
			}
		}
		if( j == m ) {
			for( j = 0 ; j < m ; j++ ) {
				lst[i][j] = upd[i][j];
				if( upd[i][j] == given[i][j] ) check[i][j] = 1;
			}
		}
	}
	updateCheck();
	if( r == n * m ) return true;
	return false;
}

int main() {

#ifdef inOut
	freopen( "B-large.in" , "r" , stdin );
	freopen( "B-large.out" , "w" , stdout );
#endif

	bool flag;
	map < int , int > mp;
	int tc , cn = 0 , i , j , k , mid;
	scanf( "%d" , &tc );
	while( tc-- ) {
		flag = false;
		scanf( "%d %d" , &n , &m );
		for( i = 0 , mid = 0 , k = 0 ; i < n ; i++ ) {
			for( j = 0 ; j < m ; j++ ) {
				scanf( "%d" , &given[i][j] );
				if( mp.find( given[i][j] ) == mp.end() ) {
					linear[k] = given[i][j];
					mp[given[i][j]] = mid;
					mid++;
					k++;
				}
			}
		}
		l = k;
		sort( linear , linear + l );

#ifdef deBug
		for( i = 0 ; i < l ; i++ ) {
			prnt( linear[i] );
			psp;
		}
		pnl;
#endif
		init();
		updateCheck();
		if( r == n * m ) flag = true;
		for( i = l - 2 ; i >= 0 && !flag ; i-- ) {
			flag = cutGrass( linear[i] );
		}
		printf( "Case #%d: " , ++cn );
		if( flag ) prntln( "YES" );
		else prntln( "NO" );
		mp.clear();
	}

	return 0;

}

