//Use Visual Studio Express 2008 to compile
// cj13.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <set>
#define digitCount 7
using namespace std;
unsigned long long pow( const unsigned long& n, const unsigned long& times ) {
	unsigned long long r = 1;
	for ( unsigned long i = 0 ; i < times; i++ ) {
		r *= n;
	}
	return r;
}
set<unsigned long long> palSq;
unsigned long long pal;
unsigned long long A,B;
unsigned long T;
bool finished = false;
unsigned long long isPal( unsigned long long pal ){
	if ( pal == 0 )
		return 0;
	while( pal%10 == 0 )
		pal /= 10;
	pal *= pal;
	unsigned long long c = pal;
	unsigned long temp;
	while( pal != 0 ) {
		for ( temp = 1 ; pal / pow( 10, temp ) != 0 ; temp++ );
		temp--;
		if ( pal / pow( 10, temp ) != pal % 10 )
			return 0;
		pal -= (pal % 10)*pow( 10, temp );
		pal /= 10;
	}
	return c;
}
void rec( unsigned long digits ){
	if ( digits == 0 ){
		palSq.insert( isPal(pal) );
		unsigned long long p = (pal - pal % pow( 10,digitCount/2))*10 + pal % pow( 10,digitCount/2);
		for ( unsigned long i = 0 ; i < 10 && !finished; i++ ) {
			p += i*pow( 10,digitCount/2);
			palSq.insert( isPal(p) );
			p -= i*pow( 10,digitCount/2);
		}
		return;
	}
	for ( unsigned long i = 0 ; i < 10 && !finished; i++ ) {
		unsigned long long p = pow( 10, digitCount/2-digits )+ pow( 10, digitCount/2+digits-1 );
		pal += i*p;
		rec( digits - 1 );
		pal -= i*p;
	}
}
bool Dummy( unsigned long long n ) {
	return true;
}
int _tmain(int argc, _TCHAR* argv[])
{
	rec(digitCount/2);
	cin >> T;
	for ( unsigned long i = 0 ; i < T; i++ ) {
		cin >> A >> B;
		set<unsigned long long>::iterator low = palSq.lower_bound (A); 
		set<unsigned long long>::iterator up  = palSq.upper_bound (B); 
		cout << "Case #" << i+1 << ": " << count_if(low,up,Dummy) << "\n";
	}
	/*for ( set< unsigned long long >::iterator it = palSq.begin(); it != palSq.end(); ++it )
		cout << *it << "\n";*/
	//system("pause");
	return 0;
}

