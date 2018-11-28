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
		int N, M;
		fin >> N;
		fin >> M;
		string ret;
		vector<vector<int>> l(N, vector<int>(M));
		for( int i = 0; i < N;i ++ )
			for( int j = 0; j < M; j++ )
				fin >> l[i][j];

		bool yes = true;
		for( int y = 0; y < N; y++ ){
			for( int x = 0; x < M; x++ ){
				bool bHighX = false;
				bool bHighY = false;
				for( int r = 0; r < M; r++ ){
					if( l[y][r] > l[y][x] ){
						bHighX = true;
						break;
					}
				}
				for( int c = 0; c < N; c++ ){
					if( l[c][x] > l[y][x] ){
						bHighY = true;
						break;
					}
				}
				if( bHighX && bHighY ){
					ret = "NO";
					goto end;
				}
			}
		}
		ret = "YES";

	/////////////////////////////
end:
		fprintf(fout,"Case #%d: %s\n", test_case, ret.c_str());
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}