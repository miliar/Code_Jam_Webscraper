/*-----------------------------------------*/
//Author      : Mir Riyanul Islam (Riyan)  
//University  : AIUB                     
//E-mail      : mir_riyan@yahoo.com        
//Problem ID  : A                       
//Problem Name:                           
//Algorithm   :                         
/*-----------------------------------------*/
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")
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

using namespace std;

const double EPS = 1e-11;
const int INF = ( 1<<29 );
const double PI = 2 * acos( 0.0 );

int MAX( int a, int b ) { return a > b ? a : b;  }
int MIN( int a, int b ) { return a < b ? a : b;  }
void SWAP( int &a, int &b ) { int t = a; a = b; b = t; }
int GCD( int a, int b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }

int main() {
	freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "A-small-attempt1.out", "w", stdout );
	int i , T, cn = 0;
	int r, t, currRad;
	scanf( "%d", &T );
	while( T-- ) {
		currRad = 0;
		scanf( "%d %d", &r, &t );
		for( i = 1 ; ; i++ ) {
			currRad += ( 2 * r ) + ( 4 * i - 3 );
			if( t - currRad < 0 ) break;
			else if( t == currRad ) {
				i++;
				break;
			}
		}
		printf( "Case #%d: %d\n", ++cn , i - 1 );
	}
	return 0;
}

