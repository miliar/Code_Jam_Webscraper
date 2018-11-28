#include <iostream>
#include <fstream>
using namespace std;

int main () {
	
	ifstream fin ("OvationIN.txt");
	ofstream fout ("OvationOUT.txt");
	
	int t;
	fin >> t;
	
	for (int i = 0; i < t; i++) {
		int x;
		fin >> x;
		x = x+1;
		char buff;
		fin >> buff;
		int buffer = buff-'0';
		int sumsofar = buffer;
		int added = 0;
		for (int j = 1; j < x; j++) {
			char b;
			fin >> b;
			int a = b-'0';
			if (a > 0 && j > sumsofar) {
				int add = (j-sumsofar);
				added += add;
				sumsofar+=add;
			}
			sumsofar+=a;
		}
		fout << "Case #" << (i+1) << ": " << added << "\n";
	}
}
