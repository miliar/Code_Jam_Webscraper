#include <cstdio>
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;


int main() {
	ifstream fin;
	fin.open("A-large.in", std::ios_base::in);
	ofstream myfile;
	myfile.open("a.out");
	int T, A, prob = 1;
	for (fin >> T; T--;) {
		fin >> A;
		int result = 0;
		int C = 0;
		char B[1000];
		fin >> B;
		for (int i = 0; i <= A; i++){
			int s = B[i]-'0';
			if (i <= C) {
				C = C + s;
			}
			else {
				int add = i-C;
				result = result + add;
				C = C + s + add;
			}
		}
		myfile << "Case #" << prob++ << ": " << result << endl;
	}
	myfile.close();
	fin.close();
	cin.get();
	return 0;
}