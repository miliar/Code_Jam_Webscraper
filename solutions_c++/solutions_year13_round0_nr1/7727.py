#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
/*char Check(char str[4][4])
{
	
}*/
char Check(float mat[4][4])
{
	float d = mat[0][0] + mat[1][1] + mat[2][2] + mat[3][3] , c = mat[0][3] + mat[1][2] + mat[2][1] + mat[3][0] ;

	float s = 0 ;
	for( int i = 0 ; i < 4 ; i ++ )
	{
		for( int j = 0 ; j < 4 ; j ++ )
		{
			s += mat[i][j];
		}
		if(fmod(s,5) == 0)
		{
			return 'X';
		}
		else if( fmod(s,7) == 0 )
		{
			return 'O' ;
		}
		s = 0;
	}
	s = 0 ;
	for(int j = 0 ; j < 4 ; j ++ )
	{
		for( int i = 0 ; i < 4 ; i ++ )
		{
			s += mat[i][j];
		}
		if(fmod(s,5) == 0)
		{
			return 'X';
		}
		else if( fmod(s,7) == 0 )
		{
			return 'O' ;
		}
		s = 0 ;
	}
	if(fmod(d,5) == 0)
	{
		return 'X';
	}
	else if( fmod(d,7) == 0 )
	{
		return 'O' ;
	}
	if(fmod(c,5) == 0)
	{
		return 'X';
	}
		else if( fmod(c,7) == 0 )
		{
			return 'O' ;
		}
	return 'd' ;
}//iswinner
bool Read(float str[4][4])
{
	bool a = 0 ;
	char ch ;
	for (int i = 0; i < 4; i ++)
	{
		for (int j = 0; j < 4; j ++)
		{
			cin >> ch ;
			if( ch == 'X' )
				str[i][j] = 5 ;
			else if( ch == 'O' )
				str[i][j] = 7 ;
			else if( ch == 'T' )
				str[i][j] = 35 ;
			else
			{
				str[i][j] = 2.9 ;
				a = 1 ;
			}
		}
	}
	return a ;
}
int main()
{
	/*ifstream fin("A-small-attempt1.in", ios::in);
	ofstream fout("out.in", ios::trunc);*/
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	bool a = 0 ;
	char ch ;
	float str[4][4] ;
	int n = 0 , k = 1 ;
	cin >> n ;
	while( n -- )
	{
		a = 0 ;
		a = Read(str);
		ch = Check( str ) ;
		cout << "Case #" << k++ << ": " ;
		if( ch == 'd' && a == 1 )
			cout << "Game has not completed" << endl ;
		else if( ch == 'd' )
			cout << "Draw" << endl ;
		else
			cout << ch << " won"<< endl ; 
	}
	
	return 0;
}