#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

bool needFarm(double perSec, double C, double F, double X)
{
	double cur = X / perSec;
	double add = C / perSec + X / (perSec + F);
	return add < cur;
}

int main() {
	ifstream infile("bIn.txt");
	ofstream outfile("bOut.txt", ios::app);
	outfile.precision(7);
	outfile.setf(ios::fixed, ios::floatfield);
	int cases;
	infile >> cases;
	int currentCase = 0;
	while(currentCase++ < cases) {
		double C, F, X;
		infile >> C >> F >> X;
		double perSec = 2.0;
		double secs = 0 ;
		while(needFarm(perSec, C, F, X)) {
			secs += C / perSec;
			perSec += F;
		}
		secs += X / perSec;
		outfile << "Case #" << currentCase << ": ";
		outfile << setprecision(7) << secs << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
