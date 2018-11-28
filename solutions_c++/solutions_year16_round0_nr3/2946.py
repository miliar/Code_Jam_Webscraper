#include<iostream>
#include<fstream>
#include <boost/multiprecision/random.hpp>
#include <boost/random.hpp>
#include<math.h>
#include <boost/multiprecision/cpp_int.hpp>
#include<boost/math/special_functions/pow.hpp>
#include<set>

#include<vector>

using namespace std;
using namespace boost::random;
using namespace boost::multiprecision;

#define NUMBER 16
#define JAMCOIN 50

vector< cpp_int > PRIME_NUMBERS;

bool temoin_miller_rabin(cpp_int a, cpp_int n) {

	int s = 0;
	cpp_int cpy = n-1;

	while(cpy % 2 == 0) {
		s++;
		cpy = cpy / 2;
	}

	cpp_int d = cpy;
	cpp_int x = powm(a,d,n);

	if(x == 1 || x == n-1) 
		return false;

	while(s > 1) {

		x = pow(x, 2) % n;
		if(x == n-1) 
			return false;
		s--;

	}

	return true;

}

bool miller_rabin(cpp_int n, int k) {

	int cpt = 0;
	while(cpt < k) {

		mt11213b base_gen(clock());
	        independent_bits_engine<mt11213b, 64, cpp_int> gen(base_gen);
	
		cpp_int a = gen() % (n - 2) + 2; 
	
		if(temoin_miller_rabin(a,n)) {
			return false;
		}
		
		cpt++;

	}

	return true;

}
 
cpp_int base_b(cpp_int N, int b) {

	int power = 0;
	cpp_int base = 0;

	while(N > 0) {

		base += (N%10) * (cpp_int)pow(b, power);
		power++;
		N = N/10;	

	}

	return base;
}

bool is_jamcoin(cpp_int J) {

        for(int i = 2; i < 11; i++) {

		cpp_int u = base_b(J, i);
                if(miller_rabin(u,40)) {

                        return false;

		}

        }

	return true;

}

bool get_witnesses(cpp_int J, cpp_int* temoins) {

	int cpt = 0;
	cpp_int bases[9] = {
		base_b(J,2),
		base_b(J,3),
		base_b(J,4),
		base_b(J,5),
		base_b(J,6),
		base_b(J,7),
		base_b(J,8),
		base_b(J,9),
		base_b(J,10)
	};

	bool done[9] = { false };

	while(cpt < 1000) {

		for(int i = 0; i < PRIME_NUMBERS.size(); i++) {

			for(int j = 0; j < 9; j++) {

				if(bases[j] % PRIME_NUMBERS[i] == 0 && !done[j]) {
		
					done[j] = true;		
					temoins[j] = PRIME_NUMBERS[i];

				}

			}

			cpt++;

		}

	}

	for(int i = 0; i < 9; i++) {

		if(done[i] == false)
			return false;

	}

	return true;

}

cpp_int try_jamcoin(int N) {

	mt11213b base_gen(clock());
        independent_bits_engine<mt11213b, 64, cpp_int> gen(base_gen);

	cpp_int n = 1;

        for(int i = 0; i < N; i++) {

        	cpp_int tmp = gen() % 2;
		n = n*10 + tmp;

	}

	n = n*10 + 1;

	return n;

}

void gen_jamcoins(int N, int J) {

	// Generation unique
	set<cpp_int> jamcoins;
	// TODO : utiliser des set pour les doublons
	while(jamcoins.size() < J) {

		cpp_int n = try_jamcoin(N);

		// Nouveau jamcoin trouve
		if(is_jamcoin(n) && jamcoins.find(n) == jamcoins.end()) {

			cpp_int* temoins = new cpp_int[9];
			if(get_witnesses(n, temoins)) {

				jamcoins.insert(n);
				cout << n << " ";
				for(int i = 0; i < 9; i++) 
					cout << temoins[i] << " ";

				cout << endl;

			}

		}

	}

}

int main(int argc, char** argv) {

	// TODO : crible
	for(int i = 3; i < 10000; i++) {

		if(miller_rabin(i, 5)) {
			PRIME_NUMBERS.push_back(i);
		}

	}

	gen_jamcoins(14, 50);

	return 0;

}
