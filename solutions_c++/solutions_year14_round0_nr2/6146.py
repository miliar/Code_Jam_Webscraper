#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


int main() {

	ifstream fin("btxt.in");
	ofstream fout("btxt.out");
	int testcases;
	double C, F, X;
	fin >> testcases;
	for (int t=0; t<testcases; ++t) {
		fout << "Case #" << t + 1 << ": ";
		fin >> C >> F >> X;
		int nFarms = 0;
		double time_elapse = 0.0;
		while (true) {
			double choice1 = X / (nFarms * F + 2);
			double choice2 = C / (nFarms * F + 2) + X / ((nFarms + 1) * F + 2);
			if (choice1 < choice2) {
				time_elapse += choice1;
				break;
			} else {
				time_elapse += C / (nFarms * F + 2);
				++nFarms;
			}
		}
		fout << std::fixed << std::setprecision(7) << time_elapse << endl;
	}

	return 0;
}