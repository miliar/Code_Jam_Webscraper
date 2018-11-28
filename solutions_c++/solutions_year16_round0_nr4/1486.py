#include <fstream>

using namespace std;

typedef unsigned long long ull;

int T, K, C, S;

ull ipow(ull base, ull exp) {
	ull res = 1;
	while(exp) {
		if(exp & 1) {
			res *= (ull)base;
		}
		exp >>= 1;
		base *= base;
	}

	return res;
}

inline ull blockAt(ull block, ull num, ull blockSize) {
	return (block - 1) * blockSize + num;
}

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");

	in >> T;

	for(int t = 1; t <= T; t++) {
		out << "Case #" << t << ": ";

		in >> K >> C >> S;

		if(C == 1) {
			if(S < K) {
				out << "IMPOSSIBLE" << endl;
			} else {
				for(int i = 1; i <= K; i++)
					out << i << " ";
				out << endl;
			}
			continue;
		}

		if((K+1)/2 > S) {
			out << "IMPOSSIBLE" << endl;
			continue;
		}

		ull blockSize = ipow(K, C-1);

		for(ull i = 2; i <= K; i += 2)
			out << blockAt(i-1, i, blockSize) << " ";

		if(K % 2 == 1)
			out << ipow(K, C);

		out << endl;
	}

	return 0;
}
