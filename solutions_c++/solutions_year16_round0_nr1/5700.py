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
	unsigned long int N;
	cin >> N;
	unsigned int R = 0;
	
	if( N == 0) {
		printf("INSOMNIA");
		return;
	}
	
	unsigned long int n = 0;
	
	while(R != 0x3FF) {
		n += N;
		unsigned long int t = n;
		while( t != 0) {
			unsigned char b = t % 10;
			R |= 1 << b;
			t /= 10;
		}
	}
	printf("%ld", n);
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
		printf("\n");
	}
	
	if(bTestRun) {
		cin.rdbuf(cinbuf);   //reset to standard input again
	}
	
    return 0;
}
