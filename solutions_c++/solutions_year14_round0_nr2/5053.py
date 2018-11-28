#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("B-large.out");
	int nCases;
	infile >> nCases;
	double C, F, X;
	for (int i = 0; i < nCases; i++) {
		infile >> C >> F >> X;
		double curSpeed = 2.0;
		double totaltime = 0.0;
		while (1) {
			double time1 = X / curSpeed;
			double time2 = C / curSpeed + X / (curSpeed+F);
			if (time1 < time2) {
				totaltime += time1;
				break;
			}
			else {
				totaltime += C / curSpeed;
				curSpeed += F;
			}
		}
		outfile.precision(15);
		outfile << "Case #" << i+1 << ": ";
		outfile << totaltime << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}