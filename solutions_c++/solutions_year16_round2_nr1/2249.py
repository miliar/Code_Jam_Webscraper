#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
	int t;
	cin >> t;

	string str;
	ofstream ofs("GettingTheDigits.txt");

	int j = 1;
	while (j <= t) {
		cin >> str;
		int len = str.length();

		map<char, int> cmap;
		for (int i = 0; i < len; ++i) {
			cmap[str[i]]++;
		}

		vector<int> phonenumber;

		while (cmap['Z']) {
			phonenumber.push_back(0);
			cmap['Z']--; cmap['E']--; cmap['R']--; cmap['O']--;
		}

		while (cmap['W']) {
			phonenumber.push_back(2);
			cmap['T']--; cmap['W']--; cmap['O']--;
		}

		while (cmap['U']) {
			phonenumber.push_back(4);
			cmap['F']--; cmap['O']--; cmap['U']--; cmap['R']--;
		}

		while (cmap['X']) {
			phonenumber.push_back(6);
			cmap['S']--; cmap['I']--; cmap['X']--; 
		}

		while (cmap['G']) {
			phonenumber.push_back(8);
			cmap['E']--; cmap['I']--; cmap['G']--; cmap['H']--; cmap['T']--;
		}

		while (cmap['O'] && cmap['N'] && cmap['E']) {
			phonenumber.push_back(1);
			cmap['O']--; cmap['N']--; cmap['E']--;
		}

		while (cmap['T'] && cmap['H'] && cmap['R'] && cmap['E'] >= 2) {
			phonenumber.push_back(3);
			cmap['T']--; cmap['H']--; cmap['R']--; cmap['E']--; cmap['E']--;
		}

		while (cmap['F'] && cmap['I'] && cmap['V'] && cmap['E'] ) {
			phonenumber.push_back(5);
			cmap['F']--; cmap['I']--; cmap['V']--; cmap['E']--;
		}

		while (cmap['S'] && cmap['E']>=2 && cmap['V'] && cmap['N']) {
			phonenumber.push_back(7);
			cmap['S']--; cmap['E']--; cmap['E']--; cmap['V']--; cmap['N']--;
		}


		while (cmap['N'] >= 2 && cmap['I'] && cmap['E']) {
			phonenumber.push_back(9);
			cmap['N']--; cmap['I']--; cmap['N']--; cmap['E']--;
		}

		sort(phonenumber.begin(), phonenumber.end());

		ofs << "Case #" << j++ << ": ";
		for (int i = 0; i < phonenumber.size(); ++i) {
			ofs << phonenumber[i];
		}

		ofs << endl;
	}
}