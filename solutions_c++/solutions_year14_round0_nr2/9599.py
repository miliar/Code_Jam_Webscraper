#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

ifstream fin ("Cookie.in");
ofstream fout ("Cookie.out");

int main(){	
	//lee numero de casos
	int T = 0;
	fin >> T;
	
	double c = 0, f = 0, x = 0;
	double ng = 0;
	const double cookpersec = 2;
	double gps = 0;
	
	for(int t=0; t<T; t++){
		fin >> c;
		fin >> f;
		fin >> x;
		
		gps=cookpersec;
		ng=0;
		double tiempo=0;
		if(x<=c){			
			tiempo = x/gps;
			fout.precision(7);
			fout << "Case #" << t+1 << ": " << tiempo << endl;
		}
		else {
			ng=(int)(x/c-cookpersec/f);
			for(int i=0; i<ng; i++){
				tiempo += c/(cookpersec+i*f);
			}
			tiempo+=x/(cookpersec+ng*f);
			fout.precision(15);
			fout << "Case #" << t+1 << ": " << tiempo << endl;			
		}
	}	

	return 0;
}
