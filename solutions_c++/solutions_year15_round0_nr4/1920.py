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
		int X, R, C;
		fin >> X;
		fin >> R;
		fin >> C;
		string ans;

		if( X == 1 ){
			ans = "GABRIEL";
		}else if( X == 2 ){
			if( R&1 && C&1 )
				ans = "RICHARD";
			else
				ans = "GABRIEL";
		}else if( X == 3 ){
			if( R != 3 && C != 3 )
				ans = "RICHARD";
			else{
				if( R == 1 || C == 1 )
					ans = "RICHARD";
				else
					ans = "GABRIEL";
			}

		}else if( X == 4 ){
			ans = "RICHARD";
			if( R >= 3 && C >= 3 )
				if( R*C % 4 == 0 )
					ans = "GABRIEL";
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: %s\n", test_case, ans.c_str());
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}