/*
  by asas
*/
#include <bits/stdc++.h>
#define CASET int ___T, Case = 1; scanf("%d ", &___T); while (___T-- > 0)
#define SZ(X) ((int)(X).size())
#define PHB push_back
#define PPB pop_back
#define LL long long
#define ULL unsigned long long
#define ALL(X) (X).begin(), (X).end()
#define MP make_pair
#define PII pair<int,int>
#define VPII vector<pair<int,int>>
#define PLL pair<long long,long long>
#define F first
#define S second
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define DRI(X) int (X) = in()
#define DRII(X, Y) int X = in() , Y = in()
#define DRIII(X, Y, Z) int X = in() , Y = in() , Z = in()
using namespace std ;
const int MOD = 1e9+7;
const int SIZE = 1e5+10;
inline int in(int d=0,char q=0,int c=1){while(q!='-'&&q!=EOF&&(q<48||q>57))q=getchar();if(q==EOF)return EOF;if(q=='-')c=-1,q=getchar();do d=d*10+(q^48),q=getchar();while(q<58&&q>47);return c*d;}
// template end here
int main()
{
	CASET
	{
		DRI( n ) ;
		if ( !n )
		{
			printf( "Case #%d: INSOMNIA\n" , Case ++ ) ;
		}
		else
		{
			unsigned int check = ( 1 << 10 ) - 1 , j , k ;
			int res ;
			for ( int i = 1 ; check ; i ++ )
			{
				j = res = i * n ;
				while ( j )
				{
					k = j % 10 ;
					check = check & ( ~( 1 << k ) ) ;
					j /= 10 ;
				}
			}
			printf( "Case #%d: %d\n" , Case ++ , res ) ;
		}
	}
	return 0 ;
}

