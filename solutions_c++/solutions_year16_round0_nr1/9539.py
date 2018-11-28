#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <windows.h>

using namespace std;
#pragma warning(disable: 4996)

#define OUTPUTLOG2(X,Y)\
{\
	char msg[1024];\
	sprintf( msg, X, Y );\
	OutputDebugString(msg);\
}
#define OUTPUTLOG OutputDebugString

bool check( unsigned int& d, long long N )
{
	while( N != 0 ){
		d = d | (1 << (N % 10));
		N /= 10;
	}

	if( d == 0x3ff )
		return true;
	return false;
}

void main(int argc, char*argv[]) // usage: main.exe in.txt out.txt
{
	ifstream fin(argv[1]);
	if( fin == NULL ){
		OUTPUTLOG2("cannot open in-file : %s\n", argv[1]);
		return;
	}
	FILE* fout = fopen(argv[2],"w");
	if( fin == NULL ){
		OUTPUTLOG2("cannot open out-file : %s\n", argv[2]);
		return;
	}

/////////////////////////////
	char line[1024];
	int CASE;
	fin >> CASE;
	for( int test_case = 1; test_case <= CASE; test_case++ ){
	/////////////////////////////
		long long N;
		fin >> N;

		if( N == 0 ){
			fprintf(fout,"Case #%d: INSOMNIA\n", test_case);
			continue;
		}

		unsigned int d = 0;
		long long A = N;
		while(1){
			if( check(d, A) )
				break;
			A += N;
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: %lld\n", test_case, A);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}