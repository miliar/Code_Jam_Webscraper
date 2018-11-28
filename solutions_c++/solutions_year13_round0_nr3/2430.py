// GoogleCodeJam_2013_Third.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <list>

using namespace std;

const double MAX_NUM = 10000000;

bool IsPalindromes( double a )
{
	list <int> lst;

	double mov = 10;

	if ( a - floor( a/mov ) * mov  == 0 ) return false;

	while(a)
	{
		lst.push_back( a - floor( a/mov ) * mov );

		a = floor(a/mov);
	};

	while(!lst.empty())
	{
		if (lst.size()==1) return true;

		if ( *(lst.begin()) == *(lst.rbegin()) )
		{
			lst.pop_front();
			lst.pop_back();
		}
		else
		{
			return false;
		}
	}

	return true;
}


int main(int argc, char* argv[])
{
	int iPro;

	int k;

	double a,b;

	vector<double> vec;

	ifstream in;
	ofstream out;

	//in.open("C-small-attempt0.in");
	in.open("C-large-1.in");
	out.open("out_third_l.txt");

	for ( a=1;a<MAX_NUM;a++)
	{
		if ( IsPalindromes( a ) )
		{
			if ( IsPalindromes( a*a ) )
			{
				vec.push_back(a*a);
				cout.precision(14);
				cout << a << " "<< a*a<<endl;
			}
		}
	}
	
	
	in >> iPro;

	for(k=1;k<=iPro;k++)
	{
		in >> a >> b;

		vector<double>::iterator ii;

		int num=0;

		for ( ii=vec.begin();ii<vec.end();ii++)
		{
			if ( *ii < a ) continue;
			if ( *ii > b ) break;
			
			num++;
		}

		out << "Case #" << k << ": " << num << endl; 

	}


	return 0;
}

