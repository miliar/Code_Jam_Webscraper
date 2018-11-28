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
	int a[ 10000 ] ;
	while ( t -- )
	{
		int n = in() , x = in() ;
		for ( int i = 0 ; i < n ; i ++ )
		{
			a[ i ] = in() ;
		}
		sort( a , a + n ) ;
		int sum = 0 ;
		for ( int i = 0 , j = n - 1 ; i <= j ;  )
		{
			if ( a[ i ] + a[ j ] > x )
			{
				j -- ;
				sum ++ ;
			}
			else
			{
				i ++ ;
				j -- ;
				sum ++ ;
			}
		}
		printf( "Case #%d: %d\n" , Case ++ , sum ) ;
	}
}


