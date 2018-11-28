#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <limits>
#include <algorithm>
#define _USE_MATH_DEFINES
#define vi vector<int>
using namespace std;
int m[10][26];
string num[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string find(vector<int> v) {
	bool imPos [10] = {0,0,0,0,0,0,0,0,0,0};
	for (int i = 0; i < 10; i++) {
		bool poss = true;
		bool imposs = false;
		for (int j = 0; j < 26; j++) {
			if (m[i][j] != v[j])
				poss = false;
			if (m[i][j] > v[j])
				imposs = true;
			if (imposs)
				break;
		}
		if (poss) {
			char ret[2];
			return _itoa(i, ret, 10);
		}
		imPos[i] = imposs;
	}
	for (int i = 0; i < 10; i++) {
		if (imPos[i])
			continue;
		vector<int> newvec (26);
		for (int j = 0; j < 26; j++)
			newvec[j] = v[j] - m[i][j];
		string s = find(newvec);
		if (s.compare("-1") != 0) {
			char ret[2];
			return s + _itoa(i, ret, 10);
		}
	}
	return "-1";
}
int main () {
	freopen ("D:\\Internet\\A-small-attempt0.in", "r", stdin);
	freopen ("A-small.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < 10; i++) {
		for (size_t j = 0; j < num[i].length(); j++)
			m[i][num[i][j] - 'A']++;
	}
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		vector<int> v (26);
		for (size_t i = 0; i < s.length(); i++)
			v[s[i] - 'A']++;
		s = find(v);
		char *arr = (char *) s.c_str();
		sort(arr, arr + s.length());
		cout << "Case #" << t << ": " << arr << endl;
	}
}