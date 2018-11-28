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

	char* jcs = new char[100];
	char* interps = new char[100];

	mpz_t jc, numb, sqnumb, numd;
	mpz_init(jc);
	mpz_init(numb);
	mpz_init(sqnumb);
	mpz_init(numd);

	mpz_t *divs = new mpz_t[20];
	FOR(i,0,19){
		mpz_init(divs[i]);
		mpz_set_ui(divs[i], 0);
	}

	for (int test = 0; test < T; test++) {
		// test
		if (test > 0)
			fprintf(fo, "\n");

		int N;
		READI(N, fi);
		int J;
		READI(J, fi);

		int j = 0;

		cout << "N " << N << " J " << J << endl;

		FOR(i, 0, N-1){
			jcs[i] = '0';
		}
		jcs[0] = '1';
		jcs[N-1] = '1';
		jcs[N] = '\0';

		fprintf(fo, "Case #%d:", test+1);
		//exit(0);

		FOR(d, 0, (1<<(N-2))-1) { // 2^(N-2)
			FOR(i,0,N-3) {
				if((d/(1<<i))%2)
					jcs[i+1] = '1';
				else
					jcs[i+1] = '0';
			}

			mpz_set_str(jc, jcs, 10);
			cout << "tested:"; mpz_out_str(stdout, 10, jc); cout << endl;

			int isjamcoin = 1;

			FOR(b, 2, 10) {
				if (isjamcoin) {
					mpz_set_str(numb, jcs, b);
					mpz_get_str(interps, 10, numb);
					//cout << "base " << b << " " << interps << endl;

					//mpz_sqrt(sqnumb, numb);
					mpz_set_ui(sqnumb, 100);
					mpz_set_ui(numd, 2);

					int prime = 0;
					int firsttime = 1;
					while (1) {
						if (mpz_divisible_p(numb, numd)) {
							break;
						}
						//mpz_nextprime(numd, numd);
						if (firsttime) {
							mpz_set_ui(numd, 3);
							firsttime = 0;
						}
						else
							mpz_add_ui(numd, numd, 2);
						if (mpz_cmp(numd, sqnumb) > 0) {
							isjamcoin = 0;//number is prime stop
							break;
						}
					}

					mpz_set(divs[b], numd);

				}
			}

			if (isjamcoin) {
				j++;
				cout << "jamcoin" << endl;
				fprintf(fo, "\n");
				fprintf(fo, "%s", jcs);

				FOR(b,2,10) {
					mpz_get_str(interps, 10, divs[b]);
					fprintf(fo, " %s", interps);
					//printf(" %s", interps);
				}

				/*FOR(b,2,10) { for checking
					mpz_set_str(numb, jcs, b);
					mpz_get_str(interps, 10, numb);
					fprintf(fo, " %s", interps);
					//printf(" %s", interps);
				}*/
			}

			if (j >= J) {
				break;
			}

		}


	}


	////////////////////////////////////////////////////////////////////////

	delete[] fb;

	fclose(fo);
	fclose(fi);

	return 0;
}

