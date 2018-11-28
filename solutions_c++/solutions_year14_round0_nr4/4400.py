#include <iostream>
#include <fstream>
using namespace std;

ifstream inFile;
ofstream outFile;

void compute(double* a, double* b, int N);
void sort(double* a, int N);
int main(int argc, const char* argv[]) {
	double a[1000];
	double b[1000];
	int N;
	int T;
	outFile.open("out.txt");
	inFile.open(argv[1]);
	inFile >> T;
	for (int i = 1; i <= T; i++) {
		outFile << "Case #" << i << ": ";
		inFile >> N;
		for (int j = 0; j < N; j++)
			inFile >> a[j];
		for (int j = 0; j < N; j++)
			inFile >> b[j];
		sort(a, N);
		sort(b, N);
		compute(a, b, N);
	}
	inFile.close();
	outFile.close();
	return 0;
}

void sort(double* a, int N) {
	double tmp;
	for (int i = 0; i < N; i++)
	for (int j = i+1; j < N; j++)
	if (a[i] > a[j]) {
		tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}
}

void compute(double* a,double* b, int N) {
	int r = 0;
	int l = 0;
	int h = N-1;
	for (int i = 0; i < N; i++) {
		if (a[i] > b[l]) {
			++r;
			++l;
			continue;
		}
		else {
			--h;
			continue;
		}
	}

	int s = 0;
	int pos = 0;
	for (int i = 0; i < N; i++) {
		bool getValue = false;
		while (pos < N) {
			if (b[pos] > a[i]) {
				pos++;
				getValue = true;
				break;
			}
			pos++;
			if (pos >= N)
				break;
		}
		if (getValue) continue;
	 	if (pos >= N) {
			s = N-i;
			break;
		}
	}
	outFile << r << " " << s << std::endl;
}
