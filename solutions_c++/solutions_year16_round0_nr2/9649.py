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

void rev( const vector<char>& pn, vector<char>& p, int pos )
{
	int N = pn.size();
	for( int i = 0; i < pos; i++ ){
		p[i] = (1-pn[(pos-1)-i]);
	}
	for( int i = pos; i < N; i++ ){
		p[i] = pn[i];
	}
}

void check( vector<char>& pn, int& f, int &b )
{
	int N = pn.size();

	for( int i = 0; i < N; i++ ){
		if( pn[0] != pn[i] )
			break;
		f++;
	}
	for( int i = N-1; i >= 0; i-- ){
		if( pn[N-1] != pn[i] )
			break;
		b++;
	}
}

int op( vector<char> pn, int idx, char s )
{
	if( idx == 1 ){
		if( pn[idx-1] != s )
			return 1;
		return 0;
	}

	int f = 0, b = 0;
	int N = pn.size();

	for( int i = 0; i < idx; i++ ){
		if( pn[0] != pn[i] )
			break;
		f++;
	}
	if( f == idx ){
		if( pn[idx-1] != s )
			return 1;
		return 0;
	}
	for( int i = idx-1; i >= 0; i-- ){
		if( pn[idx-1] != pn[i] )
			break;
		b++;
	}

	int ans = op(pn, idx-b, pn[idx-1]);
	if( pn[idx-1] != s )
		ans++;
	return ans;
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
		string p;
		fin >> p;
		vector<char> pn(p.length());
		for( int i = 0; i < p.length(); i++ ){
			if( p[i] == '-' ){
				pn[i] = 0;
			}else{
				pn[i] = 1;
			}
		}

		int ans = op( pn, pn.size(), 1 );

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