#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int main() {
	ifstream inp("input.txt");
	ofstream outp("output.txt");

	int count;

	double C;
	double F;
	double X;

	int cookie;

	inp >> count;

	for (int i = 0; i < count; ++i) {
		int tmp = 0;
		double time = 0.0f;

		cookie = 0;

		inp.precision(6);
		inp >> C >> F >> X;

		tmp = ceil((X / C) - (2.0f / F + 1.0f));

		if (tmp > 0) {
			for (int j = 0; j < tmp; ++j) {
				time += C / (F * j + 2.0f);
			}
			time += X / (F * tmp + 2.0f);
		}
		else {
			time = X / 2.0f;
		}

		outp.setf(ios::fixed);
		outp.setf(ios::showpoint);
		outp.precision(6);
		outp << "Case #" << (i + 1) << ": " << time << endl;
	}

	return 0;
}