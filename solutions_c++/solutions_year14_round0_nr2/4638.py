#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

int main(){

	// Decleration
	ofstream fout ("cookie.out");
	ifstream fin ("cookie.in");

	fout.precision(7);

	int T;
	double C, F, X, time, produce;

	fin >> T;
	for (int q = 0; q < T; q++){
		// farm costs
		fin >> C;
		// farm money
		fin >> F;
		// goal
		fin >> X;

		time = 0;
		produce = 2;

		while(X / produce > C / produce + X / (produce + F)){
			time += C / produce;
			produce += F;
		}
		time += X / produce;


		fout << "Case #" << q + 1 << ": " << setprecision(7) << time << "\n";

	}

	return 0;
}