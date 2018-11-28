#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;




char app[4][4] = { {'1', 'i', 'j', 'k'} , {'i', '1', 'k', 'j'} , {'j', 'k', '1', 'i'} , {'k', 'j', 'i', '1'} };



int toInt(char a) {
	int aa = 0;
	if (a == 'i') aa = 1;
	if (a == 'j') aa = 2;
	if (a == 'k') aa = 3;
	return aa;
}


char f(char a, char b) {
	int aa = toInt(a), bb = toInt(b);
	return app[aa][bb];
}


bool sgn[4][4] = { {0,0,0,0} , {0,1,0,1}, {0,1,1,0}, {0,0,1,1} };

bool mminus(char a, char b) {
	int aa = toInt(a), bb = toInt(b);
	return sgn[aa][bb];
}


// All string is -1
// First pos that is i
// Last that is k to the end.
// Last > first


int main () {
	long long T, L, X;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		cin >> L >> X;
		string s;
		cin >> s;

		
		string tot = "";
		for (int i = 0; i < min(X, 8 + X%4); ++i) {
			tot = tot + s;
		}


		bool minus = false;
		char cur = '1';


		int firsti = -1, lastk = -1;
		for (int i = 0; i < min(X, 8 + X%4) * L; ++i) {
			minus = minus ^ mminus(cur, tot[i]);
			cur = f(cur, tot[i]);

			if (!minus && cur == 'i' && firsti == -1) {
				firsti = i;
			}
			if (!minus && cur == 'k') {
				lastk = i;
			}
		}

		string rez = "YES";
		if (!minus || cur != '1' || firsti == -1 || lastk == -1 || firsti >= lastk) rez = "NO";

		printf("Case #%d: %s\n", t, rez.c_str());

	}
	return 0;
}
