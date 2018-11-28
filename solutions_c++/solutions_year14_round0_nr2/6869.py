#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main(){
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	long T,i;
	double C,F,X,S,time;
	fin>>T;
	for (i=1;i<=T;i++){
		fin>>C>>F>>X;
		S=2;
		time=0;
		while (S<(X*F/C)-F){
			time+=C/S;
			S+=F;
		}
		time+=X/S;
		fout<<"Case #"<<i<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<time<<endl;
	}
	fin.close();
	fout.close();
}