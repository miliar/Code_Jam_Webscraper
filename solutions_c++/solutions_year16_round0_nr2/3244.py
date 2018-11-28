#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <bitset>
#include <string>


using namespace std;

bitset<105> S;

int solve(int L) {
	int res = 0;
	int p = 0;

	while (p < L) {
		while (p < L && S[p]) {
			p++;
		}
		int c = 0;
		while (p + c < L && !S[p+c]) {
			c++;
		}

		if (p < L) {
			if (p > 0) {
				res += 2;
			} else {
				res++;
			}
		}

		p += c;
	}

	return res;
}


int main() {

	ifstream in ("in.txt");
	ofstream out ("out.txt");

	int T; in >> T;

	string line;
	getline(in, line);

	for (int i = 1; i <= T; i++) {

		getline(in, line);

		int L = (int) line.size();

		S.reset();

		for (int j = 0; j < L; j++) {
			if (line[j] == '-') {
				S[j] = false;
			} else {
				S[j] = true;
			}
		}

		
		int res = solve(L);
			
		out << "Case #" << i << ": " << res << endl;
		
	}


	in.close();
	out.close();
	return 0;
}
