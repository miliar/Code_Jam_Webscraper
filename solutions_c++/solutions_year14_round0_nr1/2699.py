#include<iostream>
#include<fstream>
using namespace std ;
int main ()
{
	ofstream out ;
	ifstream in ;
	out.open ("example.txt") ;
	in.open("A-small-attempt1.in") ;
	int i , j , k ; // counters
	int t , arr [ 4 ] [ 4 ] , r ; //test cases , card arrangment , row number
	int p1 [ 4 ] , p2 [ 4 ] ; // raw contestant chose
	int possibility ;
	int theone ;
	in >> t ;
	for ( i = 1 ; i <= t ; i ++ )
	{
		possibility = 0 ;
		in >> r ;
		for ( k = 0 ;  k < 4 ; k ++ )
			for ( j = 0 ; j < 4 ; j ++ )
				in >> arr [ k ] [ j ] ;
		for ( k = 0 ; k < 4 ; k ++ )
			p1 [ k ] = arr [ r-1 ] [ k ] ;
		//
		in >> r ;
		for ( k = 0 ;  k < 4 ; k ++ )
			for ( j = 0 ; j < 4 ; j ++ )
				in >> arr [ k ] [ j ] ;
		for ( k = 0 ; k < 4 ; k ++ )
			p2 [ k ] = arr [ r-1 ] [ k ] ;
		//
		for ( k = 0 ; k < 4 ; k ++ )
			for ( j = 0 ; j < 4 ; j ++ )
				if ( p1 [ k ] == p2 [ j ] )
				{
					possibility ++ ;
					theone = k ;
				}
		out << "Case #" << i << ": " ;
		if ( possibility == 0 )
			out << "Volunteer cheated!\n" ;
		else if ( possibility == 1 )
			out << p1 [ theone ] << '\n' ;
		else out << "Bad magician!\n" ;
	}
	
}