// ProA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

unsigned long long paint() {
	unsigned long long r,t;
	scanf( "%llu %llu", &r, &t );

	bool done = false;
	unsigned long long rings = 0;

	unsigned long long a = 0;
	unsigned long long r2 = 2 * r;
	unsigned long long p = 0;
	while (!done) {
		p = r2 + ( 2 * a ) + 1;
		if ( p > t ) {
			break;
		}

		t -= p;
		rings++;
		a += 2;
	}

	return rings;
}


int _tmain(int argc, _TCHAR* argv[])
{
	unsigned int nTestCases = 0;
	unsigned int counter = 0;
	scanf( "%u", &nTestCases );

	while ( nTestCases-- ) {
		printf( "Case #%u: %u\n", ++counter, paint() );
	}

	return 0;
}

