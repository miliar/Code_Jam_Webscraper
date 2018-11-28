//============================================================================
// Name        : jjj.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	ifstream in ("in.txt") ;
	ofstream out ("out.txt") ;
	vector < int > v ;
	string s ;
	int t , i , j ;
	in >> t ;
	for ( j = 1 ; j < t+1 ; j ++ )
	{
		v.clear() ;
		in >> s ;
		while ( s.find('Z') != string::npos )
		{
			v.push_back(0);
			s.erase(s.find('Z'), 1) ;
			s.erase(s.find('E'), 1) ;
			s.erase(s.find('R'), 1) ;
			s.erase(s.find('O'), 1) ;
		}
		while ( s.find('W') != string::npos )
		{
			v.push_back(2);
			s.erase(s.find('W'), 1) ;
			s.erase(s.find('T'), 1) ;
			s.erase(s.find('O'), 1) ;
		}
		while ( s.find('G') != string::npos )
		{
			v.push_back(8);
			s.erase(s.find('G'), 1) ;
			s.erase(s.find('E'), 1) ;
			s.erase(s.find('I'), 1) ;
			s.erase(s.find('H'), 1) ;
			s.erase(s.find('T'), 1) ;
		}
		while ( s.find('H') != string::npos )
		{
			v.push_back(3);
			s.erase(s.find('R'), 1) ;
			s.erase(s.find('E'), 1) ;
			s.erase(s.find('E'), 1) ;
			s.erase(s.find('H'), 1) ;
			s.erase(s.find('T'), 1) ;
		}
		while ( s.find('U') != string::npos )
		{
			v.push_back(4);
			s.erase(s.find('U'), 1) ;
			s.erase(s.find('O'), 1) ;
			s.erase(s.find('F'), 1) ;
			s.erase(s.find('R'), 1) ;
		}
		while ( s.find('X') != string::npos )
		{
			v.push_back(6);
			s.erase(s.find('X'), 1) ;
			s.erase(s.find('I'), 1) ;
			s.erase(s.find('S'), 1) ;
		}
		while ( s.find('O') != string::npos )
		{
			v.push_back(1);
			s.erase(s.find('O'), 1) ;
			s.erase(s.find('N'), 1) ;
			s.erase(s.find('E'), 1) ;
		}
		while ( s.find('S') != string::npos )
		{
			v.push_back(7);
			s.erase(s.find('S'), 1) ;
			s.erase(s.find('E'), 1) ;
			s.erase(s.find('V'), 1) ;
			s.erase(s.find('E'), 1) ;
			s.erase(s.find('N'), 1) ;
		}
		while ( s.find('V') != string::npos )
		{
			v.push_back(5);
			s.erase(s.find('F'), 1) ;
			s.erase(s.find('I'), 1) ;
			s.erase(s.find('V'), 1) ;
			s.erase(s.find('E'), 1) ;
		}
		while ( s.size() != 0 )
		{
			v.push_back(9);
			s.erase(s.find('N'), 1) ;
			s.erase(s.find('I'), 1) ;
			s.erase(s.find('N'), 1) ;
			s.erase(s.find('E'), 1) ;
		}
		sort ( v.begin() , v.end()) ;
		out << "Case #" << j << ": " ;
		for ( i  = 0 ; i < v.size() ; i ++ )
			out << v[i] ;
		out << endl ;
	}
	return 0;
}
