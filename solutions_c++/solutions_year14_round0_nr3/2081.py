//
//  main.cpp
//
//
//  Created by dmp on 5/3/13.
//  Copyright (c) 2013 dmp. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <functional>   // std::greater

using namespace std;

const bool bTestRun = false;

template <class T> void DumpObject(T t) { cout << t << endl; }

typedef vector<int> IntVector;
typedef pair<float, float> FP;
typedef vector<pair<float, float>> FPVector;


#define kImpossible "\nImpossible"

int R, C, M;

char F[50][50];
void printF()
{
	for(int i = 0; i < R; i++) {
		cout << endl;
		for(int j = 0; j < C; j++) {
			cout << F[i][j];
		}
	}
	
	//	cout << endl; // !!!!
}

// size min 2x2
bool place(int rr, int cc, int m)
{
	bool b;
	
	if( m == 0) return true;
	
	if( (R - rr)* (C - cc) - 1 == m ) {
		for(int i = rr; i < R;i++) {
			for(int j = cc; j < C; j++)
				F[i][j] = '*';
		}
		
		F[R - 1][C - 1] = 'c';
		return true;
	}

	if( C - cc == 2 && R - rr == 2) {
		return false;
	}
	
	if(( R - rr > 2) && ( C - cc <=m))
	{
		for( int i = cc; i < C; i++) {
			F[rr][i] = '*';
		}
		//		printF();
		b = place(rr + 1, cc, m - (C - cc));
		if(b) return b;
		
		for( int i = cc; i < C; i++) {
			F[rr][i] = '.';
		}
	}
	
	if(( C - cc > 2) && ( R - rr <=m))
	{
		for( int i = rr; i < R; i++) {
			F[i][cc] = '*';
		}
		
		// printF();
		return place(rr, cc + 1, m - (R - rr));
	}

	if(( R - rr > 2))
	{
		int mm = min(m, C - cc - 2);
		for(int i = 0; i < mm; i++ ) {
			F[rr][cc + i] = '*';
		}
		m -= mm;
		if( m == 0) return true; //??
		rr++;
	}
	
	if( C - cc > 2) {
		int mm = min(m, R - rr - 2);
		for(int i = 0; i < mm; i++ ) {
			F[rr + i][cc] = '*';
		}
		m -= mm;
		if( m == 0) return true; //??
		
	}
	return false;
}


void processCase()
{
	
	cin >> R >> C >> M;
	
	// DEBUG!!!
	
	// cout << R << " " << C << " " << M << endl;
	
	// case 0 0 ≤ M < R * C.
	if( R * C <= M) {
		cout << kImpossible; return;
	}
	
	memset(F, '.', sizeof(F));
	
	F[R - 1][C - 1] = 'c';
	
	if( C == 1) {
		// case 1
		for( int i = 0; i < M; i++) F[i][0] = '*';
	}
	else if( R == 1) {
		// case 2
		for( int i = 0; i < M; i++) F[0][i] = '*';
	} else {
		
		// case 3 (most generic)
		bool result = place(0, 0, M);
		if(!result) {
			cout << kImpossible; return;
		}
		
	}

	printF();
}

int main(int argc, const char * argv[])
{
	int T;
	streambuf	*cinbuf;
	ifstream	*in;
	
	srand((int)time(0));

	if(bTestRun) {
		in = new ifstream("TestCase.in");
		cinbuf = std::cin.rdbuf(); //save old buf
		cin.rdbuf(in->rdbuf());
		cerr << "\n******: Using data from TestCase.in ******\n\n";
	}
	
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		processCase();
		printf("\n");
	}
	
	if(bTestRun) {
		cin.rdbuf(cinbuf);   //reset to standard input again
	}
	
    return 0;
}
