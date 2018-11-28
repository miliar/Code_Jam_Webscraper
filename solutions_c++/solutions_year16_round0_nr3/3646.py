#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
using namespace std;

int divider(long long a) {
	if (a == 1 || a == 2 || a == 3) {
		return 1;
	}
	for (long long i = 2; i <= (long long)ceil(sqrt((double)a)); i++) {
		if (a % i == 0) {
			return i;
		}
	}
	return 1;
}

int main() {
	ifstream in("C-small-attempt1.in");
	ofstream out("C-small.out");
	long long T, N, J;
	in >> T >> N >> J;

	out << "Case #" << 1 << ":\n";

	vector<long long> bits(N);
	long long n;

	vector<long long> bases(9);
	vector<long long> divs(9);
	long long bit;
	long long num;
	for (long long i = 1; i <= 65536; i++) {
		if (J == 0) {
			break;
		}
		num = i;

		for (long long j = N - 1; j >= 0; j--) {
			bit = num & 1;
			num >>= 1;
			bits[j] = bit;
		}

		if (bits[0] == 0 || bits[N - 1] == 0) {
			continue;
		}

		for (long long j = 2; j <= 10; j++) {
			long long base = 1;
			long long sum = 0;
			for (long long k = N - 1; k >= 0; k--) {
				sum += bits[k] * base;
				base *= j;
			}
			bases[j - 2] = sum;
		}
		bool is_norm = true;
		for (long long j = 0; j < 9; j++) {
			divs[j] = divider(bases[j]);
			if (divs[j] == 1) {
				is_norm = false;
				break;
			}
		}
		if (is_norm) {
			for (long long j = 0; j < N; j++) {
				out << bits[j];
			}
			out << ' ';
			for (long long j = 0; j < 9; j++) {
				out << divs[j] << ' ';
			}
			out << '\n';
			J--;
		}
	}

	in.close();
	out.close();
	return 0;
}