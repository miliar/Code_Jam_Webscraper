#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int main(int argc, char** argv) {

	if (argc < 2) {
		cerr << "Usage: " << argv[0] << " input";
	}
	ifstream fin(argv[1]);
	
	int ntests;
	fin >> ntests;
	for(int cs = 1; cs <= ntests; cs++) {
		int smax;
		char str[1024];
		fin >> smax >> str;
		
		// Solve the problem
		int nadd = 0;
		int nstand = 0;
		for(int s = 0; s <= smax; s++) {
			if (s > nstand) {
				nadd += s - nstand;
				nstand = s;
			}
			nstand += int(str[s]-'0');
			cerr << "Case #" << cs << ": " << s << " " << nstand << " " << nadd << endl;
		}
		
		cout << "Case #" << cs << ": " << nadd << endl;
	}
	
	return 0;
}