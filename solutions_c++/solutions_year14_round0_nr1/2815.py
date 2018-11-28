
#include <cstdio>
#include <cstring>
#include <cctype>

#include <deque>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

using namespace std;


void p(int id) {
	int r1, r2;
	bool s[16] = {};
	cin >> r1;
	--r1;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			int a;
			cin >> a;
			if ( i == r1 ) s[a-1] = true;
		}
	}
	cin >> r2;
	--r2;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			int a;
			cin >> a;
			if ( i != r2 ) s[a-1] = false;
		}
	}
	int a, c = 0;
	for (int i = 0; i < 16; ++i) {
		if ( !s[i] ) continue;
		a = i+1;
		++c;
	}
	cout << "Case #" << id << ": ";
	if ( c == 0 ) cout << "Volunteer cheated!";
	else if ( c == 1 ) cout << a;
	else cout << "Bad magician!";
	cout << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		p(i);
	return 0;
}

