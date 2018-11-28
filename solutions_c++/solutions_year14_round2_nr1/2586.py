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
	int CASE;
	fin >> CASE;
	for( int test_case = 1; test_case <= CASE; test_case++ ){
	/////////////////////////////
		int N;
		fin >> N;
		vector<string> s(N);
		for( int i = 0; i < N; i++ ){
			fin >> s[i];
		}

		vector< vector<int> > all;
		vector<int> line;
		vector<char> chars;

		char last = s[0][0];
		chars.push_back(s[0][0]);
		int charnum = 0;
		for( int i = 0; i < s[0].size(); i++ ){
			if( s[0][i] != last ){
				chars.push_back(s[0][i]);
				line.push_back(charnum);
				charnum = 1;
				last = s[0][i];
			}else{
				charnum++;
			}
		}
		line.push_back(charnum);
		all.push_back(line);

		for( int j = 1; j < N; j++ ){
			line.clear();
			char last = s[j][0];
			if( last != chars[0] )
				goto FeglaWon;
			int charnum = 0;
			int charidx = 1;
			for( int i = 0; i < s[j].size(); i++ ){
				if( s[j][i] != last ){
					if( charidx >= chars.size() )
						goto FeglaWon;
					if( s[j][i] != chars[charidx] )
						goto FeglaWon;
					charidx++;
					line.push_back(charnum);
					charnum = 1;
					last = s[j][i];
				}else{
					charnum++;
				}
			}
			if( charidx < chars.size() )
				goto FeglaWon;
			line.push_back(charnum);
			all.push_back(line);
		}

		int ans = 0;
		for( int i = 0; i < chars.size(); i++ ){
			int lans1 = 0;
			int lans2 = 0;
			int n = 0;
			for( int j = 0; j < N; j++ ){
				n += all[j][i];
			}
			int cand1 = n/N;
			int cand2 = cand1+1;
			for( int j = 0; j < N; j++ ){
				lans1 += abs( cand1 - all[j][i] );
				lans2 += abs( cand2 - all[j][i] );
			}
			ans += min(lans1, lans2);
		}

	/////////////////////////////
		fprintf(fout,"Case #%d: %d\n", test_case, ans);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
		continue;

FeglaWon:
		fprintf(fout,"Case #%d: Fegla Won\n", test_case);

	}

	OUTPUTLOG( "program end" );
}