#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
	ifstream infl( "A-small-attempt0.in" );
	ofstream outfl( "bulleye_small.txt" );

	int num_of_tests;
	double radius;
	double paint;

	double radius2;
		
	double case_num = 0;


	infl >> num_of_tests;

	while( case_num < num_of_tests )
	{
		infl >> radius;
		infl >> paint;

		double rings = 0.;
		double total = 0.; 

		radius2 = radius+1.;

		total += (radius2 + radius) * (radius2 - radius );
		radius += 2.;

		while( total <= paint )
		{
			rings++;

			radius2 = radius+1.;

			total += (radius2 + radius) * (radius2 - radius );
			radius += 2.;
		}

	case_num++;

	outfl << "Case #" << fixed << setprecision(0) << case_num << ": "  << rings << endl; 

	}
}