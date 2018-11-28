#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

inline string compute(string x, char y) {
	bool pos = true;
	if (x[0] == '-') {
		pos = !pos;
	}
	char temp;
	switch (x[1]) {
		case '1':
			switch (y) {
				default:
					temp = y;
					break;
			}
			break;
		case 'i':
			switch (y) {
				case '1':
					temp = 'i';
					break;
				case 'i':
					temp = '1';
					pos = !pos;
					break;
				case 'j':
					temp = 'k';
					break;
				case 'k':
					temp = 'j';
					pos = !pos;
					break;
				default:
					break;
			}
			break;
		case 'j':
			switch (y) {
				case '1':
					temp = 'j';
					break;
				case 'i':
					temp = 'k';
					pos = !pos;
					break;
				case 'j':
					temp = '1';
					pos = !pos;
					break;
				case 'k':
					temp = 'i';
					break;
				default:
					break;
			}
			break;
		case 'k':
			switch (y) {
				case '1':
					temp = 'k';
					break;
				case 'i':
					temp = 'j';
					break;
				case 'j':
					temp = 'i';
					pos = !pos;
					break;
				case 'k':
					temp = '1';
					pos = !pos;
					break;
				default:
					break;
			}
			break;
		default:
			break;
	}
	if (pos) {
		return "+" + string(1, temp);
	}
	else {
		return "-" + string(1, temp);
	}
}

int main() {
	ifstream fin;
	fin.open("C-small-attempt4.in");
	ofstream fout;
	fout.open("C-small-attempt4.out");
	
	int T;
	fin >> T;
	
	for (int num = 1; num <= T; num++) {
		int L, X;
		fin >> L;
		fin >> X;
		string token;
		fin >> token;
		if (L * X < 3) {
			cout << "Case #" << num << ": Too little" << endl;
			fout << "Case #" << num << ": NO" << endl;
			continue;
		}
		
		bool same = true;
		for (int c = 1; c < L; c++) {
			if (token[c] != token[0]) {
				same = false;
				break;
			}
		}
		if (same) {
			cout << "Case #" << num << ": Same" << endl;
			fout << "Case #" << num << ": NO" << endl;
			continue;
		}
		
		string prod = "+" + string(1, token[0]);
		for (int c = 1; c < L; c++) {
			prod = compute(prod, token[c]);
		}

		if ((X % 2 != 0 && prod != "-1") || (X % 2 == 0 && prod[1] == '1')) {
			cout << "Case #" << num << ": prod=" << prod << endl;
			fout << "Case #" << num << ": NO" << endl;
			continue;
		}
		
//		string **matrix = new string*[L];
//		for (int r = 0; r < L; r++) {
//			matrix[r] = new string[L];
//			for (int c = r; c < L; c++) {
//				if (r == c) {
//					matrix[r][c]= "+" + string(1, token[c]);
//				}
//				else {
//					matrix[r][c] = compute(matrix[r][c - 1], string(1, token[c]));
//				}
//			}
//		}
//		
//		string tempI, tempJ, tempK;
//		bool succ = false;
//		string baseI = "+1";
//		string baseJ = "+1";
//		int ix, jx, kx, i, j, start;
//		ix = 0;
//		i = 0;
//		start = 0;
//		while (ix < X && !succ) {
//			do {
//				tempI = compute(baseI, matrix[start][i]);
//				i++;
//			} while (tempI != "+i" && i < L);
//			if (tempI == "+i") {
//				jx = ix;
//				j = i;
//				while (jx < X && !succ) {
//					do {
//						tempJ = compute(baseJ, matrix[i][j]);
//						j++;
//					} while (tempJ != "+j" && j < L);
//					if (tempJ == "+j") {
//						string baseK = matrix[j][L - 1];
//						for (kx = jx; kx < X && !succ; kx++) {
//							tempK = compute(baseK, matrix[0][L - 1]);
//						}
//						if (tempK == "+k") {
//							succ = true;
//						}
//						else {
//							baseJ = "+j";
//							if (j >= L) {
//								jx++;
//								j = 0;
//								i = 0;
//							}
//							else {
//								i = j;
//							}
//						}
//					}
//					else {
//						baseJ = compute(baseJ, matrix[i][L - 1]);
//						jx++;
//						j = 0;
//						i = 0;
//					}
//				}
//				if (!succ) {
//					baseI = "+i";
//					if (i >= L) {
//						ix++;
//						i = 0;
//						start = 0;
//					}
//					else {
//						start = i;
//					}
//				}
//			}
//			else {
//				baseI = compute(baseI, matrix[0][L-1]);
//				ix++;
//				i = 0;
//			}
//		}
		string tempI, tempJ, tempK;
		tempI = "+" + string(1, token[0]);
		tempJ = "+" + string(1, token[1]);
		bool succ = tempI == "+i" && tempJ == "+j";
		int i, j, k;
		i = 1;
		while (!succ && i <= L * X - 3) {
			if (tempI == "+i") {
				j = i;
				tempJ = "+" + string(1, token[j % L]);
				j++;
				while (!succ && j <= L * X - 2) {
					if (tempJ == "+j") {
						succ = true;
					}
					tempJ = compute(tempJ, token[j % L]);
					j++;
				}
			}
			tempI = compute(tempI, token[i % L]);
			i++;
		}
		cout << "Case #" << num << ": i= " << i << ", j= " << j << ", prod= " << prod << endl;
		fout << "Case #" << num << ": " << (succ ? "YES" : "NO") << endl;
	}
	
	return 0;
}
