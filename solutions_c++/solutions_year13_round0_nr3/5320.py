#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int inv(int a) {
	int b = 0;
	while (a>=10) {
		b = b*10 + a%10;
		a = a/10;
	}
	return b*10 + a;
}

bool palindrome(int a) {
	return inv(a) == a;
}

int main() {
	ifstream fin("C:\\Users\\Daniel\\Downloads\\Firefox\\C-small-attempt0.in");
	ofstream fout("C:\\Users\\Daniel\\Downloads\\Firefox\\C-small-attempt0.out");
	unsigned int T;
	fin >> T;

	for (unsigned int k=1; k<=T; k++) {
		unsigned int cont = 0;
		unsigned int a, b;
		fin >> a >> b;
		for (unsigned int i=(unsigned int)sqrt(a); i<=(unsigned int)sqrt(b); i++) {
			if (palindrome(i)) {
				if (palindrome(i*i) && i*i>=a && i*i<=b) {
					cont++;
				}
			}
		}

		fout << "Case #" << k << ": " << cont << endl;
	}


	return 0;
}
