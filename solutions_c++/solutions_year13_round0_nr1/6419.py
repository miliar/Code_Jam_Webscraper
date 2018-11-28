#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#define phb push_back
#define ppb pop_back
using namespace std ;
inline int in(int d=0,char q=0,int c=1){while(q!='-'&&q!=EOF&&(q<48||q>57))q=getchar();if(q==EOF)return EOF;if(q=='-')c=-1,q=getchar();do d=d*10+(q^48),q=getchar();while(q<58&&q>47);return c*d;}
int main ()
{
	string s[ 4 ] ;
	int t = in() , Case = 1 ;
	while ( t -- )
	{
		int r[ 4 ][ 2 ] = {} , c[ 4 ][ 2 ] = {} , d[ 7 ][ 2 ][ 2 ] = {} , sum = 0 , tt = 0 ;
		for ( int i = 0 ; i < 4 ; i ++ )
		{
			cin >> s[ i ] ;
			for ( int j = 0 ; j < s[ i ] . size() ; j ++ )
			{
				if ( s[ i ][ j ] == 'X' )
				{
					r[ i ][ 0 ] ++ ;
					c[ j ][ 0 ] ++ ;
					d[ i + j ][ 0 ][ 0 ] ++ ;
					d[ i - j + 3 ][ 1 ][ 0 ] ++ ;
				}else
				if ( s[ i ][ j ] == 'O' )
				{
					r[ i ][ 1 ] ++ ;
					c[ j ][ 1 ] ++ ;
					d[ i + j ][ 0 ][ 1 ] ++ ;
					d[ i - j + 3 ][ 1 ][ 1 ] ++ ;
				}else
				if ( s[ i ][ j ] == 'T' )
				{
					tt ++ ;
					r[ i ][ 0 ] ++ ;
					c[ j ][ 0 ] ++ ;
					d[ i + j ][ 0 ][ 0 ] ++ ;
					d[ i - j + 3 ][ 1 ][ 0 ] ++ ;
					r[ i ][ 1 ] ++ ;
					c[ j ][ 1 ] ++ ;
					d[ i + j ][ 0 ][ 1 ] ++ ;
					d[ i - j + 3 ][ 1 ][ 1 ] ++ ;
				}
			}
			sum += r[ i ][ 0 ] + r[ i ][ 1 ] ;
		}
		bool Xwin = false , Owin = false ;
		for ( int i = 0 ; i < 4 ; i ++ )
		{
			if ( r[ i ][ 0 ] == 4 || c[ i ][ 0 ] == 4 )
			{
				Xwin = true ;
				//if ( r[ i ][ 0 ] == 4 ) printf( "r " ) ;
				//if ( c[ i ][ 0 ] == 4 ) printf( "c " ) ;
				//printf( "%d X\n" , i ) ;
			}
			if ( r[ i ][ 1 ] == 4 || c[ i ][ 1 ] == 4 )
			{
				Owin = true ;
				//if ( r[ i ][ 1 ] == 4 ) printf( "r " ) ;
				//if ( c[ i ][ 1 ] == 4 ) printf( "c " ) ;
				//printf( "%d O\n" , i ) ;
			}
		}
		for ( int i = 0 ; i < 7 ; i ++ )
		{
			if ( d[ i ][ 0 ][ 0 ] == 4 || d[ i ][ 1 ][ 0 ] == 4 )
			{
				Xwin = true ;
				//if ( d[ i ][ 0 ][ 0 ] == 4 ) printf( "d0 " ) ;
				//if ( d[ i ][ 1 ][ 0 ] == 4 ) printf( "d1 " ) ;
				//printf( "%d X\n" , i ) ;
			}
			if ( d[ i ][ 0 ][ 1 ] == 4 || d[ i ][ 1 ][ 1 ] == 4 )
			{
				Owin = true ;
				//if ( d[ i ][ 0 ][ 1 ] == 4 ) printf( "d0 " ) ;
				//if ( d[ i ][ 1 ][ 1 ] == 4 ) printf( "d1 " ) ;
				//printf( "%d O\n" , i ) ;
			}
		}
		if ( Xwin )
		{
			printf( "Case #%d: X won\n" , Case ++ ) ;
		}else
		if ( Owin )
		{
			printf( "Case #%d: O won\n" , Case ++ ) ;
		}else
		if ( sum - tt == 16 )
		{
			printf( "Case #%d: Draw\n" , Case ++ ) ;
		}
		else
		{
			printf( "Case #%d: Game has not completed\n" , Case ++ ) ;
		}
	}
}


