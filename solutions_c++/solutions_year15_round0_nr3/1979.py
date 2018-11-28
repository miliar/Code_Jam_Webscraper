#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

vector<vector<int> > table;

void init() {
	table = vector<vector<int> >(4, vector<int>(4));
	table[0][0] = 1;
	table[0][1] = 2;
	table[0][2] = 3;
	table[0][3] = 4;

	table[1][0] = 2;
	table[1][1] = -1;
	table[1][2] = 4;
	table[1][3] = -3;

	table[2][0] = 3;
	table[2][1] = -4;
	table[2][2] = -1;
	table[2][3] = 2;

	table[3][0] = 4;
	table[3][1] = 3;
	table[3][2] = -2;
	table[3][3] = -1;
}

int letter_to_int(char c) {
	return c-'i'+2;
}

int pos(string &s, long long x) {
	return letter_to_int(s[x%s.size()]);
}

char mul(int a, int b) {
	int sign = 1;
	if (a < 0) {
		a = -a;
		sign *= -1;
	}
	if (b < 0) {
		b = -b;
		sign *= -1;
	}
	return sign * table[a-1][b-1];	
}

bool calck(string &str, long long size, long long index) {
	if (index >= size) return false;
	int current = 1;
	for (long long i = index; i < size; ++i) {
		current = mul(current, pos(str, i));
	}
	return current == 4;
}

bool calcj(string &str, long long size, long long index) {
	if (index >= size) return false;
	int current = 1;
	for (long long i = index; i < size; ++i) {
		current = mul(current, pos(str, i));
		if (current == 3) {
			return calck(str, size, i+1);
		}
	}
	return false;
}

bool calc(string &str, long long size) {
	int current = 1;
	for (long long i = 0; i < size; ++i) {
		current = mul(current, pos(str, i));
		if (current == 2) {
			return calcj(str, size, i+1);
		}
	}
	return false;
}

int main() {
	init();
	int t;
	cin >> t;
	for (int c = 1; c < t+1; ++c) {
		long long l, x;
		cin >> l >> x;
		string str;
		cin >> str;
		bool b = calc(str, l*x);
		cout << "Case #" << c << ": " << (b ? "YES" : "NO") << endl;
	}
}