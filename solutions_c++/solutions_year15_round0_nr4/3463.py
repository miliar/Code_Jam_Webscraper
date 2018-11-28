//============================================================================
// Name        : Ominous_Omino.cpp
// Author      : Yao Zhang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

bool omino(int X, int R, int C){
	if (X==1)
		return false;
	if(R==1 && C==1)
		return true;
	if(R==2 && C==2 && X==4)
		return true;
	if(R*C<X)
		return true;
	if((R==2 && C==4 && X==4) || (R==4 && C==2 && X==4))
		return true;
	if((R==1 && C==4 && X==4) || (R==4 && C==1 && X==4))
		return true;
	if((R==1 && C==3 && X==3) || (R==3 && C==1 && X==3))
			return true;
	if (R*C%X != 0){
		return true;
	}
	return false;
}

int main() {
	int total;
	ifstream infile("input.txt");
	ofstream SaveFile("output.txt");
	if (infile.is_open()){
		int X;
		int R;
		int C;
		infile>>total;
		for(int i=0; i<total; i++){
			infile>>X;
			cout<<"X="<<X<<" ";
			infile>>R;
			cout<<"R="<<R<<" ";
			infile>>C;
			cout<<"C="<<C<<" ";
			if(omino(X, R,C)){
				SaveFile<<"Case #"<<i+1<<": RICHARD"<<endl;
				cout<<"Case #"<<i+1<<": RICHARD"<<endl;
			}
			else{
				SaveFile<<"Case #"<<i+1<<": GABRIEL"<<endl;
				cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
			}
			cout<<endl;
		}
		infile.close();
		SaveFile.close();
	}
}
