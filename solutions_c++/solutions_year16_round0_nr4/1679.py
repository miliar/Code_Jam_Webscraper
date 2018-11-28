//============================================================================
// Name        : round0c.cpp
// Author      : jadm
// Version     :
// Copyright   : 
// Description : Hello World in C, Ansi-style
//============================================================================


#include "utility.hpp"
#include <gmp.h>

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

	mpz_t t, a;
	mpz_init(t);
	mpz_init(a);

	for (int test = 0; test < T; test++) {
		// test
		if (test > 0)
			fprintf(fo, "\n");

		int K, C, S;
		READI(K, fi);
		READI(C, fi);
		READI(S, fi);

		cout << " K "<<K<<" C "<<C<<" S "<<S<<endl;

		if (C*S < K) {
			fprintf(fo, "Case #%d: IMPOSSIBLE", test+1);
		}
		else {
			fprintf(fo, "Case #%d:", test+1);
			FOR(i, 0, K-1) {
				fprintf(fo, " %d", i+1);
			}
			/*int Sp = ceil((double)K/(double)C); // real number of tiles needed <= S
			FOR(i, 0, Sp-1) {
				//int t = 0;
				mpz_set_ui(t, 0);
				FOR(k, 0, C-1) {
					//t += (i*C + ((C-1)-k))*((int)pow(K, k));
					mpz_set_ui(a, K);
					mpz_pow_ui(a, a, k);
					mpz_mul_ui(a, a, (i*C + ((C-1)-k)));
					mpz_add(t, t, a);
				}
				//fprintf(fo, " %d", t+1);
				fprintf(fo, " ");
				mpz_add_ui(t, t, 1);
				mpz_out_str(fo, 10, t);
			}*/

		}
	}


	////////////////////////////////////////////////////////////////////////

	delete[] fb;

	fclose(fo);
	fclose(fi);

	return 0;
}

