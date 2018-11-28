#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main() {
	fstream fin("B-large.in",ios::in);
	fstream fout("B-large.out",ios::out);
	int T;
	fin>>T;
	int i;
	for(i = 1;i <= T;i++) {
		double C, F, X;
		fin>>C>>F>>X;
		double spead = 2.0;
		double minTime = X/spead;
		double buildNframTime = 0;
		
		while(true) {
			buildNframTime += C/spead;
			spead += F;
			double totalTime = buildNframTime + X/spead;
			if(totalTime < minTime) {
				minTime = totalTime;
			}
			else {
				break;
			}
		}


		fout<<"Case #"<<i<<": " <<fixed<<setprecision(7)<<minTime<<endl;

	}

	return 0;
}