#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std ;
int main ()
{
	ifstream in ; ofstream out ;
	in.open("in2.txt") ; out.open("out.txt") ;
	int t , l , N , i , j , m ;
	int low , high ;
	int *arr ;
	float *ny ;
	float *k ;
	in >> t ;
	for ( l = 1 ; l <= t ; l ++ )
	{
		in >> N ;
		i = 2 * N ;
		ny = new float [ N ] ;
		k = new float [ N ] ;
		arr = new int [ i ] ;
		for ( i = 0 ; i < N ; i ++ )
			in >> ny [ i ] ;
		for ( i = 0 ; i < N ; i ++ )
			in >> k [ i ] ;
		sort ( ny , ny + N ) ;
		sort ( k , k + N ) ; 
		i = 1 ; j = 1 ;
		for ( m = 2*N - 1 ; m > -1 ; m -- )
		{
			if ( k [ N - i ] > ny [ N - j ] )
			{
				arr [ m ] = 1 ; i ++ ;
			}
			else 
			{
				arr [ m ] = 0 ; j ++ ;
			}
		}
		j = 0 , low = 0 ;
		for ( i = 2*N-1 ; i > -1 ; i -- )
		{
			if ( arr [ i ] == 0 )
				if ( j == 0 )
					low ++ ;
				else j -- ;
			else j ++ ;
		} j = 0 , high = N ;
		for ( i = 0 ; i < 2*N ; i ++ )
		{
			if ( arr [ i ] == 0 )
				if ( j == 0 )
					high -- ;
				else j -- ;
			else j ++ ;
		}
		out << "Case #" << l << ": " << high << ' ' << low <<'\n' ;
	}

}