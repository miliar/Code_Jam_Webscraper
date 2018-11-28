#include <cstdio>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <cstring>
#include <string>
#include <utility>

using namespace std ;


int grass[101][101] ;

bool Pos(int i, int j)
{
	bool l = true, c = true ;

	for(int k = j ; k < 101 ; ++k)
	{
		if( grass[i][k] > grass[i][j] )
		{
			l = false ;
			break ;
		}
	}

	for(int k = j ; k >= 0 ; --k)
	{
		if( grass[i][k] > grass[i][j] )
		{
			l = false ;
			break ;
		}
	}

	for(int k = i ; k < 101 ; ++k)
	{
		if( grass[k][j] > grass[i][j] )
		{
			c = false ;
			break ;
		}
	}

	for(int k = i ; k >= 0 ; --k)
	{
		if( grass[k][j] > grass[i][j] )
		{
			c = false ;
			break ;
		}
	}

	return c || l ;
}


int main(void)
{
	int T, cases = 1 ;

	scanf("%d", &T) ;
	while( T-- )
	{
		int N, M ;
		bool p = true ;

		for(int i = 0 ; i < 101 ; ++i)
		{
			memset(grass[i], 0, sizeof(int) * 101) ;
		}

		scanf("%d%d", &N, &M) ;

		for(int i = 0 ; i < N ; ++i)
		{
			for(int j = 0 ; j < M ; ++j)
			{
				scanf("%d", &grass[i][j]) ;
			}
		}
		
		for(int i = 0 ; i < N ; ++i)
		{
			for(int j = 0 ; j < M ; ++j)
			{
				if( ! Pos(i, j) )
				{
					p = false ;
				}
			}
		}

		if( p )
		{
			printf("Case #%d: YES\n", cases++) ;
		}
		else
		{
			printf("Case #%d: NO\n", cases++) ;
		}
		
/*		for(int i = 0 ; i < N ; ++i)
		{
			for(int j = 0 ; j < M ; ++j)
			{
				printf("%d", grass[i][j]) ;
			}
			printf("\n") ;
		} // */
	}

	return 0 ;
}



