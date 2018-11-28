#include <fstream>
#include <iterator>
#include <string>
#include <cmath>

using namespace std;

long long isPrime (long long n) {
	int d = 2;
	while (d < (int)pow(n, 0.5) + 1) {
		if (n % d == 0) return d;
		d++;
	}
	return 0;
}

int main () {
	ifstream fin ("input.txt");
	ofstream fout ("output.txt");
   
   	int n, count = 0, t, jj;
   	fin >> t >> n >> jj;

   	fout << "Case #1:" << endl;

	for (int i = 1 << (n - 1); i < 1 << n; i++) {
		if (i % 2 == 0) continue;
		int j = i;
		long long a[11];
		long long b[11];
		for (int t = 2; t < 11; t++) {
			b[t] = 1;
			a[t] = 0;
		}
		while (j > 0) {
			int x = j % 2;
			for (int t = 2; t < 11; t++) {
				a[t] += x * b[t];
				b[t] *= t;
			}
			j /= 2;
		}
		int k = 0;
		for (int t = 2; t < 11; t++)
			if (!isPrime(a[t])) {
				k = 1;
				break;
			}
		if (k == 0) {
			count++;
			fout << a[10] << " ";
			for (int t = 2; t < 11; t++)
			fout << isPrime(a[t]) << " ";
			fout << endl;
			if (count == jj) break;
		}
	}

    fin.close ();
    fout.close ();
    return 0;
}
