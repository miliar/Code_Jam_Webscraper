#include <cstdio>
#include <cassert>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

#define MINX(a, b) ((a) < (b) ? (a) : (b));
#define MAX(a, b) ((a) > (b) ? (a) : (b));

typedef unsigned long long ulng;
typedef signed long long slng;
typedef unsigned int uint;
typedef signed int sint;

void solve()
{
	string line;
	unsigned char buf[2001];
	int len = 0;
	int digitcnt[10] = {0};
	int hist[256] = {0};
	int n;

	cin >> line;
	len = line.length();
	assert(len <= 2000);
	strncpy((char*)buf, line.c_str(), sizeof(buf));
	buf[sizeof(buf) - 1] = '\0';

	for (int i = 0; i < len; i++) {
		hist[buf[i]]++;
	}

	// filter uniquely identifyable digits
	// Z = 0
	n = hist['Z'];
	digitcnt[0] = n;
	hist['Z'] -= n;
	hist['E'] -= n;
	hist['R'] -= n;
	hist['O'] -= n;
	// W = 2
	n = hist['W'];
	digitcnt[2] = n;
	hist['T'] -= n;
	hist['W'] -= n;
	hist['O'] -= n;
	// U = 4
	n = hist['U'];
	digitcnt[4] = n;
	hist['F'] -= n;
	hist['O'] -= n;
	hist['U'] -= n;
	hist['R'] -= n;
	// X = 6
	n = hist['X'];
	digitcnt[6] = n;
	hist['S'] -= n;
	hist['I'] -= n;
	hist['X'] -= n;
	// G = 8
	n = hist['G'];
	digitcnt[8] = n;
	hist['E'] -= n;
	hist['I'] -= n;
	hist['G'] -= n;
	hist['H'] -= n;
	hist['T'] -= n;

	// 2. filter: O = "ONE", T = "THREE", F = "FIVE", S = "SEVEN", "NINE"
	// O
	n = hist['O'];
	digitcnt[1] = n;
	hist['O'] -= n;
	hist['N'] -= n;
	hist['E'] -= n;
	// T
	n = hist['T'];
	digitcnt[3] = n;
	hist['T'] -= n;
	hist['H'] -= n;
	hist['R'] -= n;
	hist['E'] -= n;
	hist['E'] -= n;
	// F
	n = hist['F'];
	digitcnt[5] = n;
	hist['F'] -= n;
	hist['I'] -= n;
	hist['V'] -= n;
	hist['E'] -= n;
	// S
	n = hist['S'];
	digitcnt[7] = n;
	hist['S'] -= n;
	hist['E'] -= n;
	hist['V'] -= n;
	hist['E'] -= n;
	hist['N'] -= n;

	// "NINE"
	assert(hist['N'] == 2 * hist['I'] && hist['I'] == hist['E']);
	digitcnt[9] = hist['E'];
	hist['N'] -= 2 * digitcnt[9];
	hist['I'] -= digitcnt[9];
	hist['E'] -= digitcnt[9];

	for (char c = 'A'; c <= 'Z'; c++) {
		assert(hist[c] == 0);
	}

	for (int digit = 0; digit <= 9; digit++) {
		for (int c = 0; c < digitcnt[digit]; c++) {
			cout << (char)('0' + digit);
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << "\n";
	}
}
