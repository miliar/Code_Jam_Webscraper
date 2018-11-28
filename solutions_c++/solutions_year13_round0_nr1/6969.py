#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cassert>

using namespace std;

int n, T;
int f[4][4];



int con(char c) {
	if (c == 'X') return 10;
	if (c == 'O') return 100;
	if (c == 'T') return 1000;
	return 1;
}

bool filled = true;

bool whoX() {
	for (int r = 0 ; r < 4 ; r ++) {
		int rs = 0;
		for (int j = 0 ; j < 4; j ++) rs += f[r][j];
		if (rs%10 != 0) filled = false;
		if (rs == 40 || rs == 1030) {
			return true;
		}
	}
	for (int r = 0 ; r < 4 ; r ++) {
		int cs = 0;
		for (int j = 0 ; j < 4; j ++) cs += f[j][r];
		if (cs%10 != 0) filled = false;
		if (cs == 40 || cs == 1030) {
			return true;
		}
	}
	int d = 0;
	for (int i = 0; i < 4 ; i++) d += f[i][i];
	if (d == 40 || d == 1030) return true;
	d = 0;
	for (int i = 0 ; i < 4 ; i ++) d += f[3-i][i];
	if (d == 40 || d == 1030) return true;
	return false;
}

bool whoO() {
	for (int r = 0 ; r < 4 ; r ++) {
		int cs = 0;
		for (int j = 0 ; j < 4; j ++) cs += f[j][r];
		if (cs%10 != 0) filled = false;
		if (cs == 400 || cs == 1300) {
			return true;
		}
	}
	for (int r = 0 ; r < 4 ; r ++) {
		int rs = 0;
		for (int j = 0 ; j < 4; j ++) rs += f[r][j];
		if (rs%10 != 0) filled = false;
		if (rs == 400 || rs == 1300) {
			return true;
		}
	}
	int d = 0;
	for (int i = 0; i < 4 ; i++) d += f[i][i];
	if (d == 400 || d == 1300) return true;
	d = 0;
	for (int i = 0 ; i < 4 ; i ++) d += f[3-i][i];
	if (d == 400 || d == 1300) return true;

	return false;
	
		
}

void solve(int T) {
	filled = true;
	for (int i = 0 ; i < 4 ; i ++) {
		for (int j = 0 ; j < 4 ; j ++) {
			char c;
			scanf("%c", &c);
			f[i][j] = con(c);	
			if (f[i][j] == 1) filled = false;
		}
		scanf("\n");
	}	
	bool O = whoO();
	bool X = whoX();
	if (O && X) {
		printf("Case #%d: Draw\n", T);
		return;
	}
	if (O) {
		printf("Case #%d: O won\n", T);
		return;
	}
	
	if (X) {
		printf("Case #%d: X won\n", T);
		return;
	}
	if (filled) printf("Case #%d: Draw\n", T);
	else 
		printf("Case #%d: Game has not completed\n", T);


	
}


int main() {
	scanf("%d\n", &T);
	for (int i = 1 ; i <= T ; i ++) solve(i);
	return 0;
}