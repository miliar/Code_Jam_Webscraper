#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int TestCase = 1; TestCase <= T; TestCase++) {
		string str;
		cin >> str;

		vector<int> v;

		int alpha[50] = { 0, };

		for (int i = 0; i < str.size(); i++) {
			alpha[str[i] - 'A']++;
		}

		// 0 2 6 7 5 3 8 9 1
		while (alpha['Z' - 'A'] > 0) {
			v.push_back(0);
			alpha['Z' - 'A']--;
			alpha['E' - 'A']--;
			alpha['R' - 'A']--;
			alpha['O' - 'A']--;
		}
		while (alpha['W' - 'A'] > 0) {
			v.push_back(2);
			alpha['T' - 'A']--;
			alpha['W' - 'A']--;
			alpha['O' - 'A']--;
		}
		while (alpha['X' - 'A'] > 0) {
			v.push_back(6);
			alpha['S' - 'A']--;
			alpha['I' - 'A']--;
			alpha['X' - 'A']--;
		}
		while (alpha['U' - 'A'] > 0) {
			v.push_back(4);
			alpha['F' - 'A']--;
			alpha['O' - 'A']--;
			alpha['U' - 'A']--;
			alpha['R' - 'A']--;
		}
		while (alpha['S' - 'A'] > 0) {
			v.push_back(7);
			alpha['S' - 'A']--;
			alpha['E' - 'A']--;
			alpha['V' - 'A']--;
			alpha['E' - 'A']--;
			alpha['N' - 'A']--;
		}
		while (alpha['V' - 'A'] > 0) {
			v.push_back(5);
			alpha['F' - 'A']--;
			alpha['I' - 'A']--;
			alpha['V' - 'A']--;
			alpha['E' - 'A']--;
		}
		while (alpha['R' - 'A'] > 0) {
			v.push_back(3);
			alpha['T' - 'A']--;
			alpha['H' - 'A']--;
			alpha['R' - 'A']--;
			alpha['E' - 'A']--;
			alpha['E' - 'A']--;
		}
		while (alpha['G' - 'A'] > 0) {
			v.push_back(8);
			alpha['E' - 'A']--;
			alpha['I' - 'A']--;
			alpha['G' - 'A']--;
			alpha['H' - 'A']--;
			alpha['T' - 'A']--;
		}
		while (alpha['I' - 'A'] > 0) {
			v.push_back(9);
			alpha['N' - 'A']--;
			alpha['I' - 'A']--;
			alpha['N' - 'A']--;
			alpha['E' - 'A']--;
		}
		while (alpha['O' - 'A'] > 0) {
			v.push_back(1);
			alpha['O' - 'A']--;
			alpha['N' - 'A']--;
			alpha['E' - 'A']--;
		}

		sort(v.begin(), v.end());

		printf("Case #%d: ", TestCase);
		for (int i = 0; i < v.size(); i++)
			printf("%d", v[i]);
		printf("\n");
	}


	return 0;
}