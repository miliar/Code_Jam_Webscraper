#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>

using namespace std;

int N, R, P, S;

char A[2048];

string recurse(int N, char head) {
	if (N == 0) {
		if (head == 'R') {
			return "R";
		} else if (head == 'P') {
			return "P";
		} else if (head == 'S') {
			return "S";
		} else {
			return "";
		}
	} else {
		if (head == 'R') {
			string a = recurse(N - 1, 'R');
			string b = recurse(N - 1, 'P');
			return a < b ? (a + b) : (b + a);
		} else if (head == 'P') {
			string a = recurse(N - 1, 'P');
			string b = recurse(N - 1, 'S');
			return a < b ? (a + b) : (b + a);
		} else if (head == 'S') {
			string a = recurse(N - 1, 'S');
			string b = recurse(N - 1, 'R');
			return a < b ? (a + b) : (b + a);
		} else {
			return "";
		}
	}
}

string ok(int N, char head) {
	string str = recurse(N, head);
	int r = 0, p = 0, s = 0;
	int L = int(str.length());
	for (int i = 0; i < L; i++) {
		if (str[i] == 'R') {
			r++;
		} else if (str[i] == 'P') {
			p++;
		} else if (str[i] == 'S') {
			s++;
		}
	}
//	printf("ok: %c %s --> %d,%d,%d (%d,%d,%d)\n", head, str.c_str(), r, p, s, R, P, S);
	if (r == R && p == P && s == S) {
		return str;
	} else {
		return "";
	}
}

void solve(int CASE) {
	string r = ok(N, 'R');
	string p = ok(N, 'P');
	string s = ok(N, 'S');
	string best = "";
	if (r != "" && (best == "" || r < best)) best = r;
	if (p != "" && (best == "" || p < best)) best = p;
	if (s != "" && (best == "" || s < best)) best = s;
	if (best == "") {
		printf("Case #%d: %s\n", CASE, "IMPOSSIBLE");
	} else {
		printf("Case #%d: %s\n", CASE, best.c_str());
	}
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	for (int c = 1; c <= T; c++) {
		fin >> N;
		fin >> R;
		fin >> P;
		fin >> S;
		solve(c);
	}
    return 0;
}
