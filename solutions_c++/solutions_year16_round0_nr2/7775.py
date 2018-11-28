//============================================================================
// Name        : codejam2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream oku("B-large.in",ios::in);
	ofstream yaz("cikti.out",ios::out);
	int i,t=0,top,T;
	string st;
	oku>>T;
	while(++t<=T) {
		oku>>st;
		top=0;
		for(i=0;st[i+1];i++)
			if(st[i]!=st[i+1]) top++;
		if(st[i]=='-') top++;
		yaz<<"Case #"<<t<<": "<<top<<endl;
	}
	return 0;
}
