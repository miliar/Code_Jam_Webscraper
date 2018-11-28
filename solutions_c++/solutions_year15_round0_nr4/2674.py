//this code could be used for small case only
#include<fstream>
#include<iostream>
using namespace std ;
int main ()
{
	ifstream in ("in.txt") ;
	ofstream out ("out.txt") ;
	int t , i , x , r , c ;
	in >> t ;
	for ( i = 1 ; i <= t ; i ++ )
	{
		in >> x >> r >> c ;
		if ( x == 1 )
			out << "Case #" << i << ": GABRIEL" << endl ;
		else if ( x == 2 )
			if ( r*c % 2 == 0 )
				out << "Case #" << i << ": GABRIEL\n" ;
			else
				out << "Case #" << i << ": RICHARD\n" ;
		else if ( x == 3 )
			if ( r*c % 3 == 0 && r*c > 3 )
				out << "Case #" << i << ": GABRIEL\n" ;
			else
				out << "Case #" << i << ": RICHARD\n" ;
		else if ( x == 4 )
			if ( r*c % 4 == 0 && r*c > 8 )
				out << "Case #" << i << ": GABRIEL\n" ;
			else
				out << "Case #" << i << ": RICHARD\n" ;
	}
}