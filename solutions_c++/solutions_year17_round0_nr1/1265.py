#define _CRT_SECURE_NO_WARNINGS


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <unordered_map> //C++11
using namespace std;

typedef long long ll;

int t;
string s;
int k, ct;
bool flag;

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> s >> k;
		ct = 0;
		flag = false;
		for (int j = 0; j <= s.length() - k; j++) {
			if (s.at(j) == '-') {
				for (int l = j; l < j + k; l++) {
					if (s.at(l) == '+') s.at(l) = '-';
					else s.at(l) = '+';
				}
				ct++;
			}
		}
		for (int j = 0; j < s.length(); j++) {
			if (s.at(j) == '-') {
				flag = true;
				break;
			}
		}
		if (flag) cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << i << ": " << ct << endl;
	}
	return 0;
}
