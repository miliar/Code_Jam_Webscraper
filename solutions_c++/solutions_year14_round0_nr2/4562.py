#include <iostream>
#include <fstream>
using namespace std;

ifstream inFile;
ofstream outFile;

void compute(double c, double f, double x);

int main(int argc, const char* argv[]) {
	double c, f, x;
	int T;
	outFile.open("out.txt");
	outFile.precision(15);
	inFile.open(argv[1]);
	inFile >> T;
	for (int i = 1; i <= T; i++){
		outFile << "Case #" << i << ": ";
		inFile >> c >> f >> x;
		compute(c,f,x);
	}
	inFile.close();
	outFile.close();
	return 0;
}

void compute(double c, double f, double x) {
	double sum = x/2;
	double acct = 0;
	int n = 0;
	while (true) {
		acct += c/(2+n*f);
		n++;
		if (sum < acct+x/(2+n*f)) {
			outFile <<  sum << std::endl;
			return;
		}
		sum = acct+x/(2+n*f);
	}
}
