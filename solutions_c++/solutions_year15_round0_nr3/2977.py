//============================================================================
// Name        : third.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

int main() {
	ifstream ifs;
	ifs.open("C-small-attempt2.in");
	ofstream ofs;
	ofs.open("output2.out");
	int z;
	ifs >> z;

	int arr[5][5] = { { 0, 0, 0, 0, 0 }, { 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 },
			{ 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };
	for (int y = 0; y < z; y++) {
		if (ifs.good()) {
			int l, x;
			char *s;
			ifs >> l >> x;
			char *n = new char[(l * x) + 1];
			s = new char[l + 1];
			ifs >> s;
			strcpy(n, s);
			for (int i = 1; i < x; i++) {
				strcat(n, s);
			}
			int tlen = strlen(n);
			char *p;
			while ((p = strpbrk(n, "i")) != NULL)
				*p = '2';
			while ((p = strpbrk(n, "j")) != NULL)
				*p = '3';
			while ((p = strpbrk(n, "k")) != NULL)
				*p = '4';
			int n1, n2;
			int STAGE = 0;
			int start = 0;
			n1 = 1;
			for (int i = start; i < tlen; i++) {
				n2 = (n[i] - '0');
				int s1 = 1, s2 = 1;
				if (n1 < 0) {
					n1 *= -1;
					s1 = -1;
				}
				if (n2 < 0) {
					n2 *= -1;
					s2 = -1;
				}
				n1 = arr[n1][n2];
				n1 = n1 * s1 * s2;
				if (n1 == 2 && STAGE == 0) {
					n1 = 1;
					start = i + 1;
					STAGE = 1;
				}
				if (n1 == 3 && STAGE == 1) {
					n1 = 1;
					start = i + 1;
					STAGE = 2;
				}

			}
			if (n1 == 4 && STAGE == 2) {
				STAGE = 3;
			}
			if (STAGE == 3) {
				ofs << "Case #" << y + 1 << ": " << "YES" << endl;
				//cout << "Case #" << y + 1 << ": " << "YES" << endl;
			} else {
				ofs << "Case #" << y + 1 << ": " << "NO" << endl;
				//cout << "Case #" << y + 1 << ": " << "NO" << endl;
			}

		}
	}

	return 0;
}

