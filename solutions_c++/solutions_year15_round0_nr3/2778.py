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

int multiply( int a, int b )
{
	static const int table[4][4] = {
		{1,2,3,4},
		{2,-1,4,-3},
		{3,-4,-1,2},
		{4,3,-2,-1}
	};

	int aa = abs(a);
	int ab = abs(b);
	int sign;
	if( a*b < 0 )
		sign = -1;
	else
		sign = 1;

	return sign * table[aa-1][ab-1];
}

vector<vector<int>> memo;

int f( const vector<int>& a, int p1, int p2 )
{
	if( p1 == p2-1 )
		return a[p1];

	if( memo[p1][p2] != 0 )
		return memo[p1][p2];

	int val = multiply( a[p1], f(a, p1+1, p2) );
	memo[p1][p2] = val;

	return val;
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
		int L, X;
		fin >> L;
		fin >> X;

		vector<int> a(L*X);
		string s;
		getline( fin, s );
		getline( fin, s );

		if( L*X < 3 ){
			fprintf(fout,"Case #%d: NO\n", test_case);
			continue;
		}
		memo.assign(L*X+1, vector<int>(L*X+1, 0));

		for( int i = 0; i < s.size(); i++ ){
			a[i] = s[i] - 'i' + 2;
		}
		for( int i = L; i < L*X; i++ ){
			a[i] = a[i%L];
		}
		bool bPossible = false;

		for( int p1 = 1; p1 < L*X-1; p1++ ){
			if( f( a, 0, p1 ) != 2 )
				continue;
			for( int p2 = p1+1; p2 < L*X; p2++ ){
				if( f( a, p1, p2 ) != 3 )
					continue;

				if( f( a, p2, L*X ) == 4 ){
					bPossible = true;
					goto end;
				}
			}
		}
end:
	/////////////////////////////
		if( bPossible )
			fprintf(fout,"Case #%d: YES\n", test_case);
		else
			fprintf(fout,"Case #%d: NO\n", test_case);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}