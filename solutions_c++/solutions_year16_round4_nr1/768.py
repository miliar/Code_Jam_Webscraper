#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

int n, p, r, s;
string line;

string gen(string str) {
	string res;
	for (int i = 0; i < str.size(); i++) {
		char ch = str[i];
		if (ch == 'P')
			res += "PR";
		else if (ch == 'S')
			res += "PS";
		else
			res += "RS";
	}
	return res;
}

int cp, cr, cs;
void cnt(string str) {
	cp = cr = cs = 0;
	for (int i = 0; i < str.size(); i++)
		if (str[i] == 'P')
			cp++;
		else if (str[i] == 'R')
			cr++;
		else if (str[i] == 'S')
			cs++;
}

void format(string &str) {
	int step = 1;
	while (step < (1 << n)) {
		for (int i = 0; i < str.size();) {
			if (str.substr(i, step) > str.substr(i + step, step)) {
				string tmp = str.substr(i, step);
				for (int j = 0; j < step; j++)
					str[i + j] = str[i + step + j];
				for (int j = 0; j < step; j++)
					str[i + step + j] = tmp[j];
			}
			i += 2 * step;
		}
		step *= 2;
	}
}

void solve() {
	cin >> n >> r >> p >> s;
	line = "P";
	for (int i = 1; i <= n; i++)
		line = gen(line);
	cnt(line);
	if (p == cp && r == cr && s == cs) {
		format(line);
		cout << line << endl;
		return;
	}		
	line = "S";
	for (int i = 1; i <= n; i++)
		line = gen(line);
	cnt(line);
	if (p == cp && r == cr && s == cs) {
		format(line);
		cout << line << endl;
		return;
	}
	line = "R";
	for (int i = 1; i <= n; i++)
		line = gen(line);
	cnt(line);
	if (p == cp && r == cr && s == cs) {
		format(line);
		cout << line << endl;
		return;
	}
	cout << "IMPOSSIBLE" << endl;
}


int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}