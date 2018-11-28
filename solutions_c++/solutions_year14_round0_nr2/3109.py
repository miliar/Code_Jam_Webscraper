#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int inputs;
	ifstream fin("B-large.in");
	ofstream fout("output.out");
	fin >> inputs;
	fout.precision(7);
	fout.setf(ios::fixed, ios::floatfield);
	for (int i = 0; i < inputs; i++) {
		double fcost, frate, goal, rate = 2.0, time = 0.0;
		fin >> fcost;
		fin >> frate;
		fin >> goal;

		while (goal / rate > fcost / rate + goal / (rate + frate)) {
			time += fcost / rate;
			rate += frate;
		}
		time += goal / rate;

		fout << "Case #" << i + 1 << ": " << time << endl;
	}
}