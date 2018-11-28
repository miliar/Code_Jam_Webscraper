#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

string check(void) {
	char s[4][4];
	int a[3];
	bool draw = true;

	// input
	for(int i = 0; i < 4; i++) {
		cin >> s[i];
	}

	// colum
	for(int i = 0; i < 4; i++) {
		// 0 -> X, 1 -> O, 2 -> T
		a[0] = 0; a[1] = 0; a[2] = 0;
		for(int j = 0; j < 4; j++) {
			if(s[i][j] == 'X')
				a[0]++;
			else if(s[i][j] == 'O')
				a[1]++;
			else if(s[i][j] == 'T')
				a[2]++;
			else
				draw = false;

			if(a[0] == 4 || (a[0] == 3 && a[2] == 1)) {
				return "X won";
			} else if(a[1] == 4 || (a[1] == 3 && a[2] == 1)) {
				return "O won";
			}
		}
	}

	// row
	for(int j = 0; j < 4; j++) {
		// 0 -> X, 1 -> O, 2 -> T
		a[0] = 0; a[1] = 0; a[2] = 0;
		for(int i = 0; i < 4; i++) {
			if(s[i][j] == 'X')
				a[0]++;
			else if(s[i][j] == 'O')
				a[1]++;
			else if(s[i][j] == 'T')
				a[2]++;
			
			if(a[0] == 4 || (a[0] == 3 && a[2] == 1)) {
				return "X won";
			} else if(a[1] == 4 || (a[1] == 3 && a[2] == 1)) {
				return "O won";
			}
		}
	}

	// diagonal
	a[0] = a[1] = a[2] = 0;
	for(int i = 0; i < 4; i++)
		if(s[i][i] == 'X') 
			a[0]++;
		else if(s[i][i] == 'O')
			a[1]++;
		else if(s[i][i] == 'T')
			a[2]++;
	if(a[0] == 4 || (a[0] == 3 && a[2] == 1))
		return "X won";
	else if(a[1] == 4 || (a[1] == 3 && a[2] == 1))
		return "O won";

	a[0] = a[1] = a[2] = 0;
	for(int i = 0; i < 4; i++)
		if(s[i][3 - i] == 'X') 
			a[0]++;
		else if(s[i][3 - i] == 'O')
			a[1]++;
		else if(s[i][3 - i] == 'T')
			a[2]++;
	if(a[0] == 4 || (a[0] == 3 && a[2] == 1))
		return "X won";
	else if(a[1] == 4 || (a[1] == 3 && a[2] == 1))
		return "O won";

	if(draw) {
		return "Draw";
	} else {
		return "Game has not completed";
	}
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: %s\n", i, check().c_str());
	}
}
