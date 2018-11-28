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

int N;
int S[27];
int Sm;
char F(int i)
{
	return 'A' + i;
}

void processCase()
{
	bool f = true;
	cin >> N;
	
	Sm = 0;
	for(int i =0; i < N; i++) {
		cin >> S[i];
		Sm += S[i];
	}

	char AA[3];
	AA[2] = 0;

	while(Sm > 0) {
		
		AA[1] = 0;
		
		int m = 0, mi = 0;
		for(int i =0; i < N; i++) {
			if(S[i] > m) {
				m = S[i];
				mi = i;
			}
		}
	
		AA[0] = F(mi);
		
		S[mi]--;
		Sm--;
	
		for(int i =0; i < N; i++) {
			if( 2*S[i] > Sm) {
				AA[1] = F(i);
				S[i]--;
				Sm--;
				break;
			}
		}
		
		if(!f) {
			f = false;
		}
		else {
			printf(" ");
		}
		
		printf("%s", AA);
		
		
		// Test
		for(int i =0; i < N; i++) {
			if( 2*S[i] > Sm) {
				printf("Test failed for index %d", i);
				break;
			}
		}

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
		printf("\n");
	}
	
	if(bTestRun) {
		cin.rdbuf(cinbuf);   //reset to standard input again
	}
	
    return 0;
}
