#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
typedef unsigned char uchar;

#define ST 2

int main(int argc, char** argv) {
	ifstream inputFile("B-large.in");
	ofstream outputFile("b.out");
	outputFile << fixed << setprecision(7);

	if(inputFile.is_open() ) {
		unsigned int T;

		inputFile >> T;
		for(unsigned int i = 0; i < T; ++i) {
			double C, F, X;
			inputFile >> C >> F >> X;


			double sum = 0.0;
			double last = 0.0;
			int k = 0; // count oif Farms

			double time = X / ST; // without any Farms
			double timeF = time; // new time with additinal Farm

			do {
				time = timeF;
				sum += C / (ST + k * F);
				timeF = sum + X / (ST + (k + 1) * F);
				++k;
			} while(timeF < time);

			// ----------------------------------
			outputFile << "Case #" << i + 1 << ": "  << time << endl;
		}
	}

	inputFile.close();
	outputFile.close();
	return 0;
}
