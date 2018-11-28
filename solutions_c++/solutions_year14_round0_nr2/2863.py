#include <iostream>

#include <fstream>
#include <sstream>
#include <cstdlib>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <cfloat>

using namespace std;

const double RateWithNoFarms = 2.0;
const int Precision = 7;

int main (int argc, char *argv[]) {
	ifstream ins(argv[1]);

	if ( !ins ) {
	cerr << "Cannot open: infile\n";

		exit(1);

	}


	ofstream outs(argv[2]);

	if ( !outs ) {
	cerr << "Cannot open: outfile\n";

		exit(1);

	}




	int T = 0;	// T Number of cases.
	double C, F, X;	// C is cost of farm; F is production rate of a farm; X is cookies required
	string str;
	getline( ins, str );
	T = atoi( str.c_str() );
	
	str.clear();


	outs.precision( Precision );
  	outs.setf( ios::fixed, ios::floatfield ); // floatfield set to fixed

	for ( int i = 0; i < T && getline( ins, str ); i++ ) {		// For each case
		istringstream ss( str );
		string x;
		getline( ss, x, ' ' );
		C = atof( x.c_str() );	// Get val of C
		getline( ss, x, ' ' );
		F = atof( x.c_str() );	// Get val of F
		getline( ss, x, ' ' );
		X = atof( x.c_str() );	// Get val of X

  
		int farms = 1;
		double totalTimeWithnFarms = 0.0, totalTimeWithn_1Farms = 0.0, totalTimeToAcquiren_1Farms = 0.0, totalTimeToAcquirenFarms = 0.0;
		double timeToAcquirenthFarm = 0.0;
		totalTimeWithn_1Farms = X/RateWithNoFarms;	// Time taken with 0 farm.
		totalTimeWithnFarms = ( C/2 ) + ( X/(2+F) );	// Time taken with 1 farm.
		timeToAcquirenthFarm = C/2;		// Time to acquire first farm.

		totalTimeToAcquirenFarms = timeToAcquirenthFarm;	// 1 farm has been acquired before starting series.
		
		for ( farms = 2; totalTimeWithn_1Farms > totalTimeWithnFarms; farms++ ) {	// Build the series adding 1 farm at a time until the min total time is achieved

			totalTimeWithn_1Farms = totalTimeWithnFarms;
			totalTimeToAcquiren_1Farms = totalTimeToAcquirenFarms;

			timeToAcquirenthFarm = C/( 2+(farms-1)*F );
			totalTimeToAcquirenFarms = totalTimeToAcquiren_1Farms + timeToAcquirenthFarm;
			totalTimeWithnFarms = totalTimeToAcquirenFarms + ( X/(2+farms*F) );

			

		}
			
		outs << "Case #" << i+1 << ": " << totalTimeWithn_1Farms << "\n";
		

	}		
		
	outs.close();
	ins.close();


}