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
		double C , F , X , res , nC = 2.0 , nT = 0.0 ;
		cin >> C >> F >> X ;
		res = X / nC ;
		while ( nT < res )
		{
			nT += C / nC ;
			nC += F ;
			if ( res > nT + X / nC )
			{
				res = nT + X / nC ;
			}
		}
		printf( "Case #%d: %.7lf\n" , Case ++ , res ) ;
	}
}


