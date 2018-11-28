#include <string>
#include <iostream>
#include <sstream>
#include <list>
#include <map>

using namespace std;

int main() {
	int t; cin >> t;

	for (int i = 1; i <= t; ++i) {
		std::string s; cin >> s;

		int digits[10] = {0,0,0,0,0,0,0,0,0,0};

		map<char, int> letter;

		for (int j = 0; j < s.size(); ++j) {
			if (letter.count(s.at(j))) {
				letter[s.at(j)]++;
			} else {
				letter[s.at(j)] = 1;
			}
		}

		while (letter['Z']) {
			digits[0]++;
			letter['Z']--;
			letter['E']--;
			letter['R']--;
			letter['O']--;
		}

		while (letter['W']) {
			digits[2]++;
			letter['T']--;
			letter['W']--;
			letter['O']--;
		}

		while (letter['U']) {
			digits[4]++;
			letter['F']--;
			letter['O']--;
			letter['U']--;
			letter['R']--;
		}

		while (letter['X']) {
			digits[6]++;
			letter['S']--;
			letter['I']--;
			letter['X']--;
		}

		while (letter['G']) {
			digits[8]++;
			letter['E']--;
			letter['I']--;
			letter['G']--;
			letter['H']--;
			letter['T']--;
		}

		while (letter['O']) {
			digits[1]++;
			letter['O']--;
			letter['N']--;
			letter['E']--;
		}

		while (letter['F']) {
			digits[5]++;
			letter['F']--;
			letter['I']--;
			letter['V']--;
			letter['E']--;
		}

		while (letter['S']) {
			digits[7]++;
			letter['S']--;
			letter['E']--;
			letter['V']--;
			letter['E']--;
			letter['N']--;
		}

		while (letter['H']) {
			digits[3]++;
			letter['T']--;
			letter['H']--;
			letter['R']--;
			letter['E']--;
			letter['E']--;
		}

		while (letter['N']) {
			digits[9]++;
			letter['N']--;
			letter['I']--;
			letter['N']--;
			letter['E']--;
		}

		cout <<	"Case #" << i << ": ";

		for (int j = 0; j < 10; ++j) {
			for (int k = 0; k < digits[j]; ++k) {
				cout << j;
			}
		}

		cout << endl;

	}

	return 0;
}
