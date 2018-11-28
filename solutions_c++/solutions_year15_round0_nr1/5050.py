#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");
	
	int T;
	fin >> T;
	
	for (int i = 1; i <= T; i++) {
		int Smax = 0;
		string shyness;
		fin >> Smax;
		fin >> shyness;
		
		int cnt = shyness[0] - '0';
		int add = 0;
		for (int j = 1; j <= Smax; j++) {
			if (cnt >= j) {
				cnt += shyness[j] - '0';
			}
			else {
				add += j - cnt;
				cnt += j - cnt + shyness[j] - '0';
			}
		}
		fout << "Case #" << i << ": " << add << endl;
	}
	
	return 0;
}
