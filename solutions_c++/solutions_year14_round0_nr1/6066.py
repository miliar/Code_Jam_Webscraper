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


void processCase()
{
	int R1, R2;
	
	int G1[4][4], G2[4][4];
	set<int> s;
	
	int count = 0;
	int r = -1;
	
	cin >> R1;
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			cin >> G1[i][j];
			if( (i + 1) == R1) s.insert(G1[i][j]);
		}
	}
	
	cin >> R2;
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			cin >> G2[i][j];
			
			if((i + 1) == R2 ) {
				if(s.count(G2[i][j])) {
					count++;
					if(count == 1) r = G2[i][j];
				}
			}
		}
	}
	
	switch( count) {
		case 0: cout << "Volunteer cheated!";break;
		case 1: cout << r;break;
		default: cout << "Bad magician!";break;
	}
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
