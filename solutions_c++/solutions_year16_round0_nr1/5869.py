#include <fstream>

using namespace std;

int main() {
	ifstream infile("A-large.in");
	ofstream outfile("A.out");
	int n, x, t, T;
	
	infile >> n;
	
	for (int i=0; i < n; i++) {
		bool seenDigits[10] = 
			{false, false, false, false, false, 
			 false, false, false, false, false};
		int digitsRemain = 10;
		infile >> x;
		outfile << "Case #" << i+1 << ": ";
		if (!x) {
			outfile << "INSOMNIA" << endl;
			continue;
		}
		T = 0;
		while (digitsRemain) {
			T += x;
			t = T;
			while (t) {
				if (!seenDigits[t % 10]) {
					seenDigits[t % 10] = true;
					digitsRemain--;
				}
				t /= 10;
			}

		}
		outfile << T << endl;
	}
	
	return 0;
}
