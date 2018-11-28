#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <sstream>

#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm> 

using namespace std;

char board[123][123];
int L[123][123], R[123][123], U[123][123], D[123][123];
string s;

void doit() {
	int Ro, C;
	int sol = 0;
	cin >> Ro >> C;
	//cerr << Ro << C << '\n';
	getline(cin,s);
	for (int i = 0; i < Ro; i++) {
		getline(cin,s);
		//cerr << s << '\n';
		for (int j = 0; j < C; j++) {
			board[i][j] = s[j];
		}
	}
	// Set U
	for (int i = 0; i < Ro; i++) {
		U[i][0] = 0;
		if (board[i][0] != '.')
			U[i][0] = -1;
		for (int j = 1; j < C; j++) {
			U[i][j] = 1;
			if (U[i][j-1] == 0) {
				if (board[i][j] == '.')
					U[i][j] = 0; 
				else
					U[i][j] = -1;
			}
		}
	}
	// Set D
	for (int i = 0; i < Ro; i++) {
		D[i][C-1] = 0;
		if (board[i][C-1] != '.')
			D[i][C-1] = -1;
		for (int j = C-2; j >= 0; j--) {
			D[i][j] = 1;
			if (D[i][j+1] == 0) {
				if (board[i][j] == '.')
					D[i][j] = 0; 
				else
					D[i][j] = -1;	
			}
		}
	}
	// Set L
	for (int j = 0; j < C; j++) {
		L[0][j] = 0;
		if (board[0][j] != '.')
			L[0][j] = -1;
		for (int i = 1; i < Ro; i++) {
			L[i][j] = 1;
			if (L[i-1][j] == 0) {
				if (board[i][j] == '.')
					L[i][j] = 0;
				else
					L[i][j] = -1;
			}
		}
	}
	// Set R
	for (int j = 0; j < C; j++) {
		R[Ro-1][j] = 0;
		if (board[Ro-1][j] != '.')
			R[Ro-1][j] = -1;
		for (int i = Ro-2; i >= 0; i--) {
			R[i][j] = 1;
			if (R[i+1][j] == 0) {
				if (board[i][j] == '.')
					R[i][j] = 0; 
				else
					R[i][j] = -1;
			}
		}
	}
	// Solve
	for (int i = 0; i < Ro; i++) {
		for (int j = 0; j < C; j++) {
			if ((D[i][j] + U[i][j] + R[i][j] + L[i][j]) == -4) {
				if (board[i][j] != '.') {
					cout << "IMPOSSIBLE\n";
					return;
				} 
			}
			if ((board[i][j] == '<') and (U[i][j] == -1)) {
				sol++;
			}
			if ((board[i][j] == '>') and (D[i][j] == -1)) {
				sol++;
			}
			if ((board[i][j] == '^') and (L[i][j] == -1)) {
				sol++;
			}
			if ((board[i][j] == 'v') and (R[i][j] == -1)) {
				sol++;
			}
		}
	}
	cout << sol << '\n';
	return;
}

int main () {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		doit();
	}
	return 0;
}

