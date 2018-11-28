#include<iostream>
#include<fstream>
using namespace std ;
int main ()
{
	ifstream in ; ofstream out ;
	in.open("in.txt") ;
	out.open("out.txt") ;
	out.precision(15) ;
	long double factor = 2 ;
	long double C , F , X ;
	long double time ;
	int t , i ;
	in >> t ;
	for ( i = 1 ; i <= t ; i ++ )
	{
		in >> C >> F >> X ;
		time = 0 , factor = 2 ;
		while ( 1 ) 
		{
			time += C / factor ;
			if ( X / ( factor + F ) > ( X - C ) / factor )
				break ;
			factor += F ;
		}
		time += ( X - C ) / factor ;
		out << "Case #" << i << ": " << time << '\n' ;
	}
	in.close() ; out.close() ;
}