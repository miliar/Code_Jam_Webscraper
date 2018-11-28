//============================================================================
// Name        : jam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<fstream>
#include<string>
#include<vector>
#include<map>
using namespace std;
int main() {
	ifstream in ("in.txt") ;
	ofstream out ("out.txt") ;
	int count , t , sum , n , i , j , k ;
	in >> t ;
	vector < int > v ;
	string s , chars ;
	bool equality ;
	char a1 , a2 ;
	int max ;
	for ( i = 1 ; i <= t ; i ++ )
	{
		out << "Case #" << i << ": " ;
		a1 = '!' ; a2 = '!' ;
		max = 0 ;
		equality = false ;
		s.clear() ;
		v.clear() ;
		sum = 0 ;
		in >> n ;
		for ( j = 0 ; j < n ; j ++ )
		{
			in >> k ;
			sum += k ;
			if ( k > 0 )
				chars += char (j+'A') ;
			v.push_back(k) ;
		}
		while ( sum > 0 )
		{
			s.clear() ;
			a1 = '!' ; a2 = '!' ;
			max = 0 ;
			equality = false ;
			for ( j = 0 ; j < chars.size() ; j ++ )
			{
				if ( v [ int (chars[j] - 'A') ] > max )
				{
					max = v [ int (chars[j] - 'A') ] ;
					a1 = chars[j] ;
					a2 = '!';
					equality = false ;
				}
				else if ( v [ int (chars[j] - 'A') ] == max )
				{
					if ( a1 == '!' )
						a1 = chars[j] ;
					else if ( a2 == '!')
						a2 = chars[j] ;
					else equality = 1 ;
				}
			}
			if ( a2 != '!' )
			{
				s.push_back(a1) ;
				sum -- ;
				v [ int ( a1 - 'A') ] -- ;
				if ( v [ int ( a1 - 'A') ] == 0 )
					chars.replace( chars.find(a1) , 1 , "") ;
				if ( sum != 2)
				{
					s.push_back(a2) ;
					sum -- ;
					v [ int ( a2 - 'A') ] -- ;
					if ( v [ int ( a2 - 'A') ] == 0 )
						chars.replace( chars.find(a2) , 1 , "") ;
				}
			}
			else if ( a2 == '!')
			{
				s.push_back(a1) ;
				sum -- ;
				v [ int ( a1 - 'A') ] -- ;
				if ( sum != 2 && v [ int ( a1 - 'A') ] != 0 && !( chars.size() == 2 && v [ int ( a1 - 'A') ] == sum / 2 ) )
				{
					s.push_back( a1 ) ;
					sum -- ;
					v [ int ( a1 - 'A') ] -- ;
				}
				if ( v [ int ( a1 - 'A') ] == 0 )
					chars.replace( chars.find(a1) , 1 , "") ;
			}
			out << s ;
			if ( chars.size() > 0 )
				out << ' ' ;
			else out << '\n' ;
		}
	}
	return 0;
}
