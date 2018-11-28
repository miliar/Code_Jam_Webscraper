#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("b.out");

double min(double a, double b) {
	if(a<b)
		return a;
	else
		return b;
}

double getTime(double C, double F, double X, int nFarms) {
	
	double rate = nFarms*F+2.0;
	double stopBuying = X/rate;
	double timeForNext = C/rate;

	double buyOneMore = timeForNext + X/((nFarms+1)*F+2.0);
	if(stopBuying<=buyOneMore)
		return stopBuying;
	else {
		double buyMore = getTime(C,F,X,nFarms+1) + C/rate;
		return min(stopBuying,buyMore);
	}

}

double getTime2(double C, double F, double X) {

	int nF=0;
	double waitTime = X;
	while(true) {

		double stopBuying = X/(2.0+nF*F);
		for(int i=0; i<nF; i++)
			stopBuying += C/(2.0+i*F);

		if(stopBuying<waitTime)
			waitTime = stopBuying;
		else
			break;

		nF++;

	}

	return waitTime;

}


int main() {

	int T; fin>>T;
	for(int t=1; t<=T; t++) {

		double C,F,X;
		fin >> C >> F >> X;
//		double time = getTime(C,F,X,0);
		double time = getTime2(C,F,X);
		fout << "Case #" << t << ": " << fixed << setprecision(7) << time << endl;

	}

	return 0;
}

