#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("AIn.txt");
ofstream fout("AOut.txt");

#define cin fin
#define cout fout

int main() {
	int T;
	cin >> T;
	for (int TC = 1; TC <= T; TC++) {
		long long n;
		cin >> n;

		if (n == 0) {
			cout << "Case #" << TC << ": " << "INSOMNIA" << endl;
			continue;
		}

		int dmax = 10;
		long long t = n;
		while (t) {
			t /= 10;
			dmax *= 10;
		}

		bool mark[10] = { 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 };
		int drem = 10;

		long long u = 0;
		int i;
		for (i = 1; i <= dmax; i++) {
			u = n * i;
			while (u) {
				if (!mark[u % 10]) {
					mark[u % 10] = true;
					drem--;
				}
				u /= 10;
			}
			if (drem == 0)
				break;
		}

		if (drem != 0) {
			cout << "Case #" << TC << ": " << "INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << TC << ": " << i * n << endl;
		}

	}
}