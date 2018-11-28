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
int r( long long n )
{
	long long i = n , j = 0 ;
	while ( i )
	{
		j = j * 10 + i % 10 ;
		i /= 10 ;
	}
	if ( j == n )
	{
		return 1 ;
	}
	return 0 ;
}
int main ()
{
	int t = in() , Case = 1 , res ;
	long long A , B , C ;
	while ( t -- )
	{
		res = 0 ;
		cin >> A >> B ;
		C = sqrt( double( A ) ) ;
		B = sqrt( double( B ) ) ;
		if ( A == C * C )
		{
			if ( r( A ) && r( C ) )
			{
				res ++ ;
				//cout << A << endl ;
			}
		}
		for ( long long i = C + 1 , j ; i <= B ; i ++ )
		{
			if ( r( i * i ) && r( i ) )
			{
				res ++ ;
				//cout << i * i << endl ;
			}
		}
		printf( "Case #%d: %d\n" , Case ++ , res ) ;
	}
}


