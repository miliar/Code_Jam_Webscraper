#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
	ifstream fin ("B-large.in");
	ofstream fout ("b.txt");
	int t;
	double c, f, x;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> c >> f >> x;
		double ti = 0, cur_rate = 2;
		while (1) {
			if (x / cur_rate < c / cur_rate + x / (cur_rate + f)) {
				ti += x / cur_rate;
				break;
			}
			else {
				ti += c / cur_rate;
				cur_rate += f;
			}
		}
		fout << setprecision(15) << "Case #" << i+1 << ": " << ti << "\n";
	}
}