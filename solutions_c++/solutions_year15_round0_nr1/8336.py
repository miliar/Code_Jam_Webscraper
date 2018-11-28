/*
Input  
4
4 11111
1 09
5 110011
0 1

Output 
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
*/

#include <iostream>
#include <string>
#include <fstream>
using namespace std;


void main() {

	ifstream fin;
	fin.open("A-large.in");
	if( fin.fail()) {
		cout<<"input file opening failed"<<endl;
	}

	ofstream fout;
	fout.open("output.txt");
	if( fout.fail()) {
		cout<<"output file opening failed"<<endl;
	}


	int numTestCases=0;
	fin>>numTestCases;
	
	int curTestCase = 0;
	while( curTestCase< numTestCases) {
		int sMax = 0;
		string S;
		fin>>sMax;
		fin>>S;

		//s1
		int sumPeople = S.at(0)-'0';
		int pos = 1;
		
		int needPeople = 0;
		while( pos <= sMax ) {
		
			//curNeedPeople = pos;
			if( sumPeople < pos) {
				needPeople += pos-sumPeople;
				sumPeople = pos;
			}

			int numNewPeople = S.at(pos)-'0';
			sumPeople += numNewPeople;

			pos++;
		}

		//Case #1: 0
		fout<<"Case #"<<curTestCase+1<<": "<<needPeople<<endl;

		curTestCase++;
	}

	return;
}