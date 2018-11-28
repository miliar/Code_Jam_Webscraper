#include "string.h"
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <stack>
#include <list>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <limits.h>
#include <fstream>
using namespace std;

int main(){

	int t;
	ifstream istream;
	istream.open("input.in");
	istream >> t;
	//cin >> t;
	ofstream ostream;
	ostream.open("output.in");
	string s;
	for (int i = 1; i <= t; i++){

		istream >> s;
		int count[10] = { 0 };
		int digital[26] = { 0 };

		string m[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
		for (int i = 0; i < s.length(); i++){
			digital[s[i] - 'A']++;
		}

		count[0] = digital['Z' - 'A'];
		for (int i = 0; i < m[0].size(); i++) digital[m[0][i] - 'A'] -= count[0];

		count[4] = digital['U' - 'A'];
		for (int i = 0; i < m[4].size(); i++) digital[m[4][i] - 'A'] -= count[4];

		count[3] = digital['R' - 'A'];
		for (int i = 0; i < m[3].size(); i++) digital[m[3][i] - 'A'] -= count[3];

		count[8] = digital['G' - 'A'];
		for (int i = 0; i < m[8].size(); i++) digital[m[8][i] - 'A'] -= count[8];

		count[2] = digital['T' - 'A'];
		for (int i = 0; i < m[2].size(); i++) digital[m[2][i] - 'A'] -= count[2];

		count[1] = digital['O' - 'A'];
		for (int i = 0; i < m[1].size(); i++) digital[m[1][i] - 'A'] -= count[1];

		count[6] = digital['X' - 'A'];
		for (int i = 0; i < m[6].size(); i++) digital[m[6][i] - 'A'] -= count[6];

		count[7] = digital['S' - 'A'];
		for (int i = 0; i < m[7].size(); i++) digital[m[7][i] - 'A'] -= count[7];		

		count[5] = digital['F' - 'A'];
		for (int i = 0; i < m[5].size(); i++) digital[m[5][i] - 'A'] -= count[5];

		count[9] = digital['I' - 'A'];
		for (int i = 0; i < m[9].size(); i++) digital[m[9][i] - 'A'] -= count[9];

		ostream << "Case #" << i << ": ";
		
		for (int i = 0; i < 10; i++){

			for (int j = 0; j < count[i]; j++) ostream << i;
		}

		ostream << endl;
	}
	return 0;
}