#include <iostream>
#include <fstream>
#include <cmath>
#include <bitset>

#define staticmemeoryallocationsucks_test 16

using namespace std;

int T, N, J;

int validate(long long n, int base) {
	long long copy = n;
	int size = 0;
	long long num_based = 0;

	while(copy != 0) {
		num_based += (copy & 0x1) * pow(base, size++);
		copy = copy >> 1;
	}
	//cerr << "--" << num_based << " " << base;
	for(int i = 2; i <= sqrt(num_based); i++) {
		//cerr << "---" << i << endl;
		if(num_based % i == 0) return i;
	}
	return 0;
}

int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);

	cin >> T >> N >> J;
	cout << "Case #1:\n";

	long long frame = 0x1 << (N-1) | 0x1;
	//cerr << bitset<staticmemeoryallocationsucks_test>(frame) << endl;
	long long looper = 0x0;
	//cerr << bitset<staticmemeoryallocationsucks_test>(looper) << endl;
	for(int i = 0; i < J; i++) {
		int bases[11];
		bases[1] = 1;
		bases[10] = 0;
		while(looper < (0x1 << (N-2)) && bases[10] == 0) {
			for(int j = 2; j < 11 && bases[j-1] != 0; j++) {
				bases[j] = validate(frame | (looper << 1), j);
				//cerr << "-" << bitset<staticmemeoryallocationsucks_test>(frame | (looper << 1)) << " " << bases[j] << endl;
			}
			looper++;
		}
		cout << bitset<staticmemeoryallocationsucks_test>(frame | ((looper-1) << 1));
		for(int j = 2; j < 11; j++) cout << " " << bases[j];
		cout << endl;
	}

	return 0;
}