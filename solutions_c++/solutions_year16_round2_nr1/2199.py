#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

string S;
int char_num[256];
int int_num[10];

void run_case(int tc) {
    cin >> S;
	memset(char_num, 0, sizeof(char_num));
	memset(int_num, 0, sizeof(int_num));
	for (int i = 0; i < S.size(); i++)
		char_num[S[i]]++;
	while (char_num['Z'] > 0) {
		int_num[0]++;
		char_num['Z']--;
		char_num['E']--;
		char_num['R']--;
		char_num['O']--;
	}
	while (char_num['W'] > 0) {
		int_num[2]++;
		char_num['T']--;
		char_num['W']--;
		char_num['O']--;
	}
	while (char_num['U'] > 0) {
		int_num[4]++;
		char_num['F']--;
		char_num['O']--;
		char_num['U']--;
		char_num['R']--;
	}
	while (char_num['G'] > 0) {
		int_num[8]++;
		char_num['E']--;
		char_num['I']--;
		char_num['G']--;
		char_num['H']--;
		char_num['T']--;
	}
	while (char_num['X'] > 0) {
		int_num[6]++;
		char_num['S']--;
		char_num['I']--;
		char_num['X']--;
	}
	while (char_num['F'] > 0) {
		int_num[5]++;
		char_num['F']--;
		char_num['I']--;
		char_num['V']--;
		char_num['E']--;
	}
	while (char_num['T'] > 0) {
		int_num[3]++;
		char_num['T']--;
		char_num['H']--;
		char_num['R']--;
		char_num['E']--;
		char_num['E']--;
	}
	while (char_num['S'] > 0) {
		int_num[7]++;
		char_num['S']--;
		char_num['E']--;
		char_num['V']--;
		char_num['E']--;
		char_num['N']--;
	}
	while (char_num['O'] > 0) {
		int_num[1]++;
		char_num['O']--;
		char_num['N']--;
		char_num['E']--;
	}
	while (char_num['I'] > 0) {
		int_num[9]++;
		char_num['N']--;
		char_num['I']--;
		char_num['N']--;
		char_num['E']--;
	}
	cout << "Case #" << tc << ": ";
	for (int i = 0; i < 10; i++)
		for (int j = 0; j < int_num[i]; j++)
			cout << i;
	cout << endl;
}

int main() {
	int num = 0;
	cin >> num;
	for (int i = 1; i <= num; ++i) {
		run_case(i);
	}
	return 0;
}