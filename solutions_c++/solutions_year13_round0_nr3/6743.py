/*
 * File:   main.cpp
 * Author: cabloo
 *
 * Created on April 12, 2013, 7:55 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

struct pr {
	long a;
	long b;
};

long reverse(long i){
	long rev = 0;
	while( i > 0 ){
		rev = rev * 10 + i % 10;
		i = i / 10;
	}

	return rev;
}

bool palendrome( long i ){
	return i == reverse( i );
}

/*
 *
 */
int main(int argc, char** argv) {
	long T, A, B, Z, N, X, high = 0;
	ifstream in( "input.txt" );
	in >> T;
	pr cases[T];
	pr p;
	for( int i = 0; i < T; i++ ){
		in >> p.a >> p.b;
		cases[i] = p;
		if( p.b > high ) high = p.b;
	}
	vector<bool> pals = vector<bool>(high+1,false);

	for( Z = 1; Z <= sqrt(high); Z++ ){
		if( !palendrome( Z ) ) continue;
		X = Z*Z;
		if( !palendrome( X ) ) continue;
		pals[Z*Z] = true;
	}

	for( int i = 1; i <= T; i++ ){
		p = cases[i-1];
		A = p.a;
		B = p.b;
		N = 0;

		for( ; A <= B; A++ ){
			if( !pals[A] ) continue;
			N++;
			//cout << A << "\t";
		}

		cout << "Case #" << i << ": " << N << "\n";
	}
	return 0;
}

