#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");


char* get(char c, char* buffer, int& len, int depth) {
	assert(len < 10000);
	if (depth == 0)
		buffer[len++] = c;
	else if (c == 'R') {
		if (depth == 1) {
			get('R', buffer, len, depth - 1);
			get('S', buffer, len, depth - 1);
		}
		else {
			get('S', buffer, len, depth - 1);
			get('R', buffer, len, depth - 1);
		}
	}
	else if (c == 'P') {
		get('P', buffer, len, depth - 1);
		get('R', buffer, len, depth - 1);
	}
	else if (c == 'S') {
		if (depth <= 2) {
			get('P', buffer, len, depth - 1);
			get('S', buffer, len, depth - 1);
		}
		else {
			get('S', buffer, len, depth - 1);
			get('P', buffer, len, depth - 1);
		}
	}
	return buffer;
}

char buf[10000];
int len;
int N, R, P, S;

bool match(char* na) {
	int r=0, p=0, s=0;
	for (int i = 0; i < len; i++) {
		if (buf[i] == 'R')
			r++;
		if (buf[i] == 'P')
			p++;
		if (buf[i] == 'S')
			s++;
	}

	buf[len] = 0;

	return r == R && p == P && s == S;
}

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";
		fin >> N >> R >> P >> S;
		if (match(get('R', buf, len = 0, N)))
			fout << buf << endl;
		else if (match(get('P', buf, len = 0, N)))
			fout << buf << endl;
		else if (match(get('S', buf, len = 0, N)))
			fout << buf << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}
}
