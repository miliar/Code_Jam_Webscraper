#include <fstream>
//#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

ifstream cin("input.in");
ofstream cout("output.out");

int i, j, k, t, n, u;
string s, s1;

void change(int x, int y) {
	int i;
	for (i = x; i <= y; i++) {
		if (s[i] == '+') {
			s[i] = '-';
		}
		else s[i] = '+';
	}

}

char swapmark1(char c) {
	if (c == '+') {
		return '-';
	}
	else return '+';
}


int main() {
	cin >> t;
	int l;
	for (i = 1; i <= t; i++) {
		k = 0;
		cin >> s;
		l = s.length()-1;
		while (l >= 0) {
			if (s[l] == '-') {
				change(0, l);
				k++;
			}
			l--;
		}
	//	char x = swapmark1('+');
		cout << "Case #"<<i<<": "<<k << endl;
	}
//	system("pause");
	return 0;
}
