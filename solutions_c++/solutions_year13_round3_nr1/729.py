//
//  main.cpp
//  Template for CodeJam
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

using namespace std;

typedef vector<int64_t> IntVector;
typedef vector<string> StringVector;

bool bTestRun = false;

template <class T> void DumpObject(T t) { cout << t << endl; }

const char* vw = "aeiou";

bool c(char ch) { return strchr(vw, ch) == NULL; }

void processCase()
{
	string	s;
	int		n;
	
	cin >> s;
	cin >> n;
	
	int L = (int)s.length();
	int sq = 0;
	int64_t r  = 0;

	int m = 0;
	for( int i = 0; i < L; i++)
	{
		if(!c(s[i])) { sq = 0; continue; }
		sq++;
		
		if( sq >= n)
		{
			r += (int64_t)((int64_t)i + 2 - n - m)*(L - (int64_t)i);
			m = i + 2 - n;
		}
	}
	
	cout << r;
}

int main(int argc, const char * argv[])
{
	int T;
	ifstream	*in;
	streambuf	*cinbuf;
	
	if(bTestRun) {
		in = new ifstream("TestCase.in");
		cinbuf = std::cin.rdbuf(); //save old buf
		cin.rdbuf(in->rdbuf()); //redirect std::cin to in.txt!
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
