#include <bits/stdc++.h>
using namespace std;

map< int , int > my_map ;
int matrix[4][4] ;
char str[300],ch;

int main()
{
	int t , k , i , j ;

	ifstream ip("in.txt");
	ofstream op("out.txt");

	ip>>t;
	//p.get(ch);

	int row_number , counter , number ;
	for(k=1;k<=t;k++)
	{
	    my_map.clear() ;
		counter = 0 ;
		ip >> row_number ; row_number-- ;

		for( i = 0 ; i < 4 ; i++ )
			for( j = 0 ; j < 4 ; j++ )
				ip >> matrix[i][j] ;

		for( i = 0 ; i < 4 ; i++ )
			my_map[ matrix[row_number][i] ]++ ;

		ip >> row_number ; row_number-- ;
		for( i = 0 ; i < 4 ; i++ )
			for( j = 0 ; j < 4 ; j++ )
				ip >> matrix[i][j] ;

		for( i = 0 ; i < 4 ; i++ ) {
			if( my_map[ matrix[row_number][i] ] ) { counter++ ; number = matrix[row_number][i] ; }
		}

		//p.getline(str,300);
		op<<"Case #"<<k<<": ";

		if( counter == 1 ) op << number << endl ;
		else if( counter  ) op << "Bad magician!" << endl ;
		else op << "Volunteer cheated!" << endl ;

	}
	ip.close();
	op.close();
	return 0;
}
