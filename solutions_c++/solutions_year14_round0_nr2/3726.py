#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int cases;
	double T;
	double c, f, x;
	double rate;

	fin >> cases;
	for(int i = 0; i < cases; ++i) {
		T = 0.0;
		rate = 2.0;
		fin >> c >> f >> x;
		while(x/rate > x/(rate+f)+c/rate) {
			T += c/rate;
			rate += f;
		}
		T += x/rate;
		fout << "Case #" << i+1 << ": " << fixed << setprecision(7) << T << endl;
	}
	fin.close();
	fout.close();
}