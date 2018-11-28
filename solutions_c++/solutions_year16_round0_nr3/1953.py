#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>
#include <cmath>
#include <bitset>

using namespace std;

int main() {
	int Ncase;
	cin >> Ncase;
	ostringstream output;
	output << "Case #1:" << endl;
	int N, J;
	cin >> N >> J;
	int64_t pmax = pow(2,16);
	vector<bool> p(pmax,true);
	vector<int64_t> plist;
	for(int64_t i = 2; i < pmax; ++i) {
		if (!p[i]) continue;
		plist.push_back(i);
		int64_t m = 2 * i;
		while (m < pmax) {
			p[m] = false;
			m = m + i;
		}
	}
	// generate key
	int64_t maxbitset = pow(2,N-1);
	int64_t minbitset = pow(2,N-2) + pow(2,N/2-1);
	for (int64_t ibits = minbitset; ibits < maxbitset; ++ibits) {
		int64_t ibitstmp = (ibits << 1) + 1;
		bitset<32> bits (ibitstmp);
		vector<int64_t> basesupr(9,0);
		vector<int64_t> baseslwr(9,0);
		vector<int64_t> divisor(9,0);

		for (int i = 0; i < N; ++i) {
			if (i < N/2) {
				for (int j = 0; j < baseslwr.size(); ++j) baseslwr[j] += bits[i] * pow(j+2,i);
			} else {
				for (int j = 0; j < basesupr.size(); ++j) basesupr[j] += bits[i] * pow(j+2,i-N/2);
			}
		}
		bool isprime;
		for (int i = 0; i < baseslwr.size(); ++i) {
			isprime = true;
			for (auto prime : plist) {
				if (prime > baseslwr[i] || prime > basesupr[i]) {
					// skip if not above case, hope there's redundancy
					break;
				}
				if (baseslwr[i] != prime && baseslwr[i] % prime == 0 && basesupr[i] % prime == 0) {
					isprime = false;
					divisor[i] = prime;
					//cout << "got here" << endl;
					break;
				}
				//cout << "got here" << endl;
			}
			if (isprime) break;
		}
		if (!isprime) {
			for (int i = N; i > 0; --i) {
				output << bits[i-1];
			}
			for (auto d : divisor) {
				output << " " << d;			
			}
			output << endl;
			--J;
			if (J == 0) break;
		}
	}
	cout << output.str();
	return 0;
}
