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

#define FOR(r,a,b) for(r=(a); r<(b); r++)
#define REP(r,b) for(r=0; r<(b); r++)
#define TRV(type,cnt,it) for(type::iterator it=(cnt).begin(); it!=(cnt).end(); it++)

bool palindrome( unsigned long long num )
{
	char buf[128];
	sprintf( buf, "%I64d", num );
	int len = strlen( buf );

	for( int i = 0; i < len/2; i++ ){
		if( buf[i] != buf[len-1-i] ){
			return false;
		}
	}

	return true;
}

void main(int argc, char*argv[]) // usage: main.exe in.txt out.txt
{
	int i,j,k,l,m,n;

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
		unsigned long long A, B;
		fin >> A;
		fin >> B;
		unsigned long long A2, B2;
		A2 = (unsigned long long )sqrt((double)A) - 1;
		B2 = (unsigned long long )sqrt((double)B) + 1;
		if( A2 < 1 )
			A2 = 1;
		if( B2 < 1 )
			B2 = 1;

		int ans = 0;
		for( unsigned long long C = A2; C <= B2; C++ ){
			if( palindrome( C ) ){
				if( palindrome( C*C ) ){
					if( C*C >= A && C*C <= B ){
						ans++;
					}
				}
			}
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: %d\n", test_case, ans);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}