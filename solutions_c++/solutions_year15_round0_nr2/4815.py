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
#include <queue>

using namespace std;

unsigned int primes[] = {
	2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
};

const bool bTestRun = false;

template <class T> void DumpObject(T t) { cout << t << endl; }

typedef vector<int> IntVector;
typedef pair<float, float> FP;
typedef vector<pair<float, float>> FPVector;
typedef std::priority_queue<unsigned int> Q;

Q P;
unsigned int Min;
unsigned int Ub;

// O(Ub!) ???

// m - number of splits already made
unsigned int optimal(Q& q, unsigned int m)
{
	unsigned int A = q.top(), r;
	r = A + m;
	if( A == 2) return r;
	if( m >= Ub) return r;
	
	q.pop();
	
	unsigned int A1 = A/2;
	for(int j = 2; j <= A1; j++) {
		Q qt = q;
			
		qt.push(j);
		qt.push(A - j);

		r = min(r, optimal( qt, m + 1));
	}
	
	return r;
}

void processCase()
{
	unsigned int D;
	P = Q();
	
	cin >> D;
	
	Min = 1000000;
	
	for(int i = 0; i < D; i++) {
		unsigned int Pi;
		cin >> Pi;
		P.push(Pi);
		
		Min = min(Min, Pi);
	}
	
	unsigned int R = P.top(); // upper bound
	Ub = R;
	
	R = optimal(P, 0);
/*
	for(int i = 1; i < Ub; i++) {

		unsigned int A;
		
		A = P.top();
		if(A == 1) break;
		P.pop();
		
		int k = 2;
		
		P.push(A / k);
		P.push( A - A/k);
		
		R = min(R, i + P.top());
		
		//		cout << A << " ";
	}
 */
	//	cout << endl << "RS: ";
	cout << R;
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
		// in = new ifstream("B-small-attempt0.in.txt");
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
