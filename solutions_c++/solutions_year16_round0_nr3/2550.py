#include "mini-gmp.h"
#include <array>
#include <cstdlib>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
#include <iostream>

using namespace std;

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in >> T;
	for (int test = 1; test <= T; test++) {
		out << "Case #" << test << ":\n";
		int N, J;
		in >> N >> J;
		vector<pair<string, array<string, 9>>> coins;
		for (unsigned n = 0; (n < 1<<(N-2)) && (int)coins.size() < J; ++n) {
			char buffer[33];
			_itoa_s(2 * ((1 << (N - 2)) + n) + 1, buffer, 2);
			//cout << buffer << endl;
			mpz_t x;
			mpz_init(x);
			array<string, 9> divisor;
			int i;
			for (i = 2; i <= 10; ++i) {
				mpz_set_str(x, buffer, i);
				//cout << '\t' << mpz_get_str(nullptr, 10, x) <<endl;
				mpz_t sqrt;
				mpz_init(sqrt);
				mpz_sqrt(sqrt, x);
				mpz_t d;
				for (mpz_init_set_ui(d, 2); mpz_cmp(d, sqrt) <= 0; mpz_add_ui(d, d, 1)) {
					//cout << "\t\t" << mpz_get_str(nullptr, 10, d) << " ";
					mpz_t mod;
					mpz_init(mod);
					mpz_mod(mod, x, d);
					//cout << "\t\t" << mpz_get_str(nullptr, 10, mod) << endl;
					if (mpz_cmp_ui(mod, 0) == 0) {
						divisor[i - 2] = mpz_get_str(nullptr, 10, d);
						break;
					}
				}
				if (mpz_cmp(d, sqrt) > 0) {
					break;
				}
			}
			if (i > 10) {
				coins.push_back({ buffer,divisor });
				cout << coins.size() << endl;
			}
		}
		for (const auto& coin : coins) {
			out << coin.first;
			for (const string& s : coin.second) {
				out << " " << s;
			}
			out << endl;
		}
	}
	return 0;
}