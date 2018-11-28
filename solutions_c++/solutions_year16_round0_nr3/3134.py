#include <fstream>
#include <vector>
#include <iostream>
#include <iomanip>
#include <bitset>

typedef unsigned long long int ubignum;

using namespace std;

vector<bool> primes;

void esieve(ubignum l){
	primes = vector<bool>(l + 1, true);
	primes[0] = false;
	primes[1] = false;
	for (int i = 2; i <= sqrt(l); i++){
		if (primes[i] == true){
			for (int n = i + i; n <= l; n += i){
				primes[n] = false;
			}
		}
	}
}

ubignum evaluateInBase(ubignum n,int base){
	int inc = 0;
	ubignum total = 0;
	while (n != 0){
		int lsb = n & 1;
		total = total + (lsb*(ubignum)pow(base, inc));
		n >>= 1;
		inc++;
	}
	return total;
}


int main(){
	const int N = 16;
	int J = 50;

	int total = 0;
	esieve(pow(10,8));

	ofstream fout("C-output.txt");

	fout << "Case #1:\n";

	for (ubignum n = (ubignum)pow(2, N - 1) + 1; n <= pow(2, N) - 1; n += 2){
		bool success;
		vector<int> proofs;
		for (int base = 2; base <= 10; base++){
			success = false;
			ubignum v = evaluateInBase(n, base);
			for (int div = 2; div <= ceil(sqrt(v)); div++){
				if (primes[div] && v % div == 0){
					success = true;
					proofs.push_back(div);
					break;
				}
			}
			if (!success){
				break;
			}
		}
		if (success){
			total++;
			bitset<N> x(n);
			fout << x;
			for (auto& it : proofs){
				fout << " " << it;
			}
			fout << endl;
			if (total >= J){
				break;
			}
		}
	}
}