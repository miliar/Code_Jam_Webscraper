//============================================================================
// Name        : round0.cpp
// Author      : jadm
// Version     :
// Copyright   : 
// Description : Hello World in C, Ansi-style
//============================================================================


#include "utility.hpp"

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


	int T;

	READI(T, fi);

	int ssize = 65536;
	char* s = (char*)calloc(sizeof(char), ssize);


	int *numf = new int[10];
	for (int test = 0; test < T; test++) {
		// test
		if (test > 0)
			fprintf(fo, "\n");

		long long N;
		long long O;



		READI(N, fi);
		cout << "N: " << N << endl;

		sprintf(s, "%I64d", N);
		int slen = strlen(s);

		int ispow10 = 1;
		if (s[0] != '1')
			ispow10 = 0;
		FOR(i, 0, slen-1) {
			if (s[i] != '0')
				ispow10 = 0;
		}

		if ((ispow10 && slen > 1) || (slen == 1 && s[0] == '0')) {
			fprintf(fo, "Case #%d: INSOMNIA", test+1);
		}
		else {
			FOR(i, 0, 9) {
				numf[i] = 0;
			}

			int check_done = 0;
			int k = 1;
			long long kN = 0;

			while (check_done == 0) {
				kN += N;

				sprintf(s, "%I64d", kN);
				int slen = strlen(s);

				//cout <<"s:"<<s <<endl;

				FOR(i, 0, slen-1) {
					//cout <<"s[i]-'0':"<<s[i]-'0'<<endl;
					numf[s[i]-'0'] = 1;
				}

				check_done = 1;
				FOR(i, 0, 9) {
					if (numf[i] == 0)
						check_done = 0;
				}
			}

			O = kN;

			fprintf(fo, "Case #%d: %I64d", test+1, O);
		}




	}

	delete[] numf;



	////////////////////////////////////////////////////////////////////////

	delete[] fb;

	fclose(fo);
	fclose(fi);

	return 0;
}

