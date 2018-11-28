// GoogleCodeJam_2013_1C_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


//std::sort(a, a+10, compare);


int main(int argc, char* argv[])
{
	int iPro;

	long i,j,k;
	
	long n, l, nnow, res;

	string as;

	ifstream in;
	ofstream out;



//	in.open("in.txt");
	in.open("A-small-attempt0.in");
	out.open("outs.text");

	in >> iPro;

	for (k=1;k<=iPro;k++)
	{
		in >> as >> n;

		res = 0;

		for ( i=0; i<as.size()-n+1; i++)
		{
			nnow = 0;

			for ( j=i; j< as.size(); j++)
			{
				if ( ( as.substr(j,1) == "a" ) || ( as.substr(j,1) == "e" ) || ( as.substr(j,1)== "i" ) || ( as.substr(j,1) == "o" ) || ( as.substr(j,1)== "u" ) )
				{
					nnow = 0;
				}
				else				
					nnow++;
				
				if ( n == nnow ) 
				{
					res += as.size()-j;
					break;
				}
			}
		}


		
		cout << "Case #" << k << ": " << res << endl;

		out << "Case #" << k << ": " << res << endl;


	}


	return 0;
}

