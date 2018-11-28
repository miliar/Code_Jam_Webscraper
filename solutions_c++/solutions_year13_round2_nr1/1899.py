//Templete 2013/04/14
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <cstring>
#include <cmath>
#include <map>
#include <stack>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#define INF 100000000
#define MAX 120
using namespace std ;
int n ;
int A , ans ;
int mote[ MAX ] , use[ MAX ] ;
void BK( int atk , int Now , int Cnt )
{
	if( Now == n )
	{
		ans = min( ans , Cnt ) ;
		return ;
	}
	
	if( ans < Cnt )
		return ;
	
	if( atk > mote[ Now ] )
	{
		BK( atk+mote[ Now ] , Now+1 , Cnt ) ;
	}
	else
	{
		BK( atk , Now+1 , Cnt+1 ) ;
		int j = 0 , i = atk ;
		while( i <= mote[ Now ] && i != 2*i-1 )
			i = 2*i-1 , j++ ;
		if( j != 0 )
			BK( i+mote[ Now ] , Now+1 , Cnt+j ) ;
	}
}
int main( )
{
	int t , T = 1 ;
	scanf( "%d" , &t ) ;
	while( t-- )
	{
		scanf( "%d%d" , &A , &n ) ;
		for( int i = 0 ; i < n ; i++ )
			scanf( "%d" , &mote[ i ] ) ;
		sort( mote , mote+n ) ;
		memset( use , 0 , sizeof( use ) ) ;
		ans = INF ;
		int cur , add , j ;
		BK( A , 0 , 0 ) ;
		printf( "Case #%d: %d\n" , T++ , ans ) ;
		
	}
	return 0 ;
}

