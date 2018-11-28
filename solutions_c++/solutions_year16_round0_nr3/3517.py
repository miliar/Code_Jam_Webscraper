#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <list>
#include <bitset>

using namespace std;

#define OUT outFile

#define T  1
#define N  16
#define J  50

typedef unsigned long long u32;
map<u32, int> mapP;

bool isPrime(u32 n, u32 *factor) {

	if (n < 2) {
		*factor = 0;
		return false;
	}
	if (n % 2 == 0) {
		*factor = 2;
		return false;
	}
	u32 sq_n = (u32)sqrt(n);
	u32 k = 0;
	for (u32 k = 3; k <= sq_n; k += 2) {
		if (n % k == 0) {
			*factor = k;
			return false;
		}
	}
	return true;
}

int main() {

	ifstream inFile("in.txt");
	ofstream outFile("out.txt");

	u32 binary = pow(2, N - 1) + 1;
	u32 binary_end = pow(2, N) - 2;

	list<u32> outList;
	while (binary < binary_end) {
		
		bool valid = true;

		// convert binary to different base
		for (u32 base = 2; base <= 10; base++) {

			// get real value
			u32 value = 0;
			u32 bin = binary;
			u32 shift = 0;
			while (bin) {
				if (bin & 0x1) {
					value += pow(base, shift);
				}
				bin >>= 1;
				shift++;
			}

			// test if dandidate is in mapP
			if (mapP.find(value) != mapP.end()) {
				valid = false;
				break;
			}

			// check if it's prime
			u32 dummy;
			if (isPrime(value, &dummy)) {
				mapP[value] = 1;
				valid = false;
				break;
			}
		}

		if (valid) {
			outList.push_back(binary);
			if (outList.size() == J)
				goto done;
		}
		binary += 2;
	}
done:

	OUT << "Case #" << 1 << ":" << endl;
	for (list<u32>::iterator it = outList.begin(); it != outList.end(); it++) { 
		
		u32 binary = *it;
		u32 factors[9] = { 0 };

		for (u32 base = 2; base <= 10; base++) {

			// get real value
			u32 value = 0;
			u32 bin = binary;
			u32 shift = 0;
			while (bin) {
				if (bin & 0x1) {
					value += pow(base, shift);
				}
				bin >>= 1;
				shift++;
			}

			// get factors by checking isPrime
			if (isPrime(value, &factors[base-2])) {
				_ASSERT(0);
			}
		}

		OUT << bitset<N>(binary);
		for (int i = 0; i < 9; i++) {
			OUT << " " << factors[i];
		}
		OUT << endl;
	}

	return 0;
}