#include <iostream>
#include <cmath>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>

using namespace std;

int gcd(int u, int v) {
return (v != 0)?gcd(v, u%v):u;
}
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
	
	for ( int i = 0; i < T; i ++ ) {
		getline( ins, str );
		istringstream ss( str );
		int P = 0, Q = 0;
		string x;
		getline( ss, x, '/' );
		P = atoi( x.c_str() );
		x.clear();
		getline( ss, x, '/' );
		Q = atoi( x.c_str() );
		cout << "P = " << P << " Q = " << Q << "\n";
		cout << "gcs = " << gcd( P, Q ) << "\n";
		int P1 = 0, Q1 = 0;
		int g = 0;
		g = gcd( P, Q );
		P1 = P / g;
		Q1 = Q / g;
		int count = 0;
		int modd = 0;
		while ( Q1 > P1 ) {
			modd = Q1 % 2;
			if ( modd > 0 ) break;
			Q1 = Q1/2;
			count++;
			cout << "Q1 = " << Q1 << "\n";
		}
		int count2 = 0;
		while ( Q1 > 1 ) {
			modd = Q1 % 2;
			if ( modd > 0 ) break;
			Q1 = Q1 / 2;
		}
		if ( Q1 == 1 ) {
			cout << "count = " << count << "\n";
			outs << "Case #" << i+1 << ": " << count << "\n";
		} else {
			cout << "No elf\n";
			outs << "Case #" << i+1 << ": impossible\n";
		}
	
	}
	outs.close();
	ins.close();	
}