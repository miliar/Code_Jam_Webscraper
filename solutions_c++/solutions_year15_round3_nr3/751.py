#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std ;
int main ()
{
	ifstream inp ("in2a.txt") ;
	ofstream out ("out2a.txt") ;
	vector < long long > arr ;
	long long c , d , v , maxpos , cov , temp ;
	int t , ti , i ;
	inp >> t ;
	for ( ti = 1 ; ti <= t ; ti ++ )
	{
		inp >> c >> d >> v ;
		arr.resize(d) ;
		for ( i = 0 ; i < d ; i ++ )
			inp >> arr [ i ] ;
		if ( arr[0] == 1 )
			maxpos = 1 , cov = 1 ;
		else if ( arr[0] == 2 )
		{
			arr.push_back(1) ;
			i ++ ;
			cov = 3 ;
		}
		else if ( arr[0] > 2 )
		{
			arr.push_back(1) ;
			arr.push_back(2) ;
			i += 2 , cov = 3 ; ;
			if ( arr [ 0 ] == 3 || arr [ 0 ] == 4 )
				cov += arr[0] ;
			else
			{
				while ( cov < arr [ 0 ] - 1 )
			{
				arr.push_back( cov + 1 ) ;
				i ++ ;
				cov = 2*cov + 1 ;
			}
				cov += arr [ 0 ] ;
			}
		}
		for ( i = 1 ; cov < v ; i ++ )
		{
			if ( i < d ) temp = arr [ i ] ;
			else temp = v+1 ;
			while ( temp > cov+1 )
			{
				
				arr.push_back(cov + 1) ;
				cov = cov*2 + 1 ;
			}
			cov += temp ;
		}
		out << "Case #" << ti << ": " << arr.size() - d << '\n' ;
	}
}