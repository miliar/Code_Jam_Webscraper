#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
double calInkUsed(long long r,long long bigR) {
	return bigR*bigR - r*r;
}
int main() {
	int num_cases;
	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
	in >> num_cases;
	long long r,t;
	long long rsf,nbr;
	double ink ;
	int i=1;
	while(in >> r>> t) {
		
		//white r cm, black 1
		rsf =r;
		ink = t;
		nbr=0;
		while(true) {
			
			t -=calInkUsed(rsf,rsf+1);
			if(t<0) break;
			rsf+=2;
			nbr++;
		}
		out <<"Case #" << i++<<": " << nbr <<endl;
	}
	return 0;
}
