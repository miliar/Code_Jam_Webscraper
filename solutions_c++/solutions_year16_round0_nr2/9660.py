// Pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include<queue>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("output.out");

	//-- check if the files were opened successfully 
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;

	int cases = 0;
	fin >> cases;
	int times = 0;
	while (cases > 0)
	{
		bool isplusState;
		queue<char> cakeQue;
		string s;
		fin >> s;
		if (s[0] == '+') {
			isplusState = true;
		}
		else {
			isplusState = false;
		}
		cakeQue.push(s[0]);
		for (unsigned i = 1; i < s.size(); ++i) {
			if (s[i] == '+') {
				if(!isplusState)
					cakeQue.push(s[i]);
				isplusState = true;
			}
			else {
				if(isplusState)
					cakeQue.push(s[i]);
				isplusState = false;
			}
		}


		int count = 0;

		if (cakeQue.front() != '+') {
			count++;
		}
		cakeQue.pop();

		while (!cakeQue.empty()) {
			if (cakeQue.front() != '+') {
				count += 2;
			}
			cakeQue.pop();
		}
		

		times++;
		cases--;
		fout << "Case #" << times << ": " << count << endl;
	}
    return 0;
}

