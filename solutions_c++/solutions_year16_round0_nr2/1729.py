//============================================================================
// Name        : round0b.cpp
// Author      : jadm
// Version     :
// Copyright   : 
// Description : Hello World in C, Ansi-style
//============================================================================


#include "utility.hpp"


char* ts;

void op(char* s, int c) {
	FOR(i,0,c-1) {
		ts[i] = s[c-i-1];
		if (ts[i] == '+')
			ts[i] = '-';
		else
			ts[i] = '+';
	}
	FOR(i,0,c-1) {
		s[i] = ts[i];
	}
	cout << "op:" << s << endl;
}


int main(int argc, char** argv) {
	cout << "=== " << argv[0] << " ===" << endl;

	char* fi_name = "input.txt";
	char* fo_name = "output.txt";

	FILE* fi = fopen(fi_name, "r");
	if (fi == NULL) {
		cerr << "could not open " << fi_name << endl;
		return -1;
	}
	FILE* fo = fopen(fo_name, "w");
	if (fo == NULL) {
		cerr << "could not open " << fo_name << endl;
		return -1;
	}

	int fbsize = 65536;
	char* fb = new char[fbsize]; // small buffer to parse words with scanf

	////////////////////////////////////////////////////////////////////////

	ts = new char[65536];

	int T;

	READI(T, fi);

	int ssize = 65536;
	char* s = (char*)calloc(sizeof(char), ssize);


	for (int test = 0; test < T; test++) {
		// test
		if (test > 0)
			fprintf(fo, "\n");

		fscanf(fi, "%s", s);

		cout << s << endl;

		int c, l;

		l = strlen(s);
		int nop = 0;

		int j = l-1;
		while (j >= 0) {
			if (s[j] == '-') {
				int k = j;
				if (s[0] == '+') {
					while (s[k] == '-')
						k--;
					op(s, k+1); nop++;
				}
				op(s, j+1); nop++;
			}
			j--;
		}

		fprintf(fo, "Case #%d: %d", test+1, nop);

	}


	////////////////////////////////////////////////////////////////////////

	delete[] fb;

	fclose(fo);
	fclose(fi);

	return 0;
}

