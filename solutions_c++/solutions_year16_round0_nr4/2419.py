#include <algorithm>
#include <fstream>

using namespace std;

long long pow(int a, int b) {
	long long result = 1;
	for (int i = 0; i < b; ++i) {
		result *= a;
	}
	return result;
}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in >> T;
	for (int test = 1; test <= T; test++) {
		out << "Case #" << test << ": ";
		int K, C, S;
		in >> K >> C >> S;
		if (C == 1 || K == 1) {
			if (S < K) {
				out << "IMPOSSIBLE\n";
			}
			else {
				for (int i = 1; i <= K; ++i) {
					out << i << " ";
				}
				out << endl;
			}
			continue;
		}
		if (S < (K + 1) / 2) {
			out << "IMPOSSIBLE\n";
			continue;
		}
		long long step = pow(K, C - 1);
		for (int i = 0; i < K; i+=2) {
			out << min(i*step + i + 2, pow(K, C)) << " ";
		}
		out << endl;
	}
	return 0;
}