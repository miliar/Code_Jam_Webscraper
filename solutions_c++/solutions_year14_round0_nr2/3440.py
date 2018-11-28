#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;

double solve(double c, double f, double x){
	double t0=x/2;
	double t=c/2+x/(2+f);
	double idx=2;
	while(t0>t){
		t0=t;
		t+=c/(2+(idx-1)*f);
		t-=x/(2+(idx-1)*f);
		t+=x/(2+idx*f);
		idx+=1;
	}
	return t0;
}
int main(){
	ifstream ifs("test.txt");
	ofstream ofs("b-large.out");
	int t;
	ifs>>t;
	for(int i=1; i<=t; i++){
		double c, f, x;
		ifs>>c>>f>>x;
		stringstream ss;
		ss<<"Case #"<<i<<": "<<to_string(solve(c, f, x))<<endl;
		cout<<ss.str();
		ofs<<ss.str();
	}
	return 0;
}