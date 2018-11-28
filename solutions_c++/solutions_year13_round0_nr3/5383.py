#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

/**
 * Property of square number 
 *		+ Ending digits must be 0, 1, 4, 6, 9 or 25
 */
const int palindrome[5] = {1, 4, 9, 121, 484};

bool is_perfect_square(int n) {
    int root(sqrt(n));
    return n == root * root;
}

void print(const vector<string> &v) {
	for (string s : v) {
		cout << s << endl;
	}
}

vector<string> two() {
	vector<string> r;
	for (int i = 1; i <= 9; ++i) {
		r.push_back(string(2, '0' + i));
	}
	return r;
}

vector<string> three() {
	vector<string> r;
	for (int i = 1; i <= 9; ++i) {
		for (int m = 0; m <= 9; ++m) {
			string n = string(3, '0' + i);
			n[1] = '0' + m;
			r.push_back(n);
		}
	}
	return r;
}

bool is_palindrome(int n) {
	string s;
	while (n) {
		s.push_back('0' + n % 10);
		n /= 10;
	}
	return equal(s.begin(), s.end(), s.rbegin());
}

int how_many(int bound) {
	int i = 0;
	while (i <= 4 && bound >= palindrome[i]) {
		i++;
	}
	return i;
}

int how_many(int l, int r) {
	return how_many(r) - how_many(l - 1);
}

void google_fair_and_square(istream &in, ostream &out) {
	int test_cases;
	in >> test_cases;
	int a, b;
	for (int tc = 1; tc <= test_cases; ++tc) {
		in >> a >> b;
		out << "Case #" << tc << ": " << how_many(a, b) << endl;
	}
}

int main() {
	google_fair_and_square(cin, cout);
	return 0;
}