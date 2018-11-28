//============================================================================
// Name        : Google.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
#define cin fin
#define cout fout
ifstream fin("in.in");
ofstream fout("out.out");

int main() {
	int T;
	double C, F, X;
	cin >> T;
	for(int i = 1; i <= T; i++){
		cin >> C >> F >> X;
		double sum = 0, f = 2.0;
		while(X / f > C / f + X/(f + F)){
			sum += C / f;
			f = f + F;
			//cout<< sum <<"---"<<f<<endl;
		}
		cout<<"Case #"<<i<<": ";
		cout<<fixed<<setprecision(7)<<sum + X / f << endl;
	}
}
