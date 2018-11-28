/*
 * main.cpp
 *
 *  Created on: 2013-04-13
 *      Author: ronanrmo
 */

#include <iostream>
#include <fstream>
#include <string.h>
#include <map>
#include <vector>
#include <cmath>
#include <list>
#include <string>
#include <sstream>
#include <limits>

using namespace std;

int **alloc2D(int N, int M){
	int **l = new int*[N];
	for(int n=0; n<N; n++){
		l[n] = new int[M];
	}
	return l;
}

void dealloc2D(int **l, int N){
	for(int n = 0; n < N; n++){
		if(l[n] != 0)
			delete [] l[n];
	}
	if(l != 0)
		delete[] l;
}



string check(int **lawn, int N, int M){
	int mxr[N], mnr[N];
	int mxc[M], mnc[M];

	// getting max and min for each row
	for(int i=0; i<N; i++){
		int max = numeric_limits<int>::min();
		int min = numeric_limits<int>::max();

		for(int j=0; j<M; j++){
			if(lawn[i][j] > max) max = lawn[i][j];
			if(lawn[i][j] < min) min = lawn[i][j];
		}
		mxr[i] = max;
		mnr[i] = min;
	}

	// getting max and min for each column
	for(int j=0; j<M; j++){
		int max = numeric_limits<int>::min();
		int min = numeric_limits<int>::max();

		for(int i=0; i<N; i++){
			if(lawn[i][j] > max) max = lawn[i][j];
			if(lawn[i][j] < min) min = lawn[i][j];
		}
		mxc[j] = max;
		mnc[j] = min;
	}


	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			if(lawn[i][j] == mnr[i] && lawn[i][j] != mxr[i] &&
			   lawn[i][j] == mnc[j] && lawn[i][j] != mxc[j])
				return string("NO");
		}
	}


	return string("YES");
}

int main(int argc, char **argv)
{
	istream &in  = (argc>1)?*(new ifstream(argv[1])):cin;
	ostream &out = (argc>2)?*(new ofstream(argv[2])):cout;

	int T;
	in >> T;

	for(int t=0; t<T; t++){
		int N, M;

		in >> N >> M;

		int **lawn = alloc2D(N,M);
		for(int n=0; n<N; n++){
			for(int m=0; m<M; m++){
				in >> lawn[n][m];
			}
		}

		string res = check(lawn, N, M);

		out << "Case #" << t+1 << ": " << res << endl;
		dealloc2D(lawn, N);
	}

	return 0;
}



