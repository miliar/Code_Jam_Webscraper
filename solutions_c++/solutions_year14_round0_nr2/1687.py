#include <iostream>
#include <fstream>
#include <set>
using namespace std;
int main() {
	int n;
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	fin >> n;
	for (int z = 0; z < n; z++) {
		double C, F, X;
		double rate = 2.0;
		double time = 0;
		double solution1, solution2;
		fin >> C >> F >> X;
		while (true) {
			solution1 = X / rate;
			solution2 = X / (rate + F) + C / rate;
			if (solution1 > solution2) {
				time += C / rate;
				rate += F;
			}
			else {
				time += solution1;
				break;
			}
		}
		fout.precision(7);
		fout << "Case #" << z+1 << fixed <<": ";
		fout << time;
		fout << endl;
	}
}