/*
ID: oooctav1
PROG: checker
LANG: C++
*/
#include <iostream> 
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <stack>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
using namespace std;
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define N 100005

char a[4][4];

int main() {
//	freopen ("checker.out","w",stdout);
//	freopen ("checker.in","r",stdin);
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	string s;
  getline(cin, s);
	for (int tt = 1; tt <= t; tt++) {
		string s;
		for (int j = 0; j < 4; j++)	{
			getline(cin, s);
			for (int k = 0; k < 4; k++) a[j][k] = s[k];
		}
		char won = '.';
		for (int j = 0; j < 4; j++) {
			bool yes = true;
			char tthis = a[j][0];
			for (int i = 0; i < 4; i++) {
				if (tthis == 'T') tthis = a[j][i];
				if (a[j][i] != 'T' && a[j][i] != tthis) yes = false;
			}
			if (yes && tthis != '.') won = tthis;
		}

		for (int j = 0; j < 4; j++) {
			bool yes = true;
			char tthis = a[0][j];
			for (int i = 0; i < 4; i++) {
				if (tthis == 'T') tthis = a[i][j];
				if (a[i][j] != 'T' && a[i][j] != tthis) yes = false;
			}
			if (yes && tthis != '.') won = tthis;
		}

			bool yes = true;
			char tthis = a[0][0];
			for (int i = 0; i < 4; i++) {
				if (tthis == 'T') tthis = a[i][i];
				if (a[i][i] != 'T' && a[i][i] != tthis) yes = false;
			}
			if (yes && tthis != '.') won = tthis;

			yes = true;
			tthis = a[0][3];
			for (int i = 0; i < 4; i++) {
				if (tthis == 'T') tthis = a[i][3-i];
				if (a[i][3-i] != 'T' && a[i][3-i] != tthis) yes = false;
			}
			if (yes && tthis != '.') won = tthis;

		string rez = "";
		if (won != '.') rez = rez + won + " won";
		for (int j = 0; j < 4; j++)
			for (int i = 0; i < 4; i++)
				if (a[i][j] == '.' && rez == "") rez = "Game has not completed";
		if (rez == "") rez = "Draw";

		cout << "Case #" << tt << ": " << rez << endl; 
		getline(cin, s);
		
	}

	return 0;
}
