#include<iostream>
#include<fstream>
#include<conio.h>
#include<cstdio>
#include<iomanip>

using namespace std ;
ifstream inFile ;
ofstream outFile ;

void main()
{
	int T, tc=1 ;
	double C, F, X, a, b, d, e ;

	inFile.open ( "B-large.in.txt", ios::in ) ;
	outFile.open ( "output.txt", ios::out|ios::trunc ) ;

	inFile >> T ;

	while (T--)
	{
		inFile >> C ;
		inFile >> F ;
		inFile >> X ;


		d = X/2.0 ;
		b = 0.0 ;
		e = 2.0 ;

		do
		{
			a = d ;
			b += (C/e) ;
			e += F ;
			d = b + (X/e) ;
		} while ( d <= a ) ;

		outFile.write ( "Case #", 6 ) ;
		outFile << tc++ ;
		outFile.write ( ": ", 2 ) ;
		outFile << setprecision(10) << a ;
		outFile.put ( '\n' ) ;
	}

	inFile.close() ;
	outFile.close() ;
	_getch() ;
}