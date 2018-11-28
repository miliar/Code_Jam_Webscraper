// GoogleCodeJam_2014_QA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define FOR( i, a, n ) for ( (i) = (a); (i) < (n) ; (i)++ )

int ChkRow( int * a, int * b)
{
	int iRes = 0, iCnt = 0;
	int i,j;

	FOR( i, 0, 4 )
	{
		FOR( j, 0, 4 )
		{
			if ( a[i] == b[j] )
			{
				iRes = a[i];
				iCnt ++;
			}

		}

	}

	if ( iCnt == 0 ) iRes = -1;
	if ( iCnt > 1 ) iRes = -2;

	return iRes;

}

//std::sort(a, a+10, compare);

int _tmain(int argc, _TCHAR* argv[])
{
	int iPro;

	long i,j,k;
	
	int iRes;

	int a[4], b[4], temp[4];
	int anum, bnum;

	string as;

	ifstream in;
	ofstream out;



//	in.open("input.text");
    in.open("A-small-attempt0.in");
	//in.open("A-large.in" );
	out.open("out0.text");

	in >> iPro;

	for (k=1;k<=iPro;k++)
	{
		iRes = 0;

		in >> anum;

		FOR ( i, 1,  4 + 1 )
		{
			if ( i == anum )
			{
				FOR( j, 0, 4 )
					in >> a[j];
			}
			else 
			{
				FOR( j, 0, 4 )
					in >> temp[j];
			}
		}

		in >> bnum;

		FOR ( i, 1,  4 + 1 )
		{
			if ( i == bnum )
			{
				FOR( j, 0, 4 )
					in >> b[j];
			}
			else 
			{
				FOR( j, 0, 4 )
					in >> temp[j];
			}
		}

		iRes = ChkRow( a, b );
	
		if ( iRes >= 0 )
			out << "Case #" << k << ": " <<  iRes << endl;
		else if ( iRes == -2 )
			out << "Case #" << k << ": Bad magician!" << endl;
		else if ( iRes == -1 )
			out << "Case #" << k << ": Volunteer cheated!" << endl;

	
	}

	return 0;
}



/*
Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
*/