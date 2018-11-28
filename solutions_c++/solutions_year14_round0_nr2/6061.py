#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int test_cases, tc;
int was[20];

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	fin >> test_cases;

	double C, F, X;

	for (tc = 1; tc <= test_cases; tc++) {	
		fin >> C >> F >> X;
		fout << "Case #" << tc << ": ";	

		double income = 2;		
		double time = 0;
		while (true) {
			if (X / income > (C / income) + (X / (income + F))) {				
				time += C / income;
				income += F;
			}
			else {
				time += X / income;
				break;
			}
		}

		fout << fixed << setprecision(7) << time << endl;
	}

	return 0;
}