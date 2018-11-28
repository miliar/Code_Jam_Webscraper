#include <bits/stdc++.h>


using namespace std;

int main() {

    ifstream fin("D:\\Google Drive\\Descargas\\A-large.in");
    ofstream fout("D:\\Google Drive\\Descargas\\A-large.out");

	int T, N, n, i, c_d, digit;
	bool d[10];

	fin >> T;

	for (int c=1; c<=T; c++) {
		for (int j=0; j<10; j++) d[j] = false;
		c_d = 0;
		fin >> N;
		if (N == 0)
			fout << "Case #" << c << ": INSOMNIA" << endl;
		else {
			i = 1;
			while (true) {
				n = i*N;
				while (n > 0) {
					digit = n % 10;
					n /= 10;
					if (!d[digit]) {
						c_d++;
						d[digit] = true;
					}
					if (c_d == 10) break;
				}
				if (c_d == 10) {
					fout << "Case #" << c << ": " << i*N << endl;
					break;
				}
				i++;
			}
		}
	}

    return 0;
}