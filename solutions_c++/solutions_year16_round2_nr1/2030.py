#include <iostream>
#include <set>
#include <map>
#include <list>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstring>
#include <numeric>

using namespace std;


int main(int argc, char** argv)
{
	if (argc != 3)
		return -1;

	ifstream in(argv[1]);
	ofstream out(argv[2]);

	int t;

	in >> t;

	for (int caseN = 1; caseN <= t; ++caseN) {
		out << "Case #" << caseN << ": ";

		string s;
		in >> s;

		list<char> phoneNumber;
		map<char, int> chars;

		for (unsigned int i = 0; i < s.length(); ++i) {

			char c = s.at(i);
			++chars[c];
		}

		// ZERO
		int nbDigit = chars['Z'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('0');
		}
		chars['Z'] = 0;
		chars['E'] -= nbDigit;
		chars['R'] -= nbDigit;
		chars['O'] -= nbDigit;

		// TWO
		nbDigit = chars['W'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('2');
		}
		chars['W'] = 0;
		chars['T'] -= nbDigit;
		chars['O'] -= nbDigit;

		// FOUR
		nbDigit = chars['U'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('4');
		}
		chars['U'] = 0;
		chars['F'] -= nbDigit;
		chars['O'] -= nbDigit;
		chars['R'] -= nbDigit;

		// FIVE
		nbDigit = chars['F'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('5');
		}
		chars['F'] = 0;
		chars['I'] -= nbDigit;
		chars['V'] -= nbDigit;
		chars['E'] -= nbDigit;

		// SIX
		nbDigit = chars['X'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('6');
		}
		chars['X'] = 0;
		chars['S'] -= nbDigit;
		chars['I'] -= nbDigit;

		// SEVEN
		nbDigit = chars['V'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('7');
		}
		chars['V'] = 0;
		chars['S'] -= nbDigit;
		chars['E'] -= nbDigit;
		chars['E'] -= nbDigit;
		chars['N'] -= nbDigit;

		// EIGHT
		nbDigit = chars['G'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('8');
		}
		chars['G'] = 0;
		chars['E'] -= nbDigit;
		chars['I'] -= nbDigit;
		chars['H'] -= nbDigit;
		chars['T'] -= nbDigit;

		// THREE
		nbDigit = chars['H'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('3');
		}
		chars['H'] = 0;
		chars['T'] -= nbDigit;
		chars['R'] -= nbDigit;
		chars['E'] -= nbDigit;
		chars['E'] -= nbDigit;

		// NINE
		nbDigit = chars['I'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('9');
		}
		chars['I'] = 0;
		chars['N'] -= nbDigit;
		chars['N'] -= nbDigit;
		chars['E'] -= nbDigit;

		// ONE
		nbDigit = chars['O'];
		for (int k = 0; k < nbDigit; ++k) {
			phoneNumber.push_back('1');
		}
		chars['O'] = 0;
		chars['N'] -= nbDigit;
		chars['E'] -= nbDigit;

		phoneNumber.sort();

		for (list<char>::iterator it = phoneNumber.begin(); it != phoneNumber.end(); ++it) {
			out << *it;
		}

		out << endl;
	}

	in.close();
	out.close();

	return 0;
}



