// (c) IURII CHULININ, RF, 2016
#include <iostream>
#include <string>
using namespace std;

bool processCase(int caseNumber, int N, int J)
{
	cout << "Case #" << caseNumber << ":" << endl;
	if (N < 6) {
		return false;
	}
	const char* const prefix = N % 2 == 0 ? "11" : "110";
	const int maxValue = (1 << (N / 2 - 2)) - 1;
	for (int i = 0; i < J; i++) {
		string jamcoin = prefix;
		for (int mask = 1 << (N / 2 - 3); mask != 0; mask >>= 1) {
			jamcoin += (mask & i) ? "11" : "00";
		}
		jamcoin += "11";

		if (jamcoin.length() != N) {
			cout << " jamcoin.length():" << jamcoin.length() << " != " << N << "; ";
			return false;
		}
		cout << jamcoin.c_str() << " 3 4 5 6 7 8 9 10 11" << endl;
		if (i >= maxValue) {
			return false;
		}
	}
	return true;
}



int main() {
	int count = 0;
	cin >> count;
	for (int i = 0; i < count; i++) {
		int N, J;
		cin >> N >> J;
		if (!processCase(i + 1, N, J)) {
			cout << "I faild" << endl;
		}
		cout << endl;
	}
	return 0;
}