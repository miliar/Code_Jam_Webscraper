#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <queue>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("largeoutput.txt");
	int caseNum;
	in >> caseNum;
	for (int i = 1; i <= caseNum; ++i) {
		int arr[26];
		string s, ret = "";
		in >> s;
		for (int j = 0; j < 26; j++)
			arr[j] = 0;
		for (auto c : s) {
			arr[c - 'A']++;
		}
		if (arr['Z' - 'A'] != 0) {
			for (int j = 0; arr['Z' - 'A']>0; j++) {
				ret += "0";
				arr['Z' - 'A']--;
				arr['E' - 'A']--;
				arr['R' - 'A']--;
				arr['O' - 'A']--;
			}
		}
		if (arr['W' - 'A'] != 0) {
			for (int j = 0; arr['W' - 'A']>0; j++) {
				ret += "2";
				arr['T' - 'A']--;
				arr['W' - 'A']--;
				arr['O' - 'A']--;
			}
		}
		if (arr['X' - 'A'] != 0) {
			for (int j = 0;arr['X' - 'A']>0; j++) {
				ret += "6";
				arr['S' - 'A']--;
				arr['I' - 'A']--;
				arr['X' - 'A']--;
			}
		}

		if (arr['G' - 'A'] != 0) {
			for (int j = 0; arr['G' - 'A']>0; j++) {
				ret += "8";
				arr['E' - 'A']--;
				arr['I' - 'A']--;
				arr['G' - 'A']--;
				arr['H' - 'A']--;
				arr['T' - 'A']--;
			}
		}
		if (arr['H' - 'A'] != 0) {
			for (int j = 0; arr['H' - 'A']>0; j++) {
				ret += "3";
				arr['T' - 'A']--;
				arr['H' - 'A']--;
				arr['R' - 'A']--;
				arr['E' - 'A']--;
				arr['E' - 'A']--;
			}
		}
		if (arr['U' - 'A'] != 0) {
			for (int j = 0; arr['U' - 'A']>0; j++) {
				ret += "4";
				arr['F' - 'A']--;
				arr['O' - 'A']--;
				arr['U' - 'A']--;
				arr['R' - 'A']--;
			}
		}

		if (arr['F' - 'A'] != 0) {
			for (int j = 0; arr['F' - 'A']>0; j++) {
				ret += "5";
				arr['F' - 'A']--;
				arr['I' - 'A']--;
				arr['V' - 'A']--;
				arr['E' - 'A']--;
			}
		}
		if (arr['I' - 'A'] != 0) {
			for (int j = 0; arr['I' - 'A']>0; j++) {
				ret += "9";
				arr['N' - 'A']--;
				arr['I' - 'A']--;
				arr['N' - 'A']--;
				arr['E' - 'A']--;
			}
		}
		if (arr['V' - 'A'] != 0) {
			for (int j = 0; arr['V' - 'A']>0; j++) {
				ret += "7";
				arr['S' - 'A']--;
				arr['E' - 'A']--;
				arr['V' - 'A']--;
				arr['E' - 'A']--;
				arr['N' - 'A']--;
			}
		}
		if (arr['O' - 'A'] != 0) {
			for (int j = 0; arr['O' - 'A'] > 0; j++) {
				ret += "1";
				arr['O' - 'A']--;
				arr['N' - 'A']--;
				arr['E' - 'A']--;
			}
		}
		sort(ret.begin(), ret.end());
		out << "Case #" << i << ": " << ret<<endl;
	}
	return 0;
}
