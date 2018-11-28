#include<fstream>
#include<vector>
#include<string>
#include<iostream>
using namespace std ;
int main ()
{
	long long t , i , n , m1 , max , m2 , j ;
	vector < long long > v ;
	ifstream in ("in2.txt") ;
	ofstream out ("out2.txt") ;
	in >> t ;
	for ( i = 1 ; i <= t ; i ++ )
	{
		m1 = 0 , m2 = 0 , max = 0 ;
		v.clear() ;
		in >> n ;
		v.resize(n) ;
		for ( j = 0 ; j < n ; j ++ )
		{
			in >> v [ j ] ;
			if ( j > 0 && v [ j ] < v [ j-1 ] )
				m1 += v[j-1] - v[j] ;
			if ( j > 0 && v [ j-1 ] - v[j] > max )
				max = v [ j-1 ] - v[j] ;
		}
		for ( j = 0 ; j < n-1 ; j ++ )
		{
			if  ( v [ j ] < max )
				m2 += v[j] ;
			else
				m2+= max ;
		}
		out << "Case #" << i << ": " << m1 << ' ' << m2 << '\n' ;
	}
}