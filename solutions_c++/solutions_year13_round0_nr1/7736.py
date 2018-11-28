#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <ctime>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include<bitset>
#define foreach(it, l) for (typeof(l.begin()) it = l.begin(); it != l.end(); it++)
#define db(a) \
cout << #a << " = " << a << endl
#define db2(a, b) \
cout << #a << " = " << a << " " << #b << " = " << b << endl
#define inf (1<<30)
using namespace std;
int main() {
	#ifdef dennisbot
		freopen("in.in", "r", stdin);
		freopen("ou.out", "w", stdout);
	#endif
	int t, cont = 0;
	vector<string> m(4);
	scanf("%d", &t);
	for (int test = 0; test < t; test++) {
		int ceros = 0;
		for (int i = 0; i < 4; ++i)
			cin >> m[i];
		string msg = "";
		bool done = false, O_won = true, X_won = true;
		for (int i = 0; i < 4 && !done; ++i) {
			O_won = true, X_won = true;
			for (int j = 0; j < 4 && !done; ++j) {

				if (m[i][j] == '.') ceros++;

				if (m[i][j] != 'O' && m[i][j] != 'T') {
					O_won = false;
				}
				if (m[i][j] != 'X' && m[i][j] != 'T') {
					X_won = false;
				}
			}
			if (O_won || X_won) {
				done = true;
				if (O_won)
					msg = "O won";
				else
					msg = "X won";
			}
			if (!done) {
				O_won = true; X_won = true;
				for (int j = 0; j < 4 && !done; ++j) {
					if (m[j][i] != 'O' && m[j][i] != 'T') {
						O_won = false;
					}
					if (m[j][i] != 'X' && m[j][i] != 'T') {
						X_won = false;
					}
				}
				if (O_won || X_won) {
					done = true;
					if (O_won)
						msg = "O won";
					else
						msg = "X won";
				}
			}
		}
		if (!done) {
			O_won = true; X_won = true;
			for (int k = 0; k < 4; ++k) {
				if (m[k][k] != 'O' && m[k][k] != 'T') {
					O_won = false;
				}
				if (m[k][k] != 'X' && m[k][k] != 'T') {
					X_won = false;
				}
			}
			if (O_won || X_won) {
				done = true;
				if (O_won)
					msg = "O won";
				else
					msg = "X won";
			}
			if (!done) {
				O_won = true; X_won = true;
				for (int k = 0; k < 4; ++k) {
					if (m[k][3 - k] != 'O' && m[k][3 - k] != 'T') {
						O_won = false;
					}
					if (m[k][3 - k] != 'X' && m[k][3 - k] != 'T') {
						X_won = false;
					}
				}
				if (O_won || X_won) {
					done = true;
					if (O_won)
						msg = "O won";
					else
						msg = "X won";
				}
			}
		}
		if (msg == "") {
			if (ceros != 0) {
				printf("Case #%d: Game has not completed\n", test + 1);
			}
			else {
				printf("Case #%d: Draw\n", test + 1);
			}
		}
		else {
			printf("Case #%d: %s\n", test + 1, msg.c_str());
		}
	}
	return 0;
}

