#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

void name(int num, bool appear[], int& aCount) {
	while (num > 0) {
		int d = num % 10;
		if (!appear[d]) {
			appear[d] = true;
			aCount++;
			if (aCount == 10) return;
		}
		num /= 10;
	}
}

int getAns(int n) {
	bool appear[10] = {0};
	int aCount = 0;
	int num = n;
	do {
		name(num, appear, aCount);
		if (aCount == 10) {
			return num;
		}
		num += n;
	} while (true);
}

int main() {
	ifstream fin("A-large.in");
	assert(fin);
	ofstream fout("pa_large.out");
	assert(fout);
	int test;
	fin >> test;
	for (int cur = 1; cur <= test; cur++) {
		int n;
		fin >> n;
		fout << "Case #" << cur << ": ";
		if (n == 0) {
			fout << "INSOMNIA" << endl;
		} else {
			fout << getAns(n) << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}