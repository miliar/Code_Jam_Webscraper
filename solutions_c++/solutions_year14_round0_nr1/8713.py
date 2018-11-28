#include<iostream>
#include<fstream>
#include<conio.h>
#include<cstdio>

using namespace std ;
ifstream inFile ;
ofstream outputFile ;

void main()
{
	int T, k1, k2, a[5][5], b[5][5], c, count, i, j, d=1 ;

	inFile.open ( "A-small-attempt1.in.txt", ios::in ) ;
	outputFile.open ( "output.txt", ios::out|ios::trunc ) ;

	inFile >> T ;

	while (T--)
	{
		inFile >> k1 ;
		for ( i=1; i<=4 ; i++ )
			for ( j=1 ; j<=4 ; j++ )
				inFile >> a[i][j] ;
		
		inFile >> k2 ;
		for ( i=1; i<=4 ; i++ )
			for ( j=1 ; j<=4 ; j++ )
				inFile >> b[i][j] ;
		
		count = 0 ;
		for ( i=1 ; i<=4 ; i++ )
			for ( j=1 ; j<=4 ; j++ )
				if ( a[k1][i] == b[k2][j] )
				{
					count++ ;
					c = a[k1][i] ;
				}

		outputFile.write ( "Case #", 6 ) ;
		outputFile << d++ ; 
		outputFile.write ( ": ", 2 ) ;
		if ( count == 1 )
			outputFile << c ;
		else if ( count == 0 )
			outputFile.write ( "Volunteer cheated!", 18 ) ;
		else
			outputFile.write ( "Bad Magician!", 13 ) ;
		outputFile.put ( '\n' ) ;
	}

	inFile.close() ;
	outputFile.close() ;
	_getch() ;
}