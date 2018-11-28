
#include <fstream>
#include <iostream>
#include <gmpxx.h>

using namespace std;

bool is_palindrom(mpz_class p) {
	string str = p.get_str();
	return str == string(str.rbegin(), str.rend());
}

long long solve(mpz_class a, mpz_class b) {
	long long i = 0;
	mpz_class c;
	for (;a <= b; a++) {
		if (is_palindrom(a) && mpz_perfect_square_p(a.get_mpz_t())) {
			mpz_sqrt(c.get_mpz_t(), a.get_mpz_t());
			if (is_palindrom(c)) {
				i++;
			}
		}
	}
	return i;
}

void palindrom(const char* filename) {
	int N;
	ifstream in(filename);
	in >> N;
	for (int i=0; i < N; i++) {
		mpz_class a, b;
		in >> a >> b;
		cout << "Case #" << (i+1) << ": " << solve(a, b) << endl;
	}
}


int main(int argc, char** argv) {
	palindrom(argv[1]);
	return 0;
}
