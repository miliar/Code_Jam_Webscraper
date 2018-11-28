#include <bitset>
#include <cmath>
#include <iostream>
#include <map>
#include <random>
#include <vector>
#define MAX_PRIME 100000001
using namespace std;

bool isPrime[MAX_PRIME];
vector<int> primeList;

void sieve() {
	memset(isPrime, true, sizeof(isPrime));
	primeList.clear();

	isPrime[0] = isPrime[1] = false;
	for (int p = 2; p < MAX_PRIME; p++) {
		if (isPrime[p]) {
			primeList.push_back(p);

			for (int i = p * 2; i < MAX_PRIME; i += p) {
				isPrime[i] = false;
			}
		}
	}
}

uint64_t tobase(uint32_t bits, int base) {
	uint64_t result = 0;
	uint64_t mult = 1;

	for (int b = 0; b != 32; b++) {
		result += bits & (1 << b) ? mult : 0;
		mult *= base; 
	}

	return result;
}

pair<bool, int> isPrimeWithProof(uint64_t n) {
	int sqrtn = sqrt(n) + 1;

	for (int i = 0; i < primeList.size() && primeList[i] <= sqrtn; i++) {
		if (n % primeList[i] == 0) {
			return pair<bool, int>(false, primeList[i]);
		}
	}

	return pair<bool, int>(true, n);
}

map<int, vector<int>> solve(int n, int j) {
	random_device rd;
	mt19937 mt(rd());
	uniform_int_distribution<uint32_t> dist;
	map<int, vector<int>> jamcoins;

	for (int i = 0; i < j; i++) {
		uint32_t jamcoin = (dist(mt) % 0x8000) | 0x8000 | 0x1;
		vector<int> proofs;
		bool isJamcoin = true;

		if (jamcoins.find(jamcoin) != jamcoins.end()) {
			i--;
			continue;
		}

		for (int b = 2; b <= 10; b++) {
			uint64_t inBaseB = tobase(jamcoin, b);
			pair<bool, int> isPrimeWithProofResult = isPrimeWithProof(inBaseB);

			if (isPrimeWithProofResult.first) {
				isJamcoin = false;
				break;
			} else {
				proofs.push_back(isPrimeWithProofResult.second);
			}
		}

		if (isJamcoin) {
			jamcoins[jamcoin] = proofs;
		} else {
			i--;
			continue;
		}
	}

	return jamcoins;
}

int main(void) {
	sieve();

	map<int, vector<int>> jamcoins = solve(16, 50);

	cout << "Case #1:" << endl;
	for (auto const &kv : jamcoins) {
		cout << bitset<16>(kv.first).to_string();
		for (auto const &v : kv.second) {
			cout << " " << v;
		}
		cout << endl;
	}
}