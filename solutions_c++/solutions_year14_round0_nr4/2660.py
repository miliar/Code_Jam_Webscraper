#include <iostream>

#include <fstream>
#include <sstream>
#include <cstdlib>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <cfloat>

using namespace std;

const int Precision = 5;

void swap( int i, int j, double cases[] ) {
	double d;
	d = cases[i];
	cases[i] = cases[j];
	cases[j] = d;

	return;
};


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
	string str;
	getline( ins, str );
	T = atoi( str.c_str() );
	

	str.clear();

	outs.precision( Precision );
  	outs.setf( ios::fixed, ios::floatfield ); // floatfield set to fixed
  
		

	for ( int i = 0; i < T; i++ ) {		// For each case
		int N = 0;	// Number of weights

		getline( ins, str );	// Will contain N
		N = atoi( str.c_str() );
		double NaomiWeights[N], KenWeights[N];
	
		getline( ins, str );	// Will contain Naomi's weights	
		istringstream ss( str );
		string x;
		for ( int j = 0; j < N; j++ ) {
			getline( ss, x, ' ' );
			NaomiWeights[j] = atof( x.c_str() );	// Get Naomi's weights
			
		}

		getline( ins, str );	// Will contain Ken's weights	
		istringstream st( str );
		for ( int j = 0; j < N; j++ ) {
			getline( st, x, ' ' );
			KenWeights[j] = atof( x.c_str() );	// Get Ken's weights
			
		}
		
		// Now sort Naomi's weights

		for ( int k = 0; k < N; k++ ) {
			int indexSmallest = k;
			for ( int j = k+1; j < N; j++ ) {
				if ( NaomiWeights[j] < NaomiWeights[indexSmallest] ) indexSmallest = j;
			}
			if ( indexSmallest != k ) swap( k, indexSmallest, NaomiWeights );
		}

		// Now sort Ken's weights

		for ( int k = 0; k < N; k++ ) {
			int indexSmallest = k;
			for ( int j = k+1; j < N; j++ ) {
				if ( KenWeights[j] < KenWeights[indexSmallest] ) indexSmallest = j;
			}
			if ( indexSmallest != k ) swap( k, indexSmallest, KenWeights );
		}
		
		int fairWin = 0, deceitWin = 0;
		
		// War
		int j = 0;
		for ( int k = 0; j < N && k < N; k++ ) {
			while ( ( k < N ) && ( NaomiWeights[j] > KenWeights[k] ) ) k++;
			if ( k < N ) j++;
		}
		fairWin = N-j;

		// Deceitful War:
		
		j = 0;
		int k = 0;
		for ( ; j < N && k < N; ) {
			while ( ( j < N ) && ( k < N ) && ( NaomiWeights[j] < KenWeights[k] ) ) j++;
			if ( j < N ) deceitWin++;
			j++; k++;
		}
			
		outs << "Case #" << i+1 << ": " << deceitWin << " " << fairWin << "\n";
		

	}		
		
	outs.close();
	ins.close();


}