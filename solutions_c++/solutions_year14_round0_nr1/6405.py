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
int main()
{
	int t = in() , Case = 1 ;
	while ( t -- )
	{
		int r = in() ;
		int a[ 17 ] = {} ;
		for ( int i = 1 , j ; i <= 4 ; i ++ )
		{
			if ( i == r )
			{
				a[ in() ] ++ ;
				a[ in() ] ++ ;
				a[ in() ] ++ ;
				a[ in() ] ++ ;
			}
			else
			{
				in() , in() , in() , in() ;
			}
		}
		r = in() ;
		for ( int i = 1 ; i <= 4 ; i ++ )
		{
			if ( i == r )
			{
				a[ in() ] ++ ;
				a[ in() ] ++ ;
				a[ in() ] ++ ;
				a[ in() ] ++ ;
			}
			else
			{
				in() , in() , in() , in() ;
			}
		}
		int res = 0 , res2 ;
		for ( int i = 1 ; i <= 16 ; i ++ )
		{
			if ( a[ i ] == 2 )
			{
				res ++ ;
				res2 = i ;
			}
		}
		if ( res == 1 )
		{
			printf( "Case #%d: %d\n" , Case ++ , res2 ) ;
		}else
		if ( res >= 2 )
		{
			printf( "Case #%d: Bad magician!\n" , Case ++ ) ;
		}
		else
		{
			printf( "Case #%d: Volunteer cheated!\n" , Case ++ ) ;
		}
	}
}


