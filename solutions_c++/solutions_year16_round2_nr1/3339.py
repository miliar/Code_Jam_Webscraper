#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
//#include <climits>
using namespace std;

void f() {
	vector<int> v(10, 0);
	size_t i;
	string s; cin >> s;
	while ( (i = s.find('Z')) != string::npos ) {
		++v[0];
		s[i] = ' ';
		s[s.find('E')] = ' ';
		s[s.find('R')] = ' ';
		s[s.find('O')] = ' ';
	}
	while ( (i = s.find('W')) != string::npos ) {
		++v[2];
		s[i] = ' ';
		s[s.find('T')] = ' ';
		s[s.find('O')] = ' ';
	}
	while ( (i = s.find('X')) != string::npos ) {
		++v[6];
		s[i] = ' ';
		s[s.find('S')] = ' ';
		s[s.find('I')] = ' ';
	}
	while ( (i = s.find('G')) != string::npos ) {
		++v[8];
		s[i] = ' ';
		s[s.find('E')] = ' ';
		s[s.find('I')] = ' ';
		s[s.find('H')] = ' ';
		s[s.find('T')] = ' ';
	}
	while ( (i = s.find('H')) != string::npos ) {
		++v[3];
		s[i] = ' ';
		s[s.find('T')] = ' ';
		s[s.find('R')] = ' ';
		s[s.find('E')] = ' ';
		s[s.find('E')] = ' ';
	}
	while ( (i = s.find('S')) != string::npos ) {
		++v[7];
		s[i] = ' ';
		s[s.find('E')] = ' ';
		s[s.find('V')] = ' ';
		s[s.find('E')] = ' ';
		s[s.find('N')] = ' ';
	}
	while ( (i = s.find('V')) != string::npos ) {
		++v[5];
		s[i] = ' ';
		s[s.find('F')] = ' ';
		s[s.find('I')] = ' ';
		s[s.find('E')] = ' ';
	}
	while ( (i = s.find('F')) != string::npos ) {
		++v[4];
		s[i] = ' ';
		s[s.find('O')] = ' ';
		s[s.find('U')] = ' ';
		s[s.find('R')] = ' ';
	}
	while ( (i = s.find('O')) != string::npos ) {
		++v[1];
		s[i] = ' ';
		s[s.find('N')] = ' ';
		s[s.find('E')] = ' ';
	}
	while ( (i = s.find('I')) != string::npos ) {
		++v[9];
		s[i] = ' ';
		s[s.find('N')] = ' ';
		s[s.find('N')] = ' ';
		s[s.find('E')] = ' ';
	}
	for (size_t j = 0; j < v.size(); ++j)
		for (int k = 0; k < v[j]; ++k)
			cout << j;
	cout << endl;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		f();
	}
	//cout << LLONG_MAX << endl;
}
