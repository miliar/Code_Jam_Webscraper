#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <queue>
#include "string.h"
#include "assert.h"
#include "math.h"

using namespace std;

int cnt[256];
char * dig[] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};



void countletters(const char * s) {
	for (char c = 'A'; c <= 'Z'; c++)
		cnt[c] = 0;

	for (const char * p = s; *p != 0; p++) {
			(cnt[*p])++;
	}
}

void solve() {
	string str; getline(cin, str);
	int l = str.length();
	countletters(str.c_str());
	
	int d[10];
	for (int i = 0; i < 10; i++)
		d[i] = 0;

	d[2] = cnt['W'];
	d[4] = cnt['U'];
	d[6] = cnt['X'];
	d[8] = cnt['G'];
	d[0] = cnt['Z'];
	d[7] = cnt['S'] - cnt['X'];
	d[3] = cnt['H'] - cnt['G'];
	d[5] = cnt['V'] - d[7];
	d[9] = cnt['I'] - d[8] - d[6] - d[5];
	d[1] = cnt['O'] - d[2] - d[4] - d[0];

	string a="";
	for (int i = 0; i <= 9; i++) {
		char c;
		if (d[i] > 0) {
			c = '0' + i;
			a = a + string(d[i], c);
		}
	}
	cout << a;
}

int main(int argc, char** argv) {
	int T;
	cin >> T; // number of test cases
	string s; getline(cin, s);
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}

	