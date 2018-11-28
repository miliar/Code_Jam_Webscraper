/*
 * A.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: yassery
 */

#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

char s[4][5];

bool testWin(char c) {
	int i, j;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (s[i][j] != c && s[i][j] != 'T')
				break;
		}
		if (j == 4)
			return true;
	}

	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (s[j][i] != c && s[j][i] != 'T')
				break;
		}
		if (j == 4)
			return true;
	}

	for (i = 0; i < 4; i++) {
		if (s[i][i] != c && s[i][i] != 'T')
			break;
	}
	if (i == 4)
		return true;
	for (i = 0; i < 4; i++) {
		if (s[i][3 - i] != c && s[i][3 - i] != 'T')
			break;
	}
	if (i == 4)
		return true;

	return false;
}

bool hasChar(char c) {
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (s[i][j] == c)
				return true;
	return false;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int tt = 0; tt < T; tt++) {
		for (int i = 0; i < 4; i++) {
			cin >> s[i];
		}

		cout<<"Case #"<<tt+1<<": ";

		if (testWin('X'))
			cout << "X won" << endl;
		else if (testWin('O'))
			cout << "O won" << endl;
		else if (hasChar('.'))
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}

	return 0;
}
