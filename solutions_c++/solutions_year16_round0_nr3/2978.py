#include <iostream>
#include <bitset>
#include <string>
#include <cmath>

using namespace std;

long divisor(long n) {
	long limit = sqrt(n);
	for (long i=2;i<limit;++i) {
		if (!(n%i)) {
			return i;
		}
	}
	return -1;
}

int main() {
	int T, N, J;
	cin >> T >> N >> J;
	cout << "Case #" << T  << ":" << endl;
	long number = (1 << (N-1))+1;
	int count = 0;
	while (count < J) {
		string nstr = bitset<16>(number).to_string();
		number += 2;
		long div2 = divisor(stol(nstr,nullptr,2));
		if (div2 == -1) {
			continue;
		}
		long div3 = divisor(stol(nstr,nullptr,3));
		if (div3 == -1) {
			continue;
		}
		long div4 = divisor(stol(nstr,nullptr,4));
		if (div4 == -1) {
			continue;
		}
		long div5 = divisor(stol(nstr,nullptr,5));
		if (div5 == -1) {
			continue;
		}
		long div6 = divisor(stol(nstr,nullptr,6));
		if (div6 == -1) {
			continue;
		}
		long div7 = divisor(stol(nstr,nullptr,7));
		if (div7 == -1) {
			continue;
		}
		long div8 = divisor(stol(nstr,nullptr,8));
		if (div8 == -1) {
			continue;
		}
		long div9 = divisor(stol(nstr,nullptr,9));
		if (div9 == -1) {
			continue;
		}
		long div0 = divisor(stol(nstr,nullptr,10));
		if (div0 == -1) {
			continue;
		}
		cout << nstr << " " << div2 << " " << div3 << " " << div4 << " " << div5 << " " << div6 << " " << div7 << " " << div8 << " " << div9 << " " << div0 << endl;
		count++;
	}
	return 0;
}
