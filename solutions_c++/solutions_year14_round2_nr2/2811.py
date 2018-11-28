#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>
using namespace std;



int main() {

	int T;
	cin >> T;
	ofstream out("1B-B.txt");

	for (int idx = 1; idx <= T; idx++) {
		int A, B, K;
		cin >> A >> B >> K;

		int buf;
		long count = 0;
		for (int i = 0; i < A; i++) {
			for( int j = 0; j < B; j++) {
				buf = i & j;
				if (buf < K) count++;
			}
		}

		out << "Case #" << idx << ": " << count << endl;

	}
	out.close();
	return 0;
}