#include <iostream>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

set<int> nums;

int add_nums(long N) {
	while (N != 0) {
		nums.insert(N % 10);
		if (nums.size() == 10) {
			return 1;
		}
		N = (N - (N % 10)) / 10;
	}	
	return 0;
}

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	long T, N;
	in >> T;

	for (long i = 0; i < T; i++) {
		in >> N;
		if (N == 0) {
			out << "Case #" << i + 1 << ": INSOMNIA\n";
			continue;
		}
		for (long j = 1; j <= 1000000; j++) {
			if (add_nums(N*j) == 1) {
				out << "Case #" << i + 1 << ": " << N*j << '\n';
				break;
			}
			if (j == 1000000) {
				out << "Case #" << i + 1 << ": INSOMNIA\n";
			}
		}
		nums.clear();
	}

	in.close();
	out.close();
	return 0;
}