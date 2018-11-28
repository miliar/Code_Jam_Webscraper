#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
using namespace std;

bool emptySquare(char str[5][5]) {
	for (int i=0; i < 4; i++) {
		for (int j=0; j < 4; j++) {
			if (str[i][j] == '.') {
				return true;
			}
		}
	}
	return false;
}

bool hasWon(char str[5][5], char player) {
	bool flag;

	for (int i=0; i < 4; i++) {
		flag = true;
		for (int j=0; j < 4; j++) {
			if (str[i][j] != player && str[i][j] != 'T') {
				flag = false;
				break;
			}
		}
		if (flag == true) {
			return true;
		}
	}

	for (int i=0; i < 4; i++) {
		flag = true;
		for (int j=0; j < 4; j++) {
			if (str[j][i] != player && str[j][i] != 'T') {
				flag = false;
				break;
			}
		}
		if (flag == true) {
			return true;
		}
	}

	flag = true;
	for (int i=0; i < 4; i++) {
		if (str[i][i] != player && str[i][i] != 'T') {
			flag = false;
			break;
		}
	}

	if (flag == true) {
		return true;
	}

	flag = true;
	for (int i=3; i >= 0; i--) {
		if (str[3-i][i] != player && str[3-i][i] != 'T') {
			return false;
		}
	}

	return true;
}

int main() {
	int t;
	char str[5][5];

	FILE *fp, *fin;
	fin = fopen("C:\\Users\\anurag\\Desktop\\A-large.in", "r");
	fp = fopen("C:\\Users\\anurag\\Desktop\\output.txt", "w");

	fscanf(fin, "%d", &t);

	for (int ts=1; ts <= t; ts++) {
		for (int i=0; i < 4; i++) {
			fscanf(fin, "%s", &str[i]);
		}
		if (hasWon(str, 'X')) {
			fprintf(fp, "Case #%d: X won\n", ts);
		} else if (hasWon(str, 'O')) {
			fprintf(fp, "Case #%d: O won\n", ts);
		} else {
			if (emptySquare(str)) {
				fprintf(fp, "Case #%d: Game has not completed\n", ts);
			} else {
				fprintf(fp, "Case #%d: Draw\n", ts);
			}
		}
	}
	return 0;
}
