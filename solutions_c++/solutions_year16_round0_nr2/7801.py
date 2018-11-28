#include<fstream>
#include<iostream>
#include<string>
using namespace std ;

int main ()
{
	ifstream in ("in.txt") ;
	ofstream out ("out.txt");
	string s ;
	int t , i , j , k , l , n , count ;
	in >> t ;
	for ( i = 1 ; i <= t ; i ++ )
	{
		s.clear() ;
		in >> s ;
		n = s.size() ;
		count = 0 ;
		for ( j = 0 ; j < n ;j ++ )
		{
			if ( s.find('-') == -1 ) break ;
			count ++ ;
			if ( s.find('+') == -1 ) break ;
			for ( k = j ; k < n ; k ++)
			{
				if ( s[k] != s[k+1]) break ;
			}
			for ( l = 0 ; l <= k ; l ++  )
				s[l] == '-' ? s[l] = '+' : s[l] = '-' ;
		}
		out << "Case #" << i << ": " << count << endl ;
	}
	return 0 ;
}
