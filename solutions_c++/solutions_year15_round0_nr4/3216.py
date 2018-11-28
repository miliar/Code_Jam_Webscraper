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
		int x = in() , r = in() , c = in() ;
		if ( r < c ) swap( r , c ) ;
		if ( x > 4 ) printf( "Case #%d: RICHARD\n" , Case ++ ) ;
		if ( x == 1 ) printf( "Case #%d: GABRIEL\n" , Case ++ ) ;
		if ( x == 2 )
		{
			if ( ( r * c ) % 2 == 1 ) printf( "Case #%d: RICHARD\n" , Case ++ ) ;
			else printf( "Case #%d: GABRIEL\n" , Case ++ ) ;
		}
		if ( x == 3 )
		{
			if ( ( r * c ) % 3 == 0 )
			{
				if ( r == 3 && c == 1 )
				{
					printf( "Case #%d: RICHARD\n" , Case ++ ) ;
				}
				else
				{
					printf( "Case #%d: GABRIEL\n" , Case ++ ) ;
				}
			}
			else printf( "Case #%d: RICHARD\n" , Case ++ ) ;
		}
		if ( x == 4 )
		{
			if ( ( r * c ) % 4 == 0 )
			{
				if ( r == 2 && c == 2 ||
					 r == 4 && c == 1 ||
					 r == 4 && c == 2 )
				{
					printf( "Case #%d: RICHARD\n" , Case ++ ) ;
				}
				else
				{
					printf( "Case #%d: GABRIEL\n" , Case ++ ) ;
				}
			}
			else printf( "Case #%d: RICHARD\n" , Case ++ ) ;
		}
	}
}


