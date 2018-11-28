#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

char s[10][10];

int isXWin() {
	int xwin = false;
	for (int i = 0; i < 4; i++) {
		int cntx = 0;
		int cntt = 0;
		for (int j = 0; j < 4; j++) {
			if (s[i][j] == 'X') cntx++;
			if (s[i][j] == 'T') cntt++;
		}
		if (cntx == 4 || (cntx == 3 && cntt == 1)) {
			xwin = true;
			break;
		}
	}
	for (int i = 0; i < 4; i++) {
		int cntx = 0;
		int cntt = 0;
		for (int j = 0; j < 4; j++) {
			if (s[j][i] == 'X') cntx++;
			if (s[j][i] == 'T') cntt++;
		}
		if (cntx == 4 || (cntx == 3 && cntt == 1)) {
			xwin = true;
			break;
		}
	}
	
	int cntx = 0;
	int cntt = 0;
		
	for (int i = 0; i < 4; i++) {
		if (s[i][i] == 'X') cntx++;
		if (s[i][i] == 'T') cntt++;	
	}
	if (cntx == 4 || (cntx == 3 && cntt == 1)) {
		xwin = true;
	}
	
	cntx = 0;
	cntt = 0;
		
	for (int i = 0; i < 4; i++) {
		if (s[i][3 - i] == 'X') cntx++;
		if (s[i][3 - i] == 'T') cntt++;	
	}
	if (cntx == 4 || (cntx == 3 && cntt == 1)) {
		xwin = true;
	}
	
	if (xwin) return true;
	return false;
}

int isOWin() {
	int xwin = false;
	for (int i = 0; i < 4; i++) {
		int cntx = 0;
		int cntt = 0;
		for (int j = 0; j < 4; j++) {
			if (s[i][j] == 'O') cntx++;
			if (s[i][j] == 'T') cntt++;
		}
		if (cntx == 4 || (cntx == 3 && cntt == 1)) {
			xwin = true;
			break;
		}
	}
	for (int i = 0; i < 4; i++) {
		int cntx = 0;
		int cntt = 0;
		for (int j = 0; j < 4; j++) {
			if (s[j][i] == 'O') cntx++;
			if (s[j][i] == 'T') cntt++;
		}
		if (cntx == 4 || (cntx == 3 && cntt == 1)) {
			xwin = true;
			break;
		}
	}
	
	int cntx = 0;
	int cntt = 0;
		
	for (int i = 0; i < 4; i++) {
		if (s[i][i] == 'O') cntx++;
		if (s[i][i] == 'T') cntt++;	
	}
	if (cntx == 4 || (cntx == 3 && cntt == 1)) {
		xwin = true;
	}
	
	cntx = 0;
	cntt = 0;
		
	for (int i = 0; i < 4; i++) {
		if (s[i][3 - i] == 'O') cntx++;
		if (s[i][3 - i] == 'T') cntt++;	
	}
	if (cntx == 4 || (cntx == 3 && cntt == 1)) {
		xwin = true;
	}
	
	if (xwin) return true;
	return false;
}

int isEnded() {
	int isDot = false;
	for (int i = 0; i < 4; i++)	
		for (int j = 0; j < 4; j++)
			if (s[i][j] == '.')
				return false;
	return true;
}

string solve() {
	if (isXWin()) return "X won";
	else if (isOWin()) return "O won";
	else if(isEnded()) return "Draw";
	else return "Game has not completed";
}

int main() {
	int T , caseNo = 1;
	scanf("%d",&T);
	while (T--) {
		for (int i = 0; i < 4; i++) 
			scanf ("%s" , &s[i]);
		string res = solve ();
		//printf("Case #%d: %s\n" , caseNo ++ , res);
		cout << "Case #"<<caseNo++<<": "<< res << endl;
	}
	return 0;
}
