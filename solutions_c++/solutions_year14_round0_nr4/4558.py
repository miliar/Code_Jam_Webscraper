// GoogleCodeJam_2014_QD.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

#define MAX 1000

#define FOR( i, a, n ) for ( (i) = (a); (i) < (n) ; (i)++ )

int Shift( int * a, int n )
{
	int i;
	FOR ( i, 0, n )
	{
		a[n-i] = a[n-i-1];
	}

	return 0;
}

bool ChkAll ( int * a, int * b, int n )
{
	int i;

	FOR ( i, 0, n )
	{
		if ( a[i] < b[i] ) return false;
	}

	return true;
}

//std::sort(a, a+10, compare);

int _tmain(int argc, _TCHAR* argv[])
{
	int iPro;

	long i,j,k;
	
	int iResDW, iResW;

	int N, iDigit;

	int Naomi[MAX], Ken[MAX];

	int Na[MAX], Ke[MAX];

	float f;
	string s;

	ifstream in;
	ofstream out;



//	in.open("input.text");
//    in.open("D-small-attempt0.in");
	in.open("D-large.in" );
	out.open("out_ld.text");

	in >> iPro;

	for (k=1;k<=iPro;k++)
	{
		iResDW = 0;
		iResW = 0;

		in >> N;

		FOR( i, 0, N )
		{
			in >> s;
			Naomi[i] = atoi( s.c_str() +2 ) ;			
		}
	
		FOR( i,0, N)
		{
			in >> s;
			Ken[i] = atoi( s.c_str() +2 ) ;		
		}

		sort( Naomi, Naomi+N , greater<int>());
		sort( Ken, Ken+N, greater<int>() );

		// War

		iResW = 0;

		FOR( i,0,N )
		{
			Na[i] = Naomi[i];
			Ke[i] = Ken[i];
		}

		FOR( i, 0 , N )
		{
			if ( Na[i] > Ke[i] )
			{
				Shift( &Ke[i], N - i -1 );

				iResW ++;
			}

		}


		// D War
		
		FOR( i,0,N )
		{
			Na[i] = Naomi[i];
			Ke[i] = Ken[i];
		}


		FOR ( i, 0 , N )
		{
			if ( ChkAll( &Na[i], &Ke[i], N - i ) )
			{
				iResDW = N - i;

				break;
			}
			else
			{
				Shift( &Na[i], N - i -1 );
			}

		}

		out << "Case #" << k << ": " <<  iResDW << " " << iResW << endl;

	}

	return 0;
}



/*
Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4
*/
