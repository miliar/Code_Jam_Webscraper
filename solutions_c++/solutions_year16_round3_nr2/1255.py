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

typedef unsigned long int uint64;

uint64 M;
unsigned int B;

void processCase()
{
	cin >>B >> M;
	
	uint64 max_m = (1 << (B - 2));
	if( M > max_m) {
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("POSSIBLE\n");
	
	uint64 m = M;
	if( M == max_m) {
		printf("0");
		for(int i = 1; i < B; i++) {
			printf("1");
		}
	}
	else
	{
		for(unsigned int i = B; i != 0; i--) {
			printf( ((m & ( 1UL << (i -2 ))) != 0)? "1":"0");
		}
	}
	
	printf("\n");
	
	
	for(int i = 1; i < B; i++) {
		for(int j = 0; j < B; j++) {
			printf( i < j? "1":"0");
		}
		printf("\n");
	}
	
}

int main(int argc, const char * argv[])
{
	int T;
	streambuf	*cinbuf;
	ifstream	*in;
	
	srand((int)time(0));
	std::ios::sync_with_stdio(false);

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
	}
	
	if(bTestRun) {
		cin.rdbuf(cinbuf);   //reset to standard input again
	}
	
    return 0;
}
