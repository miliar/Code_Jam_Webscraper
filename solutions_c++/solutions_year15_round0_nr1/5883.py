//============================================================================
// Name        : CodeJam.cpp
// Author      : Chantal Ding
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int standingOvation(int smax, string repartition){
	int up=0;
	int need=0;
	for(int i=0;i<=smax;i++){
		int n=repartition[i]-'0'; //nb of people at shyness i
		int iNeed = i-up;
		if(n*iNeed>0){
			need+=iNeed;
			up+=iNeed;
		}
		up+=n;
	}
	return need;
}

int main(int argc, char* argv[]) {
	ifstream in(argv[1]);
	streambuf * cinbuf = cin.rdbuf();//save old buf
	cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	ofstream out(argv[2]);
	streambuf * coutbuf = cout.rdbuf();
	cout.rdbuf(out.rdbuf());

	int testCases;
	cin>>testCases;
	for(int i=0;i<testCases;i++){
		int s;
		string r;
		cin>>s>>r;
		int res = standingOvation(s,r);
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	cin.rdbuf(cinbuf);//reset to standard input again
	cout.rdbuf(coutbuf);
	return 0;
}
