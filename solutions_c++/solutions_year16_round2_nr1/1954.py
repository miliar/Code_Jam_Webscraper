#include <iostream>
#include <fstream>
#include <string>
using namespace std;

static int caseNum = 1;
void getDigits(string input, ofstream& out) {
	int alpha[26];
	int number[10];
	for (int i = 0; i < 10; i++) {
		number[i] = 0;
	}
	for (int i = 0; i < 26; i++) {
		alpha[i] = 0;
	}
	for (int i = 0; i < input.length();i++) {
		alpha[input[i] - 'A']++;
	}
	while (alpha['Z' - 'A'] != 0) {
		number[0]++;
		alpha['Z' - 'A']--;
		alpha['E' - 'A']--;
		alpha['R' - 'A']--;
		alpha['O' - 'A']--;
	}
	while (alpha['W' - 'A'] != 0) {
		number[2]++;
		alpha['T' - 'A']--;
		alpha['W' - 'A']--;
		alpha['O' - 'A']--;
	}
	while (alpha['U' - 'A'] != 0) {
		number[4]++;
		alpha['F' - 'A']--;
		alpha['O' - 'A']--;
		alpha['U' - 'A']--;
		alpha['R' - 'A']--;
	}
	while (alpha['X' - 'A'] != 0) {
		number[6]++;
		alpha['S' - 'A']--;
		alpha['I' - 'A']--;
		alpha['X' - 'A']--;
	}
	while (alpha['G' - 'A'] != 0) {
		number[8]++;
		alpha['E' - 'A']--;
		alpha['I' - 'A']--;
		alpha['G' - 'A']--;
		alpha['H' - 'A']--;
		alpha['T' - 'A']--;
	}
	while (alpha['T' - 'A'] != 0) {
		number[3]++;
		alpha['T' - 'A']--;
		alpha['H' - 'A']--;
		alpha['R' - 'A']--;
		alpha['E' - 'A']--;
		alpha['E' - 'A']--;
	}
	while (alpha['F' - 'A'] != 0) {
		number[5]++;
		alpha['F' - 'A']--;
		alpha['I' - 'A']--;
		alpha['V' - 'A']--;
		alpha['E' - 'A']--;
	}
	while (alpha['V' - 'A'] != 0) {
		number[7]++;
		alpha['S' - 'A']--;
		alpha['E' - 'A']--;
		alpha['V' - 'A']--;
		alpha['E' - 'A']--;
		alpha['N' - 'A']--;
	}
	while (alpha['O' - 'A'] != 0) {
		number[1]++;
		alpha['O' - 'A']--;
		alpha['N' - 'A']--;
		alpha['E' - 'A']--;
	}
	while (alpha['I' - 'A'] != 0) {
		number[9]++;
		alpha['N' - 'A']--;
		alpha['I' - 'A']--;
		alpha['N' - 'A']--;
		alpha['E' - 'A']--;
	}
	cout << "Case #" << caseNum << ": " ;
	out << "Case #" << caseNum << ": ";
	for (int i = 0; i < 10; i++) {
		for (int j = number[i]; j > 0; j--) {
			cout << i;
			out << i;
		}
	}
	cout << endl;
	out << endl;
}

int main() {
	string temp;
	ifstream file("A-large.in");
	ofstream out("output.out");
	int T;
	file >> temp;
	T = stoi(temp);
	if (T >= 1 && T <= 100) {
		while (T != 0) {
			file >> temp;
			getDigits(temp, out);
			caseNum++;
			T--;
		}
	}
	return 0;
}