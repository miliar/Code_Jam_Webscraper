//============================================================================
// Name        : Brattleship.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt1.in");

void process(int t){
	int r,c,w;
	fin>>r>>c>>w;
	int total = r*(c%w==0 ? c/w : c/w+1)+(w-1);
	cout<<"Case #"<<t<<": "<<total<<endl;
}

int main() {
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
		process(i);
	return 0;
}
