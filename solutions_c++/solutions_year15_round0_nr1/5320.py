#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int t;
char d[10000];

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	
	fin >> t;

	int c=1;
	for (; t>0; t--) {
		int s=0;
		int r=0;
		int a;
		fin >> s >> d;	s=0;
		int l = strlen(d);
		for (int i=0; i<l; i++) {
			int v = d[i]-'0';
			if (s<i) {
				a=i-s;
				s+=a;
				r+=a;
			}
			s+=v;
		}
		fout << "Case #" << c++ << ": " << r << "\n";
	}

	fin.close();
	fout.close();
}

