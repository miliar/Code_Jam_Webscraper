#include <iostream>
#include <fstream>
using namespace std;
int main() {
	ifstream fin;
	ofstream fout;

	fin.open("B-small-attempt0.in");
	fout.open("B-small-attempt0.out");

	int Test;
	fin >> Test;
	for (int TestCase = 1; TestCase <= Test; TestCase++) {
		int A, B, K;
		fin >> A >> B >> K;

		int res = 0;
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				int x = i & j;
				if (x < K) res++;
			}
		}
		fout << "Case #" << TestCase << ": " << res << endl;
	}
}