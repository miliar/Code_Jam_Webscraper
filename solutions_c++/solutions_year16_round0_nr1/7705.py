#include<fstream>
#include<iostream>
using namespace std ;
void play ( int x , int *go , int &done )
{
	int temp ;
	while ( x > 0 )
	{
		temp = x % 10 ;
		x /= 10 ;
		go [ temp ] ++ ;
		if ( go[temp] == 1 ) done ++ ; ;
	}
}
int main ()
{
	ifstream in ("in.txt") ;
	ofstream out ("out.txt") ;
	int array [ 10 ] ;
	int t , done , n , i , j , k ;
	in >> t ;
	for ( i = 1 ; i <= t ; i ++ )
	{
		j = 0 ;
		in >> n ;
		done = 0 ;
		for ( k = 0 ; k < 10 ; k ++ ) array[k] = 0 ;
		if ( n == 0  )
		{
			out << "Case #" << i << ": INSOMNIA\n" ;
			continue ;
		}
		while ( done < 10 )
		{
			j ++ ;
			play ( n*j , array , done ) ;
		}
		out << "Case #" << i << ": " << n*j << '\n' ;
	}
	return 0 ;
}
