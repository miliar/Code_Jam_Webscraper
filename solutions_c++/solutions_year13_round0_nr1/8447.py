
#include "cstdio"
#include "iostream"
#include "cstring"
using namespace std;

typedef long long ll ;

bool eq( char a , char b )
{
	if ( a == 'T' || b == 'T' ) return true ;
	if ( a == '.' || b == '.' ) return false ;
	return a == b ;
}

int main()
{
	int T , cas = 0;
	int flag ;
	int i , j ;
	char maze[10][10] ;
	scanf ( "%d" , &T ) ;
	while ( T -- )
	{
		flag = -1 ;
		for ( i = 0 ; i < 4 ; i ++ ) scanf ( "%s" , maze[i] ) ;
		//line
		for ( i = 0 ; i < 4 ; i ++ )
		{
			char s ;
			for ( j = 0 ; j < 4 ; j ++ )
				if ( maze[i][j] == '.' ){
					s = '.'; break ;
				}else if ( maze[i][j] == 'T' ) continue ;
				else 
				{
					s = maze[i][j] ; break ;
				}
			if ( s == '.' ) continue ;
			for ( j = 0 ; j < 4 ; j ++ )
			{
				if ( !eq(maze[i][j],s) ) break ;
			}
			if ( j == 4 )
			{
				if ( s == 'X' ) flag = 0 ;
				else if ( s == 'O' ) flag = 1 ;
				else while(true);
			}

		}
		//ro
		for ( j = 0 ; j < 4 ; j ++ )
		{
			char s ;
			for ( i = 0 ; i < 4 ; i ++ )
				if ( maze[i][j] == '.' ){
					s = '.';break ;
				}else if ( maze[i][j] == 'T' ) continue ;
				else {
					s= maze[i][j] ; break ;
				}
			if ( s == '.' ) break ;
			for ( i = 0 ; i < 4 ; i ++ )
			{
				if ( !eq(maze[i][j],s) ) break ;
			}
			if ( i == 4 )
			{
				if ( s == 'X' ) flag = 0 ;
				else if ( s == 'O' ) flag = 1 ;
				else while(true) ;
			}
		}
		//xie1
		char s ;
		for ( i = 0 ; i < 4 ; i ++ )
		{
			if ( maze[i][i] == '.' )
			{
				s = '.' ; break ;
			}else if ( maze[i][i] == 'T' ) continue ;
			else 
			{
				s = maze[i][i] ; break ;
			}
		}
		if ( s != '.' )
		{
			for ( i = 0 ; i < 4 ; i ++ )
			{
				if ( !eq(maze[i][i],s)) break;
			}
			if ( i == 4)
			{
				if ( s == 'X' ) flag = 0 ;
				else if ( s == 'O' ) flag = 1 ;
				else while(true) ;
			}
		}
		for ( i = 0 ; i < 4 ; i ++ )
		{
			if ( maze[i][3-i] == '.' )
			{
				s = '.';break;
			}else if ( maze[i][3-i] =='T' ) continue ;
			else 
			{
				s = maze[i][3-i] ; break ;
			}
		}
		if ( s != '.' )
		{
			for ( i = 0 ; i < 4; i++)
			{
				if ( !eq(maze[i][3-i],s) ) break ;
			}
			if ( i == 4 )
			{
				if ( s == 'X' ) flag = 0 ;
				else if ( s == 'O' ) flag = 1 ;
				else flag = -1 ;
			}
		}
		if ( flag == -1 )
		{
			for ( i = 0 ; i < 4 ; i ++ )
				for ( j = 0 ; j < 4 ; j ++ )
					if ( maze[i][j] == '.' ) flag = -2 ;
		}
		printf ( "Case #%d: " , ++cas ) ;
		if ( flag == -2 )
		{
			puts("Game has not completed") ;
		}
		else if ( flag == -1 )
		{
			puts("Draw") ;
		}else if ( flag == 0 )
		{
			puts("X won") ;
		}else puts("O won") ;
	}
	return 0 ;
}
