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
#include <queue>

using namespace std;

typedef vector<int64_t> IntVector;
typedef vector<string> StringVector;

bool bTestRun = false;

template <class T> void DumpObject(T t) { cout << t << endl; }

int x, y;

vector<char> s;

void processCase()
{
	cin >> x; cin >> y;

	int p = x > 0?1:-1;
	bool f = true;
	for(int i = 0; i < abs(x); i++)
	{
		if( f )
		{
			cout << ((p > 0)?"E":"W");
			f = false;
		}
		else
		{
			if( p > 0) cout << "WE";
			else cout << "EW";
		}
	}
	
	p = y > 0?1:-1;

	for(int i = 0; i < abs(y); i++)
	{
		if( f )
		{
			cout << ((p > 0)?"N":"S");
			f = false;
		}
		else
		{
			if( p > 0) cout << "SN";
			else cout << "NS";
		}
	}
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
