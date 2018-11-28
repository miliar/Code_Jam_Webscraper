// GoogleCodeJam_2014_QB.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define FOR( i, a, n ) for ( (i) = (a); (i) < (n) ; (i)++ )


//std::sort(a, a+10, compare);

int _tmain(int argc, _TCHAR* argv[])
{
	int iPro;

	long i,j,k;

	float C, F, X;

	float fRes;

	float fThis;

	ifstream in;
	ofstream out;



//	in.open("input.text");
    in.open("B-small-attempt4.in");
	//in.open("A-large.in" );
	out.open("out1.text");

	in >> iPro;

	for (k=1;k<=iPro;k++)
	{
		fRes = 0.0;

		in >> C >> F >> X;
		
		FOR( i, 0, 10000 )
		{
			fThis = 0.0;

			FOR( j, 0, i )
			{
				fThis += C / ( j * F + 2.0 ); 
			}

			fThis += X /( 2.0 + i * F ); 
		
			if ( fRes == 0.0 ) fRes = fThis;
			else if ( fRes > fThis ) fRes = fThis;
			else if ( fRes < fThis ) break;
			
		}
	
		out << "Case #" << k << ": " << std::fixed <<setprecision(7 + (int)log10(fRes) ) <<setiosflags( ios::showpoint) <<  fRes << endl;

	
	}

	return 0;
}



/*
Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
*/