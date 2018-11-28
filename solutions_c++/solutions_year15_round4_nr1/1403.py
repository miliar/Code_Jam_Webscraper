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

bool Up( vector<vector<int>>& BD, int y, int x, int R, int C )
{
	for( int i = y-1; i >= 0; i-- ){
		if( BD[i][x] != 0 )
			return true;
	}
	return false;
}

bool Down( vector<vector<int>>& BD, int y, int x, int R, int C )
{
	for( int i = y+1; i < R; i++ ){
		if( BD[i][x] != 0 )
			return true;
	}
	return false;
}

bool Left( vector<vector<int>>& BD, int y, int x, int R, int C )
{
	for( int i = x-1; i >= 0; i-- ){
		if( BD[y][i] != 0 )
			return true;
	}
	return false;
}

bool Right( vector<vector<int>>& BD, int y, int x, int R, int C )
{
	for( int i = x+1; i < C; i++ ){
		if( BD[y][i] != 0 )
			return true;
	}
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
		int R, C;
		fin >> R;
		fin >> C;
		vector<vector<int>> BD(R, vector<int>(C, 0));
		for( int y = 0; y < R; y++ ){
			fin >> line;
			for( int x = 0; x < C; x++ ){
				if( line[x] == '^' )
					BD[y][x] = 1;
				else if( line[x] == '>' )
					BD[y][x] = 2;
				else if( line[x] == 'v' )
					BD[y][x] = 3;
				else if( line[x] == '<' )
					BD[y][x] = 4;
			}
		}
		int ans = 0;
		bool bImpossible = false;
		for( int y = 0; y < R; y++ ){
			for( int x = 0; x < C; x++ ){
				if( BD[y][x] != 0 ){
					if( BD[y][x] == 1 ){
						if( !Up(BD, y, x, R, C ) ){
							if( Left(BD, y, x, R, C ) || Down(BD, y, x, R, C ) || Right(BD, y, x, R, C ) )
								ans++;
							else{
								bImpossible = true;
								goto end;
							}
						}
					}else if( BD[y][x] == 2 ){
						if( !Right(BD, y, x, R, C ) ){
							if( Left(BD, y, x, R, C ) || Down(BD, y, x, R, C ) || Up(BD, y, x, R, C ) )
								ans++;
							else{
								bImpossible = true;
								goto end;
							}
						}
					}else if( BD[y][x] == 3 ){
						if( !Down(BD, y, x, R, C ) ){
							if( Left(BD, y, x, R, C ) || Up(BD, y, x, R, C ) || Right(BD, y, x, R, C ) )
								ans++;
							else{
								bImpossible = true;
								goto end;
							}
						}

					}else if( BD[y][x] == 4 ){
						if( !Left(BD, y, x, R, C ) ){
							if( Up(BD, y, x, R, C ) || Down(BD, y, x, R, C ) || Right(BD, y, x, R, C ) )
								ans++;
							else{
								bImpossible = true;
								goto end;
							}
						}
					}
				}
			}
		}
end:

	/////////////////////////////
		if( bImpossible )
			fprintf(fout,"Case #%d: IMPOSSIBLE\n", test_case);
		else
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