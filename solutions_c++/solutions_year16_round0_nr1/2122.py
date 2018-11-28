#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	string name = "A-large.in";
	ifstream input;
	input.open(name);
	ofstream output("out_" + name);
	int T;
	input >> T;
	for (int cases = 1; cases <= T; cases++) {
		long long n;
		input >> n;
		output << "Case #" << cases << ": ";
		if (!n) {
			output << "INSOMNIA" << endl;
			continue;
		}
		long long count = 0;
		long long N = 0;
		while (count != (1 << 10) - 1) {
			N += n; cout << count << endl;
			long long temp = N;
			while (temp) {
				count |= (1 << (temp % 10));
				temp /= 10;
			}
		}
		output << N << endl;
	}
	return 0;
}