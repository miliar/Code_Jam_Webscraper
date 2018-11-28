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

bool notFit(int x, int r, int c){
	if(x>r&&x>c) return true; //long omino does not fit
	if(x>2*r||x>2*c) return true; //L-shape won't fit
	if((r*c)%x!=0) return true; //area not x-pavable


	return false;
}

string omino(int x, int r, int c){
	if(notFit(x,r,c)){
		return "RICHARD";
	}
	if(x>=7){ //possibility of piece containing a 1-square hole
		return "RICHARD";
	}
	if(x<=2){ //always fits provided area is a multiple of x
		return "GABRIEL";
	}
	if(x=4&&r*c==8){
		return "RICHARD";
	}
	return "GABRIEL";
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
		int x,r,c;
		cin>>x>>r>>c;
		//int res = standingOvation(s,r);
		string res = omino(x,r,c);
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	cin.rdbuf(cinbuf);//reset to standard input again
	cout.rdbuf(coutbuf);
	return 0;
}
