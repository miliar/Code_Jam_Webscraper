#include<iostream>
#include<string>
#include<fstream>
using namespace std ;
int main ()
{
	int cur , ned , j , k , t , i ;
	string s ;
	ifstream in ("in.txt") ;
	ofstream out ("out.txt") ;
	in >> t ;
	for ( i = 1 ; i <= t ; i++ )
	{
		cur = 0 , ned = 0 ;
		in >> k >> s ;
		for ( j = 0 ; j < s.length() ; j ++ )
		{
			if (cur < j )
				ned += 1 , cur += 1 ;
			cur += s[j] - 48 ;
		}
		out << "Case #" << i << ": " << ned << '\n' ;
	}
	return 0 ;
}