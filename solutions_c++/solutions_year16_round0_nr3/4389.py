#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

unsigned long toBase10(unsigned long num, unsigned long from, unsigned long len) {
	unsigned long res = 0;
	unsigned long aux = num;
	unsigned long multiplier = 1;
	for (unsigned long i = 0; aux != 0 && i < len; i++) {
		if ((aux & 1) == 1) {
			res += multiplier;
		}
		aux = aux >> 1;
		multiplier *= from;
	}
	return res;
}

unsigned long isPrime(unsigned long num) {
	unsigned long divNum = 0;
	for (unsigned long i = 1; i <= sqrt(num); i++) {
		if (num % i == 0) {
			divNum++;
		}
		if (divNum == 3) {
			return i;
		}
	}
	return 0;
}

int main(int argc, char **argv) {
	unsigned long T, N, J;
	fstream fin(argv[1]);
	vector<unsigned long> proofs(9, 0);
	fin >> T;
	for (unsigned long i = 0; i < T; i++) {
		fin >> N >> J;
		bitset<32> bits;
		unsigned long firstBit = 1;
		unsigned long lastBit = 1;
		lastBit = lastBit << (N - 1);
		unsigned long j = firstBit | lastBit;
		//cout << j << endl;
		cout << "Case #" << i + 1 << ": " << endl;
		unsigned long numFinished = 0;
		for (; numFinished < J && ((j & lastBit) == lastBit && (j & firstBit) == firstBit); j+=2) {
			unsigned long notPrimesNum = 0;
			for (unsigned long k = 2; k < 11; k++) {
				unsigned long num = toBase10(j, k, N);
				unsigned long proof = isPrime(num);
				if (proof > 1) {
					proofs[notPrimesNum] = proof;
					//cout << num << endl;
					notPrimesNum++;
				}
			}
			if (notPrimesNum == 9) {
				string bitstr = bitset<32>(j).to_string();
				bitstr = string(bitstr.begin()+(32-N), bitstr.end());
				cout << bitstr;
				for (unsigned long k = 0; k < 9; k++) {
					cout << " " << proofs[k];
					proofs[k] = 0;
				}
				cout << endl;
				numFinished++;
				//cout << numFinished << endl;
			}
		}
	}
	return 0;
}