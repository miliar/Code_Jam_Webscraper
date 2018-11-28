// google.cpp : Defines the entry point for the console application.
//

// #include "stdafx.h"

// #include "targetver.h"

#include <stdio.h>
// #include <tchar.h>



// TODO: reference additional headers your program requires here
#include <string> 
#include <iostream>
#include <fstream>

using namespace std ;


int need( string gente )
{
	int amigos = 0 ;
	int acum = 0 ;
	for( int i = 0 ; i < gente.size() ; i ++ ) 
	{
		int n = gente[i] - '0' ;
		if( n == 0 ) continue ;
		if( i <= acum ) ; // esperaban i gente aplaudiendo pero ya hay mas
		else
		{
			amigos += ( i - acum ) ; // añadimos amigos justos pa que aplauda esta gente
			acum += amigos ; // añadimos amigos a gente
		}
		acum += n ;
	}
	return amigos ;
}



// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	// ifstream input() ;
	int T , Smax  , x ; 
	string line ;

	ifstream cin("C:\\Users\\villo_000\\Downloads\\A-small-attempt2.in") ;
	ofstream cout("output") ;

	cin >> T ; // if( T < 1 || 100	< T ) return 0 ;
	// for( string line ; getline(cin, line) ; ) 
	for( int t = 1 ; t <= T ; t ++ ) 
	{
        // std::cout << line << std::endl;

		// cin >> Smax ;
		// getline( cin , line ) ;
		cin >> Smax >> line ; // if( Smax < 0 || 6 < Smax ) return 0 ;


		// cout << line ;

		x = need( line ) ; 
		
		// cout << x ;
		cout << "Case #" << t << ": " << x << endl ;

    }
#if 0
	string gente = 
		// "1120000245" ;
		"00000000000000000000510000000000000000000000000000000000000009" ;

	int x = need(gente) ;

	cout << x ;
#endif
	return 0;
}

