// GettingDigits.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
	int t;
	cin >> t;

	unordered_map<char, int> m;

	for (int x = 1; x <= t; ++x) {
		string s;
		cin >> s;

		m.clear();
		for (int i = 0; i < s.length(); ++i) {
			m[s[i]]++;
		}

		vector<int> digits;
		digits.resize(10);

		digits[0] = m['Z'];
		m['Z'] -= digits[0];
		m['E'] -= digits[0];
		m['R'] -= digits[0];
		m['O'] -= digits[0];

		digits[2] = m['W'];
		m['T'] -= digits[2];
		m['W'] -= digits[2];
		m['O'] -= digits[2];

		digits[4] = m['U'];
		m['F'] -= digits[4];
		m['O'] -= digits[4];
		m['U'] -= digits[4];
		m['R'] -= digits[4];

		digits[6] = m['X'];
		m['S'] -= digits[6];
		m['I'] -= digits[6];
		m['X'] -= digits[6];

		digits[8] = m['G'];
		m['E'] -= digits[8];
		m['I'] -= digits[8];
		m['G'] -= digits[8];
		m['H'] -= digits[8];
		m['T'] -= digits[8];

		digits[1] = m['O'];
		m['O'] -= digits[1];
		m['N'] -= digits[1];
		m['E'] -= digits[1];

		digits[3] = m['T'];
		m['T'] -= digits[3];
		m['H'] -= digits[3];
		m['R'] -= digits[3];
		m['E'] -= digits[3];
		m['E'] -= digits[3];

		digits[5] = m['F'];
		m['F'] -= digits[5];
		m['I'] -= digits[5];
		m['V'] -= digits[5];
		m['E'] -= digits[5];

		digits[7] = m['S'];
		m['S'] -= digits[7];
		m['E'] -= digits[7];
		m['V'] -= digits[7];
		m['E'] -= digits[7];
		m['N'] -= digits[7];

		digits[9] = m['I'];

		cout << "Case #" << x << ": ";
		for (int i = 0; i < 10; ++i) {
			while (digits[i]) {
				cout << i;
				digits[i]--;
			}
		}
		cout << endl;
	}
    return 0;
}

